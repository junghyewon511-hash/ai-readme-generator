# Weather CLI

> Fetch live weather forecasts right from your terminal.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
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

Fetch live weather forecasts right from your terminal.

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
git clone https://github.com/janedoe/weather-cli.git
cd weather-cli

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

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
python main.py \
  --name "Weather CLI" \
  --description "Fetch live weather from the terminal" \
  --author "Jane Doe" \
  --github "janedoe" \
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

Copyright © 2026 Jane Doe.  
Distributed under the [MIT License](LICENSE).
