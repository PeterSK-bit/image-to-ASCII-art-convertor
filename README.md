# Image to ASCII Art Converter

This simple Python script converts an image into ASCII art using grayscale brightness and maps it to a set of characters.

Supports both **CLI arguments** and **interactive prompts**, so you can run it however you prefer.

---

## Features

- Converts color images to ASCII based on brightness
- Automatically sanitizes and validates filenames
- Preserves aspect ratio with spacing
- Supports **CLI arguments** (non-interactive) and **input() fallback** (interactive)
- Easy to run — just provide an image path and output name

---

## Requirements

- Python 3.10 or higher
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)

### Install dependencies:

```bash
pip install Pillow
```

OR

```
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Option 1: Interactive prompts
```bash
\image-to-ASCII-art-convertor> python main.py
path to image: cat.jpg
new file name: cat ascii 😼
INFO: Sanitized filename: cat-ascii
```

### Option 2: CLI arguments
```bash
\image-to-ASCII-art-convertor> python main.py path/to/image.png --output ascii-art-name
INFO: Sanitized filename: ascii-art-name
```

## Included Examples

This repository includes sample input and output to help you get started:

- **example-input.png** – A test image you can use immediately.
- **example-output.txt** – The ASCII art result generated from the example image.

---

## License
This project is open-source and free to use under the MIT License.