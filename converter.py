#!/usr/bin/env python3
"""
Interactive HTML to PPTX Converter
Main entry point with user-friendly menu interface
"""

import os
import sys
import tempfile
from html_to_pptx import HTMLtoPPTXConverter

def print_banner():
    """Print welcome banner"""
    print("\n" + "="*60)
    print("🚀 HTML to PPTX Converter")
    print("="*60 + "\n")

def print_menu():
    """Display main menu options"""
    print("\nChoose an option:")
    print("  [1] Insert HTML code directly")
    print("  [2] Upload a .html file")
    print("  [3] Run example")
    print("  [4] Exit")
    print()

def option_insert_code():
    """Option 1: Insert HTML code directly"""
    print("\n📝 Insert your HTML code")
    print("Tip: Paste your HTML and press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) when done\n")
    
    try:
        lines = []
        print("Paste your HTML code below:")
        print("-" * 40)
        
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        
        html_content = '\n'.join(lines)
        
        if not html_content.strip():
            print("❌ No HTML content provided!")
            return
        
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(html_content)
            temp_html_path = temp_file.name
        
        # Get output filename
        output_name = input("\n📁 Enter output filename (without .pptx extension): ").strip()
        if not output_name:
            output_name = "output"
        
        output_path = f"{output_name}.pptx"
        
        # Convert
        print(f"\n🔄 Converting to {output_path}...")
        converter = HTMLtoPPTXConverter()
        try:
            converter.convert(temp_html_path, output_path)
            print(f"\n✅ Success! PPTX saved as: {output_path}")
        finally:
            converter.cleanup()
            # Clean up temp file
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)
    
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

def option_upload_file():
    """Option 2: Upload/specify a .html file"""
    print("\n📂 Upload HTML File")
    
    file_path = input("Enter the path to your HTML file: ").strip()
    
    # Remove quotes if user wrapped path in quotes
    file_path = file_path.strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found!")
        return
    
    if not file_path.lower().endswith('.html'):
        print("⚠️  Warning: File doesn't have .html extension. Continue anyway? (y/n): ", end='')
        if input().lower() != 'y':
            return
    
    # Get output filename
    default_output = os.path.splitext(os.path.basename(file_path))[0] + ".pptx"
    output_name = input(f"\n📁 Enter output filename (default: {default_output}): ").strip()
    
    if not output_name:
        output_path = default_output
    else:
        output_path = output_name if output_name.endswith('.pptx') else f"{output_name}.pptx"
    
    # Convert
    print(f"\n🔄 Converting {file_path} to {output_path}...")
    converter = HTMLtoPPTXConverter()
    try:
        converter.convert(file_path, output_path)
        print(f"\n✅ Success! PPTX saved as: {output_path}")
    except Exception as e:
        print(f"\n❌ Error during conversion: {str(e)}")
    finally:
        converter.cleanup()

def option_run_example():
    """Option 3: Run example conversion"""
    print("\n🎨 Running Example Conversion")
    
    example_file = "example.html"
    
    if not os.path.exists(example_file):
        print(f"❌ Error: Example file '{example_file}' not found!")
        print("Make sure you're running this from the project directory.")
        return
    
    output_path = "example_output.pptx"
    
    print(f"Converting {example_file} to {output_path}...")
    converter = HTMLtoPPTXConverter()
    try:
        converter.convert(example_file, output_path)
        print(f"\n✅ Success! Example PPTX saved as: {output_path}")
        print(f"📊 Open '{output_path}' to see the result!")
    except Exception as e:
        print(f"\n❌ Error during conversion: {str(e)}")
    finally:
        converter.cleanup()

def main():
    """Main interactive loop"""
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                option_insert_code()
            elif choice == '2':
                option_upload_file()
            elif choice == '3':
                option_run_example()
            elif choice == '4':
                print("\n👋 Goodbye!")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
        
        # Ask if user wants to continue
        print("\n" + "-"*60)
        continue_choice = input("Press Enter to continue or 'q' to quit: ").strip().lower()
        if continue_choice == 'q':
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
