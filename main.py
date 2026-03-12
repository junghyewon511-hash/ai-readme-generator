#!/usr/bin/env python3
"""
AI README Generator
-------------------
A CLI tool that generates beautiful README files for your projects.
"""

import argparse
import sys
from datetime import datetime


# ── Colour helpers (no external deps) ────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"


def color(text: str, code: str) -> str:
    """Wrap *text* in an ANSI colour code (skipped on non-TTY)."""
    if sys.stdout.isatty():
        return f"{code}{text}{RESET}"
    return text


# ── README template ───────────────────────────────────────────────────────────

def generate_readme(
    project_name: str,
    description: str,
    author: str = "Your Name",
    github_user: str = "yourusername",
    license_name: str = "MIT",
    python_version: str = "3.8+",
) -> str:
    """Return a fully-formatted README.md string."""

    year = datetime.now().year
    slug = project_name.lower().replace(" ", "-")

    readme = f"""\
# {project_name}

> {description}

[![Python Version](https://img.shields.io/badge/python-{python_version}-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-{license_name}-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## About

{description}

This project was created to make developers' lives easier by automating
repetitive documentation tasks so you can focus on writing great code.

---

## ✨ Features

- ✅ **Easy to use** – minimal setup, runs from the command line
- ✅ **Customisable** – tweak templates to match your style
- ✅ **No heavy dependencies** – works with the Python standard library
- ✅ **Cross-platform** – macOS, Linux, and Windows

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/{github_user}/{slug}.git
cd {slug}

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage

```
python main.py --name "My Project" --description "A short description"
```

### All options

| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--name` | `-n` | Project name | *required* |
| `--description` | `-d` | One-line project description | *required* |
| `--author` | `-a` | Author name | `Your Name` |
| `--github` | `-g` | GitHub username | `yourusername` |
| `--license` | `-l` | License identifier | `MIT` |
| `--python` | `-p` | Minimum Python version | `3.8+` |
| `--output` | `-o` | Write output to a file | *(stdout)* |

---

## 📖 Examples

**Basic usage**

```bash
python main.py -n "Weather CLI" -d "Fetch live weather from the terminal"
```

**Save to file**

```bash
python main.py \\
  --name "Weather CLI" \\
  --description "Fetch live weather from the terminal" \\
  --author "Jane Doe" \\
  --github "janedoe" \\
  --output README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for
guidelines on how to get started.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

Copyright © {year} {author}.  
Distributed under the [{license_name} License](LICENSE).
"""
    return readme


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="readme-gen",
        description="Generate a beautiful README.md for your project.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python main.py -n 'My App' -d 'Does something cool'\n"
            "  python main.py -n 'My App' -d 'Does something cool' -o README.md\n"
        ),
    )

    parser.add_argument("-n", "--name",        required=True,  help="Project name")
    parser.add_argument("-d", "--description", required=True,  help="Short project description")
    parser.add_argument("-a", "--author",      default="Your Name",    help="Author name")
    parser.add_argument("-g", "--github",      default="yourusername", help="GitHub username")
    parser.add_argument("-l", "--license",     default="MIT",          help="License identifier")
    parser.add_argument("-p", "--python",      default="3.8+",         help="Min Python version")
    parser.add_argument("-o", "--output",      default=None,           help="Output file path")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print(color("\n🤖  AI README Generator", BOLD + CYAN))
    print(color("─" * 40, CYAN))
    print(color(f"  Project : ", YELLOW) + args.name)
    print(color(f"  Author  : ", YELLOW) + args.author)
    print(color("─" * 40, CYAN))

    readme = generate_readme(
        project_name=args.name,
        description=args.description,
        author=args.author,
        github_user=args.github,
        license_name=args.license,
        python_version=args.python,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(readme)
        print(color(f"\n✅  README written to '{args.output}'\n", GREEN))
    else:
        print(color("\n📄  Generated README\n", GREEN))
        print("─" * 60)
        print(readme)
        print("─" * 60)
        print(color("\nTip: add  -o README.md  to save directly to a file.\n", YELLOW))


if __name__ == "__main__":
    main()
