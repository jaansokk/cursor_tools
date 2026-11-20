"""Exercise package replacement in temporary directories, never user installs."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "install_ui_design", Path(__file__).resolve().parents[1] / "install_ui_design.py"
)
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallSkillTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.source = self.root / "repo" / "skills" / "ui-design"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text("New principles\n")
        self.destination = self.root / "toolhome" / "skills" / "ui-design"

    def test_replacement_removes_stale_files_and_preserves_backup(self):
        self.destination.mkdir(parents=True)
        (self.destination / "SKILL.md").write_text("Old instructions\n")
        stale = self.destination / "references" / "tailwind.md"
        stale.parent.mkdir()
        stale.write_text("Old framework rules\n")

        backup = installer.install_skill(self.destination, self.source)

        self.assertEqual((self.destination / "SKILL.md").read_text(), "New principles\n")
        self.assertFalse((self.destination / "references").exists())
        self.assertEqual((backup / "SKILL.md").read_text(), "Old instructions\n")
        self.assertEqual((backup / "references" / "tailwind.md").read_text(), "Old framework rules\n")
        self.assertNotIn(self.destination.parent, backup.parents)

    def test_destination_symlink_is_replaced_without_changing_target(self):
        target = self.root / "other-package"
        target.mkdir()
        (target / "SKILL.md").write_text("Keep this target\n")
        self.destination.parent.mkdir(parents=True)
        self.destination.symlink_to(target, target_is_directory=True)

        backup = installer.install_skill(self.destination, self.source)

        self.assertFalse(self.destination.is_symlink())
        self.assertEqual((target / "SKILL.md").read_text(), "Keep this target\n")
        self.assertTrue(backup.is_symlink())
        self.assertEqual(backup.resolve(), target)

    def test_rejects_source_overlap_in_either_direction(self):
        destinations = (
            self.source,
            self.source / "nested" / "ui-design",
        )
        for destination in destinations:
            with self.subTest(destination=destination):
                with self.assertRaisesRegex(ValueError, "overlap"):
                    installer.install_skill(destination, self.source)
        ancestor = self.root / "ui-design"
        nested_source = ancestor / "skills" / "ui-design"
        nested_source.mkdir(parents=True)
        (nested_source / "SKILL.md").write_text("Nested source\n")
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install_skill(ancestor, nested_source)
        self.assertEqual((self.source / "SKILL.md").read_text(), "New principles\n")

    def test_rejects_source_overlap_via_parent_or_destination_symlink(self):
        parent_link = self.root / "linked-skills"
        parent_link.symlink_to(self.source.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install_skill(parent_link / "ui-design", self.source)
        self.destination.parent.mkdir(parents=True)
        self.destination.symlink_to(self.source, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install_skill(self.destination, self.source)
        self.assertTrue(self.destination.is_symlink())

    def test_copy_is_independent_and_dereferences_source_links(self):
        shared = self.root / "shared.md"
        shared.write_text("Shared reference\n")
        (self.source / "reference.md").symlink_to(shared)

        self.assertIsNone(installer.install_skill(self.destination, self.source))
        (self.destination / "SKILL.md").write_text("Local modification\n")
        shared.write_text("Changed upstream\n")

        self.assertEqual((self.source / "SKILL.md").read_text(), "New principles\n")
        self.assertFalse((self.destination / "reference.md").is_symlink())
        self.assertEqual((self.destination / "reference.md").read_text(), "Shared reference\n")

    def test_install_failure_restores_previous_package(self):
        self.destination.mkdir(parents=True)
        (self.destination / "SKILL.md").write_text("Previous package\n")
        real_replace = os.replace

        def fail_staged_install(source, destination):
            if Path(source).parent.name.startswith(".ui-design-install-"):
                raise OSError("Simulated install failure")
            return real_replace(source, destination)

        with patch.object(installer.os, "replace", side_effect=fail_staged_install):
            with self.assertRaisesRegex(OSError, "Simulated install failure"):
                installer.install_skill(self.destination, self.source)

        self.assertEqual((self.destination / "SKILL.md").read_text(), "Previous package\n")
        self.assertEqual(list(self.destination.parent.glob(".ui-design-install-*")), [])

    def test_copy_failure_leaves_previous_package_in_place(self):
        self.destination.mkdir(parents=True)
        (self.destination / "SKILL.md").write_text("Previous package\n")
        (self.source / "broken.md").symlink_to(self.root / "missing.md")

        with self.assertRaises(installer.shutil.Error):
            installer.install_skill(self.destination, self.source)

        self.assertEqual((self.destination / "SKILL.md").read_text(), "Previous package\n")
        self.assertFalse((self.destination.parent.parent / "skill-backups").exists())

    def test_install_failure_restores_relative_destination_symlink(self):
        target = self.destination.parent.parent / "original"
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("Keep target\n")
        self.destination.parent.mkdir()
        self.destination.symlink_to("../original", target_is_directory=True)
        real_replace = os.replace

        def fail_staged_install(source, destination):
            if Path(source).parent.name.startswith(".ui-design-install-"):
                raise OSError("Simulated install failure")
            return real_replace(source, destination)

        with patch.object(installer.os, "replace", side_effect=fail_staged_install):
            with self.assertRaisesRegex(OSError, "Simulated install failure"):
                installer.install_skill(self.destination, self.source)

        self.assertTrue(self.destination.is_symlink())
        self.assertEqual(os.readlink(self.destination), "../original")
        self.assertEqual((target / "SKILL.md").read_text(), "Keep target\n")

    def test_replaces_broken_destination_symlink(self):
        self.destination.parent.mkdir(parents=True)
        self.destination.symlink_to(self.root / "missing", target_is_directory=True)

        backup = installer.install_skill(self.destination, self.source)

        self.assertTrue((self.destination / "SKILL.md").is_file())
        self.assertTrue(backup.is_symlink())
        self.assertFalse((self.root / "missing").exists())

    def test_rejects_other_destination_names(self):
        with self.assertRaisesRegex(ValueError, "named ui-design"):
            installer.install_skill(self.root / "skills", self.source)


if __name__ == "__main__":
    unittest.main()
