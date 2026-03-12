# My Projects

This is a Python project for Machine Learning.

## Environment Setup

### What is uv?
An extremely fast Python package and project manager, written in Rust.

### Prerequisites
- Python 3.14 or higher
- uv (install using the command below)

### Install uv

**On macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /my_projects
   ```
   checkout to branch: 

   git checkout python-tutorial

2. **Create a virtual environment:**
   ```bash
   uv venv --python 3.14
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   uv sync
   ```

## Adding Dependencies

To add new dependencies to the project using uv:

1. **Add a dependency:**
   ```bash
   uv add requests pandas
   ```
   This command will:
   - Add the packages to `pyproject.toml`
   - Update the lock file
   - Install the packages in the virtual environment

2. **Alternative: Edit `pyproject.toml` manually:**
   Open `pyproject.toml` and add dependencies to the `dependencies` list.

   Example:
   ```toml
   dependencies = [
       "requests>=2.25.0",
       "pandas>=1.3.0"
   ]
   ```

   Then sync the environment:
   ```bash
   uv sync
   ```

