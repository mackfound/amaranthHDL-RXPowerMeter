# Python Virtual Environments

This README briefly details how to set up a Python virtual environment and why it is a necessary step in Python development.

## What is a Virtual Environment and Why Use It?

A virtual environment is an isolated directory tree containing a specific Python version and its associated packages. You should use them for a few key reasons:

* **Dependency Isolation:** Project A might need a specific library version (e.g., Django 3.2), while Project B needs a newer one (e.g., Django 4.0). Virtual environments prevent these conflicts.
* **System Cleanliness:** They keep your global Python installation clean and free of project-specific clutter.
* **Reproducibility:** You can easily generate a `requirements.txt` file so other developers can exactly replicate your project's environment.

---

## Setup Instructions

Python includes a built-in module called `venv` to handle this.

### 1. Create the Environment
Navigate to your project directory in your terminal and run:

```bash
python -m venv venv
```
> Note: The second `venv` is the name of the folder being created. You can name it `.venv` or something else, but `venv` is the standard convention.

### 2. Activate the Environment
You must activate the environment before installing packages so your terminal knows to use this specific isolated folder. The command depends on your operating system.

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS and Linux:**
```bash
source venv/bin/activate
```

### 3. Install Packages
Once activated, your terminal prompt will usually change to show `(venv)` at the beginning of the line. You can now safely install packages just for this project:

```bash
pip install requests
```

### 4. Deactivate
When you are finished working on the project, you can return to your system's global Python environment by simply running:

```bash
deactivate
```
```