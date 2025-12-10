#!/usr/bin/env python3
"""Batch convert multiple HTML files"""

import os
import glob
from html_to_pptx import HTMLtoPPTXConverter

def batch_convert(input_dir, output_dir=None):
    if not output_dir:
        output_dir = input_dir
    
    os.makedirs(output_dir, exist_ok=True)
    
    html_files = glob.glob(os.path.join(input_dir, "*.html"))
    
    if not html_files:
        print(f"No HTML files found in {input_dir}")
        return
    
    converter = HTMLtoPPTXConverter()
    
    try:
        for html_file in html_files:
            basename = os.path.basename(html_file)
            output_file = os.path.join(output_dir, basename.replace('.html', '.pptx'))
            
            print(f"\n{'='*50}")
            converter.convert(html_file, output_file)
            
    finally:
        converter.cleanup()
    
    print(f"\n✅ Converted {len(html_files)} files")

if __name__ == "__main__":
    import sys
    input_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    batch_convert(input_dir, output_dir)
