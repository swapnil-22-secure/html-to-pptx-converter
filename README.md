# HTML to PPTX Converter

Convert HTML files (with CSS, JavaScript, and design) into PowerPoint presentations.

## Features

- ✅ Full HTML/CSS/JS rendering
- ✅ Captures complete page design
- ✅ Auto-splits long pages into multiple slides
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

### Single File Conversion

```bash
# Convert HTML to PPTX (auto-named output)
python html_to_pptx.py input.html

# Convert with custom output name
python html_to_pptx.py input.html output.pptx
```

### Batch Conversion

```bash
# Convert all HTML files in a directory
python batch_convert.py ./html_files

# Convert with custom output directory
python batch_convert.py ./html_files ./output_pptx
```

## How It Works

1. **Renders HTML**: Uses Selenium with headless Chrome to fully render HTML, CSS, and JavaScript
2. **Captures Screenshot**: Takes a full-page screenshot of the rendered content
3. **Splits into Slides**: Automatically divides long pages into multiple slides (1080px height each)
4. **Creates PPTX**: Generates a PowerPoint presentation with 16:9 aspect ratio

## Requirements

- Python 3.7+
- Chrome/Chromium browser (automatically managed by webdriver-manager)

## Example

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

## License

MIT License

## Author

Created by Swapnil via Bhindi
