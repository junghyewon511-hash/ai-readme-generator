# Contributing to AI README Generator

First off — thank you for taking the time to contribute! 🎉  
All contributions, big or small, are genuinely appreciated.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Submitting a Pull Request](#submitting-a-pull-request)

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/).
By participating you agree to uphold a welcoming, respectful environment for everyone.

---

## How Can I Contribute?

### 🐛 Reporting Bugs

1. Search [existing issues](../../issues) first.
2. Open a new issue and fill in the **bug report** template.
3. Include steps to reproduce, expected vs. actual behaviour, and your Python version.

### 💡 Suggesting Features

1. Check the [open issues](../../issues) and [discussions](../../discussions).
2. Open a **feature request** issue describing the problem it solves and a rough idea of the solution.

### 📝 Improving Docs

Documentation lives in `README.md`, `CONTRIBUTING.md`, and inline docstrings.
Feel free to open a PR for typos, clarifications, or additional examples.

### 🔧 Submitting Code

See [Development Setup](#development-setup) and [Submitting a Pull Request](#submitting-a-pull-request) below.

---

## Development Setup

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/ai-readme-generator.git
cd ai-readme-generator

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dev dependencies
pip install -r requirements.txt

# 4. Verify everything works
python main.py --name "Test" --description "A quick smoke test"
```

---

## Coding Standards

| Tool | Purpose | Run with |
|------|---------|----------|
| `ruff` | Linting + formatting | `ruff check . && ruff format .` |
| `pytest` | Unit tests | `pytest` |

- Follow [PEP 8](https://pep8.org/) style.
- Add docstrings to all public functions.
- Keep functions small and focused on a single responsibility.
- New features should come with at least one test.

---

## Submitting a Pull Request

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** and commit with a clear message:
   ```bash
   git commit -m "feat: add --template flag for custom templates"
   ```
3. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Open a **Pull Request** against `main`.  
   Fill in the PR template — describe *what* changed and *why*.

### Commit message style (loosely follows Conventional Commits)

| Prefix | When to use |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `test:` | Adding or fixing tests |
| `chore:` | Maintenance / tooling |

---

## Questions?

Open a [Discussion](../../discussions) — we're happy to help. 🙌
