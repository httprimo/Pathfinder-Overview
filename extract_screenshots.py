#!/usr/bin/env python3
"""
Script to extract screenshots/images from the PATHFINDER User Manual PDF
and save them to the screenshots directory.
"""

import os
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    from pdf2image import convert_from_path
    HAS_PDF2IMAGE = True
except ImportError:
    HAS_PDF2IMAGE = False

def extract_with_pymupdf(pdf_path, output_dir):
    """Extract images using PyMuPDF (fitz)"""
    doc = fitz.open(pdf_path)
    image_count = 0
    
    print(f"Processing PDF with {len(doc)} pages...")
    
    for page_num, page in enumerate(doc, start=1):
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Save image
            image_filename = f"step-{page_num:02d}-page-{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            
            image_count += 1
            print(f"  Extracted: {image_filename} (Page {page_num})")
    
    doc.close()
    return image_count

def extract_with_pdf2image(pdf_path, output_dir):
    """Extract pages as images using pdf2image"""
    print("Converting PDF pages to images...")
    images = convert_from_path(pdf_path, dpi=300)
    
    for page_num, image in enumerate(images, start=1):
        image_filename = f"step-{page_num:02d}-page.png"
        image_path = os.path.join(output_dir, image_filename)
        image.save(image_path, "PNG")
        print(f"  Extracted: {image_filename} (Page {page_num})")
    
    return len(images)

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
    
    print(f"Extracting images from: {pdf_path}")
    print(f"Output directory: {output_dir}\n")
    
    # Try PyMuPDF first (better for extracting embedded images)
    if HAS_PYMUPDF:
        print("Using PyMuPDF (fitz) to extract images...")
        try:
            count = extract_with_pymupdf(str(pdf_path), str(output_dir))
            print(f"\nSuccessfully extracted {count} image(s)")
            return
        except Exception as e:
            print(f"Error with PyMuPDF: {e}")
            print("Trying alternative method...\n")
    
    # Try pdf2image as fallback (converts pages to images)
    if HAS_PDF2IMAGE:
        print("Using pdf2image to convert pages to images...")
        try:
            count = extract_with_pdf2image(str(pdf_path), str(output_dir))
            print(f"\nSuccessfully extracted {count} page(s) as images")
            return
        except Exception as e:
            print(f"Error with pdf2image: {e}")
    
    # If both methods fail, provide instructions
    print("\n" + "="*60)
    print("ERROR: Required libraries not installed")
    print("="*60)
    print("\nPlease install one of the following:")
    print("\nOption 1 (Recommended - extracts embedded images):")
    print("  pip install PyMuPDF")
    print("\nOption 2 (Converts pages to images):")
    print("  pip install pdf2image")
    print("  (Also requires poppler: https://github.com/oschwartz10612/poppler-windows/releases)")
    print("\nAfter installation, run this script again.")
    sys.exit(1)

if __name__ == "__main__":
    main()

