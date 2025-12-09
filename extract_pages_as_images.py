#!/usr/bin/env python3
"""
Script to convert PDF pages to images - useful for extracting full-page screenshots
from the PATHFINDER User Manual PDF.
"""

import os
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    print("Error: PyMuPDF not installed. Please run: pip install PyMuPDF")
    sys.exit(1)

def convert_pages_to_images(pdf_path, output_dir, dpi=200):
    """Convert each PDF page to an image"""
    doc = fitz.open(pdf_path)
    
    print(f"Converting {len(doc)} pages to images...")
    print(f"DPI: {dpi} (higher = better quality but larger files)\n")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Convert page to image (pixmap)
        mat = fitz.Matrix(dpi/72, dpi/72)  # 72 is default DPI
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        image_filename = f"page-{page_num+1:02d}.png"
        image_path = os.path.join(output_dir, image_filename)
        pix.save(image_path)
        
        print(f"  Converted page {page_num+1:02d} -> {image_filename}")
    
    page_count = len(doc)
    doc.close()
    print(f"\nSuccessfully converted {page_count} page(s) to images")
    return page_count

def main():
    # Paths
    script_dir = Path(__file__).parent
    pdf_path = script_dir / "public" / "documents" / "PATHFINDER - User Manual.pdf"
    output_dir = script_dir / "public" / "images" / "screenshots"
    
    # Check if PDF exists
    if not pdf_path.exists():
        print(f"Error: PDF not found at {pdf_path}")
        sys.exit(1)
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Converting PDF pages to images...")
    print(f"PDF: {pdf_path}")
    print(f"Output: {output_dir}\n")
    
    # Convert pages to images
    try:
        count = convert_pages_to_images(str(pdf_path), str(output_dir), dpi=200)
        print(f"\nDone! {count} page images created.")
        print("\nNext steps:")
        print("1. Review the page-XX.png files")
        print("2. Identify which pages contain the screenshots you want")
        print("3. Rename the relevant pages to step-XX-description.png")
        print("4. Update the screenshotSteps array in Features.vue")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

