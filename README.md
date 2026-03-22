# 📂 Automated Downloads Organizer

A robust Python-based automation tool designed to manage and clean up your 'Downloads' folder. This script identifies files by their extensions and moves them into categorized directories, ensuring a clutter-free workspace. It is designed in Portuguese, but it can be easily adjusted to any language. 

## ✨ Features
- **Smart Categorization:** Automatically maps common file types (Images, Documents, Videos, etc.) to specific folders.
- **Recursive Cleanup:** Capable of scanning both the root directory and generic subfolders (like "Outros").
- **Safety First:** Includes a `SAFE_FOLDERS` list to prevent the script from moving its own organizational structure.
- **Error Resilience:** Robust exception handling for `PermissionError` (e.g., when a file is currently open) and other unexpected system events.
- **Unit Tested:** Built with a Test-Driven mindset to ensure category mapping is always accurate.

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pathlib:** For modern, cross-platform file system paths.
- **Pytest:** For automated unit testing.

## 🧪 Testing
The project includes a comprehensive test suite to verify the file classification logic.  
To run the tests, ensure your virtual environment is active and run:

````markdown
```bash
pytest
```

## 🚀 Getting Started

### 1. Installation
Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/organizador-downloads.git
cd organizador-downloads
```

### 2. Setup Environment
Create and activate a virtual environment:

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate
```

### 3. Usage
Run the main script:

```bash
python project.py
```
````

*Developed as a personal automation project to improve workflow efficiency.*
