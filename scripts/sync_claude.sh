#!/usr/bin/env sh
#
# Sync Claude Code tools from this project to ~/.claude for global use.
#
# Usage:
#   scripts/sync_claude.sh              # sync all (agents, skills, CLAUDE.md)
#   scripts/sync_claude.sh --all        # same
#   scripts/sync_claude.sh --agents     # sync only agents
#   scripts/sync_claude.sh --skills     # sync only skills
#   scripts/sync_claude.sh --claude-md  # sync only CLAUDE.md
#   scripts/sync_claude.sh --agents --skills  # sync multiple
#

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE_DIR="${SCRIPT_DIR}/.claude"
GLOBAL_DIR="${HOME}/.claude"

sync_agents() {
  echo "Syncing agents..."
  mkdir -p "${GLOBAL_DIR}/agents"
  for f in "${CLAUDE_DIR}"/agents/*.md; do
    [ -f "$f" ] || continue
    name=$(basename "$f")
    cp "$f" "${GLOBAL_DIR}/agents/${name}"
  done
  echo "  -> ${GLOBAL_DIR}/agents/"
}

sync_skills() {
  echo "Syncing skills..."
  mkdir -p "${GLOBAL_DIR}/skills"
  for d in "${CLAUDE_DIR}"/skills/*; do
    [ -d "$d" ] || continue
    name=$(basename "$d")
    cp -r "${CLAUDE_DIR}/skills/${name}" "${GLOBAL_DIR}/skills/"
    echo "  -> ${GLOBAL_DIR}/skills/${name}/"
  done
}

sync_claude_md() {
  echo "Syncing CLAUDE.md..."
  if [ -f "${CLAUDE_DIR}/CLAUDE.md" ]; then
    cp "${CLAUDE_DIR}/CLAUDE.md" "${GLOBAL_DIR}/CLAUDE.md"
    echo "  -> ${GLOBAL_DIR}/CLAUDE.md"
  else
    echo "  (no CLAUDE.md found, skipping)"
  fi
}

# Parse args; if none, sync all
DO_ALL=false
DO_AGENTS=false
DO_SKILLS=false
DO_CLAUDE_MD=false

for arg in "$@"; do
  case "$arg" in
    --all)        DO_ALL=true ;;
    --agents)     DO_AGENTS=true ;;
    --skills)     DO_SKILLS=true ;;
    --claude-md)  DO_CLAUDE_MD=true ;;
    -h|--help)
      echo "Usage: $0 [--all] [--agents] [--skills] [--claude-md]"
      echo "  --all        sync all (default when no args)"
      echo "  --agents     sync only agents"
      echo "  --skills     sync only skills"
      echo "  --claude-md  sync only CLAUDE.md"
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
  DO_CLAUDE_MD=true
fi

[ "$DO_AGENTS" = true ] && sync_agents
[ "$DO_SKILLS" = true ] && sync_skills
[ "$DO_CLAUDE_MD" = true ] && sync_claude_md

echo "Done."
