#!/usr/bin/env python3
"""
Entry point for /stitch-react-native slash command.
Loads the stitch-react-native skill and outputs its guidance for the agent.
"""
import sys
from pathlib import Path

def main():
    skill_dir = Path(__file__).parent.parent
    skill_md = skill_dir / "SKILL.md"
    
    if not skill_md.exists():
        print("SKILL.md not found")
        sys.exit(1)
    
    content = skill_md.read_text(encoding="utf-8")
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    
    print(content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("\n--- User Arguments: " + " ".join(sys.argv[1:]) + " ---\n")
    main()
