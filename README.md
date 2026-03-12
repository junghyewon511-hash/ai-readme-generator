# 🤖 AI README Generator

> Generate beautiful, professional README files for your projects — in seconds, from the command line.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## About

Writing a great README takes time — time you'd rather spend writing code.  
**AI README Generator** is a lightweight Python CLI tool that scaffolds a
polished, structured `README.md` from just a project name and description.
No internet connection required, no API keys, no fuss.

Whether you're publishing your first open-source project or prototyping a
new idea, this tool gives you a professional starting point in under five
seconds.

---

## ✨ Features

- 📝 **One command** – supply a name and description, get a full README
- 🎨 **Professional template** – badges, ToC, installation steps, usage table, contributing guide
- 💾 **File output** – write directly to `README.md` with `--output`
- 🎨 **Colourful terminal output** – clear, readable feedback (gracefully degrades on non-TTY)
- 📦 **Zero heavy dependencies** – runs on the Python standard library alone
- 🔧 **Easy to extend** – plug in an AI backend (OpenAI, Anthropic …) in minutes

---

## 🗂 Project Structure

```
ai-readme-generator/
├── main.py              # CLI entry point & README template engine
├── requirements.txt     # Dependencies (minimal by design)
├── LICENSE              # MIT licence
├── CONTRIBUTING.md      # Contributor guide
├── README.md            # This file
└── examples/
    ├── example_input.txt    # Sample inputs you can copy-paste
    └── example_output.md    # README generated from the example inputs
```

---

## 🚀 Installation

**Requirements:** Python 3.8 or newer.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ai-readme-generator.git
cd ai-readme-generator

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

> **No pip install needed for basic usage** — `main.py` works with the
> standard library out of the box.

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
| `--author` | `-a` | Author / organisation name | `Your Name` |
| `--github` | `-g` | GitHub username | `yourusername` |
| `--license` | `-l` | Licence identifier (e.g. `MIT`) | `MIT` |
| `--python` | `-p` | Minimum Python version | `3.8+` |
| `--output` | `-o` | Write output to this file path | *(stdout)* |

---

## 📖 Example

### Command

```bash
python main.py \
  --name        "Weather CLI" \
  --description "Fetch live weather forecasts right from your terminal." \
  --author      "Jane Doe" \
  --github      "janedoe" \
  --output      README.md
```

### Terminal output

```
🤖  AI README Generator
────────────────────────────────────────
  Project : Weather CLI
  Author  : Jane Doe
────────────────────────────────────────

✅  README written to 'README.md'
```

The generated file is saved to `README.md` — see
[`examples/example_output.md`](examples/example_output.md) for the full result.

---

## 🤝 Contributing

Contributions are very welcome!  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

Quick start:

```bash
git checkout -b feature/my-feature
# … make changes …
git commit -m "feat: describe your change"
git push origin feature/my-feature
# open a Pull Request on GitHub
```

---

## 📄 License

Copyright © 2025 AI README Generator Contributors.  
Distributed under the [MIT License](LICENSE).
