# HTML to PPTX Converter

Convert HTML files (with CSS, JavaScript, and design) into PowerPoint presentations.

## Features

- ✅ Full HTML/CSS/JS rendering
- ✅ Captures complete page design
- ✅ Auto-splits long pages into multiple slides
- ✅ Interactive CLI with 3 easy options
- ✅ Batch conversion support
- ✅ Customizable slide dimensions

## Installation

```bash
# Clone the repository
git clone https://github.com/swapnil-22-secure/html-to-pptx-converter.git
cd html-to-pptx-converter

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 🎯 Interactive Mode (Recommended)

Simply run the interactive converter:

```bash
python converter.py
```

You'll get 3 options:

**[1] Insert HTML code directly**
- Paste your HTML code directly into the terminal
- Perfect for quick conversions or code snippets
- Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) when done

**[2] Upload a .html file**
- Provide the path to your HTML file
- Supports drag-and-drop paths
- Auto-suggests output filename

**[3] Run example**
- Test the converter with the included example.html
- See how it works before using your own files
- Generates example_output.pptx

### 📝 Command Line Mode

#### Single File Conversion

```bash
# Convert HTML to PPTX (auto-named output)
python html_to_pptx.py input.html

# Convert with custom output name
python html_to_pptx.py input.html output.pptx
```

#### Batch Conversion

```bash
# Convert all HTML files in a directory
python batch_convert.py ./html_files

# Convert with custom output directory
python batch_convert.py ./html_files ./output_pptx
```

## Quick Start Example

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run interactive mode
python converter.py

# 3. Choose option [3] to run the example
# 4. Open example_output.pptx to see the result!
```

## How It Works

1. **Renders HTML**: Uses Selenium with headless Chrome to fully render HTML, CSS, and JavaScript
2. **Captures Screenshot**: Takes a full-page screenshot of the rendered content
3. **Splits into Slides**: Automatically divides long pages into multiple slides (1080px height each)
4. **Creates PPTX**: Generates a PowerPoint presentation with 16:9 aspect ratio

## Requirements

- Python 3.7+
- Chrome/Chromium browser (automatically managed by webdriver-manager)

## Programmatic Usage

```python
from html_to_pptx import HTMLtoPPTXConverter

converter = HTMLtoPPTXConverter(width=1920, height=1080)
converter.convert('my_page.html', 'presentation.pptx')
converter.cleanup()
```

## Customization

You can customize the converter by adjusting parameters:

```python
# Custom dimensions
converter = HTMLtoPPTXConverter(width=1280, height=720)

# Custom wait time for JS loading
converter.capture_html('file.html', wait_time=5)
```

## Files Overview

- `converter.py` - Interactive CLI interface (recommended)
- `html_to_pptx.py` - Core conversion library
- `batch_convert.py` - Batch processing script
- `example.html` - Demo HTML file
- `requirements.txt` - Python dependencies

## Troubleshooting

**Chrome driver issues?**
- The tool auto-downloads the correct Chrome driver
- Make sure Chrome/Chromium is installed on your system

**Import errors?**
- Run `pip install -r requirements.txt` again
- Make sure you're in the project directory

**Conversion fails?**
- Check if your HTML file exists
- Ensure the HTML is valid
- Try increasing wait_time for complex JavaScript

## License

MIT License

## Author

Created by Swapnil via Bhindi

---

⭐ Star this repo if you find it useful!
