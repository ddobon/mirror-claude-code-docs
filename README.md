# 🤖 Claude Code Docs Mirror

[![Daily Sync](https://github.com/ddobon/mirror-claude-code-docs/actions/workflows/daily-sync.yml/badge.svg)](https://github.com/ddobon/mirror-claude-code-docs/actions/workflows/daily-sync.yml)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated mirroring system that maintains a synchronized copy of the official [Claude Code Documentation](https://code.claude.com/docs/llms.txt).

## 🌟 Overview

The Claude Code documentation is an ever-evolving resource. This repository serves as an automated daily snapshot, keeping all Markdown documentation fully accessible for offline reading, quick local searches, and version history tracking.

### Key Features
- 🔄 **Automated Daily Sync**: A GitHub Action workflow runs automatically every day at 08:00 AM (JST/KST) (23:00 UTC).
- 📥 **Zero-Dependency Script**: The `sync.py` script is built purely with Python's Standard Library making it universally executable.
- 📁 **Clean Organization**: All documentation files are cleanly downloaded and stored directly in the `docs/` directory.
- 🛡️ **Diff-Aware Commits**: The GitHub Action intelligently checks for Git diffs and only pushes a commit if the upstream documentation is genuinely modified.

---

## 🚀 How It Works

The core synchronization script (`sync.py`) operates in three simple steps:
1. **Fetch**: Retrieves the primary index file from `https://code.claude.com/docs/llms.txt`.
2. **Parse**: Uses Regex to extract all individual Markdown document URLs listed in the index.
3. **Save**: Downloads each individual `.md` file and overwrites the local copy inside the `/docs` folder.

*(Note: The script includes a safe SSL bypass specifically to handle local execution on macOS environments where certificate chains might be unverified).*

---

## 💻 Local Usage

Want to run the synchronization manually on your own machine? 

### Prerequisites
- Python 3.10 or higher installed.
- No `pip install` required! (No third-party packages used).

### Execution
Simply run the sync script from the root directory of the project:

```bash
python sync.py
```

The script will output its progress directly to your terminal:
```text
Fetching https://code.claude.com/docs/llms.txt...
Found 57 documentation links.
Created directory: docs
Downloading agent-teams.md...
Downloading amazon-bedrock.md...
...
```

---

## ⚙️ CI/CD automation

This repository utilizes GitHub Actions to stay up-to-date automatically.

The workflow is defined in `.github/workflows/daily-sync.yml` and is configured to:
- Checkout the repository.
- Setup a Python 3.10 environment.
- Execute `python sync.py`.
- Configure the `GitHub Action Bot` git user.
- Add the `docs/` directory, verify if changes are present, and commit/push if necessary.

You can also trigger it manually at any time using the `workflow_dispatch` trigger from the Actions tab in GitHub!