#!/usr/bin/env sh
#
# Copy Cursor tools from this project to ~/.cursor for global use.
# Run from project root or .cursor directory.
#
# Usage:
#   ./copy-to-global.sh           # copy all (agents, skills, rules, commands)
#   ./copy-to-global.sh --all     # same
#   ./copy-to-global.sh --agents  # copy only agents
#   ./copy-to-global.sh --skills  # copy only skills
#   ./copy-to-global.sh --rules   # copy only rules
#   ./copy-to-global.sh --commands # copy only commands
#   ./copy-to-global.sh --agents --skills  # copy multiple
#

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CURSOR_DIR="${SCRIPT_DIR}"
GLOBAL_DIR="${HOME}/.cursor"
SKILLS_GLOBAL="${GLOBAL_DIR}/skills-cursor"

copy_agents() {
  echo "Copying agents..."
  mkdir -p "${GLOBAL_DIR}/agents"
  for f in "${CURSOR_DIR}"/agents/*.md; do
    [ -f "$f" ] || continue
    name=$(basename "$f")
    cp "$f" "${GLOBAL_DIR}/agents/${name}"
    # Update skill paths in engineer agent for global use
    if [ "$name" = "engineer.md" ]; then
      tmp=$(mktemp)
      sed 's|\.cursor/skills/|~/.cursor/skills-cursor/|g' "${GLOBAL_DIR}/agents/${name}" > "$tmp"
      mv "$tmp" "${GLOBAL_DIR}/agents/${name}"
    fi
  done
  echo "  -> ${GLOBAL_DIR}/agents/"
}

copy_skills() {
  echo "Copying skills..."
  mkdir -p "${SKILLS_GLOBAL}"
  for d in "${CURSOR_DIR}"/skills/*; do
    [ -d "$d" ] || continue
    name=$(basename "$d")
    # Use dir path without trailing slash so cp copies the directory itself, not its contents
    cp -r "${CURSOR_DIR}/skills/${name}" "${SKILLS_GLOBAL}/"
    echo "  -> ${SKILLS_GLOBAL}/${name}/"
  done
}

copy_rules() {
  echo "Copying rules..."
  mkdir -p "${GLOBAL_DIR}/rules"
  cp "${CURSOR_DIR}"/rules/*.mdc "${GLOBAL_DIR}/rules/" 2>/dev/null || true
  echo "  -> ${GLOBAL_DIR}/rules/"
}

copy_commands() {
  echo "Copying commands..."
  mkdir -p "${GLOBAL_DIR}/commands"
  for f in "${CURSOR_DIR}"/commands/*.md; do
    [ -f "$f" ] || continue
    cp "$f" "${GLOBAL_DIR}/commands/"
  done
  echo "  -> ${GLOBAL_DIR}/commands/"
}

# Parse args; if none, copy all
DO_ALL=false
DO_AGENTS=false
DO_SKILLS=false
DO_RULES=false
DO_COMMANDS=false

for arg in "$@"; do
  case "$arg" in
    --all)      DO_ALL=true ;;
    --agents)   DO_AGENTS=true ;;
    --skills)   DO_SKILLS=true ;;
    --rules)    DO_RULES=true ;;
    --commands) DO_COMMANDS=true ;;
    -h|--help)
      echo "Usage: $0 [--all] [--agents] [--skills] [--rules] [--commands]"
      echo "  --all      copy all (default when no args)"
      echo "  --agents   copy only agents"
      echo "  --skills   copy only skills"
      echo "  --rules    copy only rules"
      echo "  --commands copy only commands"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 1
      ;;
  esac
done

if [ "$DO_ALL" = true ] || [ "$#" -eq 0 ]; then
  DO_AGENTS=true
  DO_SKILLS=true
  DO_RULES=true
  DO_COMMANDS=true
fi

[ "$DO_AGENTS" = true ] && copy_agents
[ "$DO_SKILLS" = true ] && copy_skills
[ "$DO_RULES" = true ] && copy_rules
[ "$DO_COMMANDS" = true ] && copy_commands

echo "Done."
