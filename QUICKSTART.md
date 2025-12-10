# Quick Start Guide

Get started with HTML to PPTX Converter in 3 simple steps!

## Step 1: Install

```bash
git clone https://github.com/swapnil-22-secure/html-to-pptx-converter.git
cd html-to-pptx-converter
pip install -r requirements.txt
```

## Step 2: Run

```bash
python converter.py
```

## Step 3: Choose Your Option

```
🚀 HTML to PPTX Converter
============================================================

Choose an option:
  [1] Insert HTML code directly
  [2] Upload a .html file
  [3] Run example
  [4] Exit
```

### Option 1: Insert HTML Code

Perfect for quick conversions or testing code snippets.

```
Enter your choice (1-4): 1

📝 Insert your HTML code
Paste your HTML and press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows)

Paste your HTML code below:
----------------------------------------
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background: linear-gradient(135deg, #667eea, #764ba2); }
        h1 { color: white; text-align: center; }
    </style>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
[Press Ctrl+D or Ctrl+Z]

📁 Enter output filename (without .pptx extension): my_presentation

🔄 Converting to my_presentation.pptx...
✅ Success! PPTX saved as: my_presentation.pptx
```

### Option 2: Upload HTML File

Use existing HTML files from your computer.

```
Enter your choice (1-4): 2

📂 Upload HTML File
Enter the path to your HTML file: /path/to/your/file.html

📁 Enter output filename (default: file.pptx): 

🔄 Converting /path/to/your/file.html to file.pptx...
✅ Success! PPTX saved as: file.pptx
```

**Tips:**
- You can drag and drop the file to get its path
- Leave output filename empty to use default
- Supports relative and absolute paths

### Option 3: Run Example

Test the converter with the included demo.

```
Enter your choice (1-4): 3

🎨 Running Example Conversion
Converting example.html to example_output.pptx...

✅ Success! Example PPTX saved as: example_output.pptx
📊 Open 'example_output.pptx' to see the result!
```

## What Gets Converted?

✅ **HTML Structure** - All tags and content  
✅ **CSS Styling** - Colors, fonts, layouts, gradients  
✅ **JavaScript** - Dynamic content and animations  
✅ **Images** - Embedded and linked images  
✅ **Responsive Design** - Captured at specified resolution  

## Output Format

- **Aspect Ratio**: 16:9 (widescreen)
- **Resolution**: 1920x1080 per slide
- **Format**: Microsoft PowerPoint (.pptx)
- **Slides**: Auto-split for long pages

## Common Use Cases

### 1. Web Design Mockups
Convert your HTML prototypes to presentations for client reviews.

### 2. Documentation
Turn HTML documentation into shareable PowerPoint slides.

### 3. Reports
Convert HTML reports with charts and graphs to PPTX.

### 4. Landing Pages
Showcase your landing page designs in presentation format.

### 5. Email Templates
Convert HTML email templates to slides for team review.

## Next Steps

- Try converting your own HTML files
- Explore batch conversion with `batch_convert.py`
- Customize dimensions in the code
- Check out the full README for advanced usage

## Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review [example.html](example.html) for HTML structure examples
- Open an issue on GitHub for bugs or questions

---

Happy Converting! 🚀
