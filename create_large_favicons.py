#!/usr/bin/env python3
"""
Script to create large, prominent favicons that fill the space like YouTube's favicon.
Optimizes the logo to appear bigger in browser tabs.
"""

import os
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL (Pillow) is not installed. Install it with: pip install Pillow")

def create_large_favicon(input_path, output_dir, size=32, padding_ratio=0.85):
    """
    Create a favicon where the logo fills most of the space (like YouTube).
    
    Args:
        input_path: Path to input image (transparent PNG)
        output_dir: Directory to save favicon files
        size: Favicon size to create
        padding_ratio: How much of the space the logo should fill (0.85 = 85% of space)
    """
    if not HAS_PIL:
        print("Error: PIL (Pillow) is required. Install with: pip install Pillow")
        return False
    
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Ensure it's RGBA
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Calculate the size the logo should be (fill most of the space)
        logo_size = int(size * padding_ratio)
        
        # Resize the logo to fill most of the favicon space
        resized = img.copy()
        resized.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Create a new image with the exact size and transparent background
        favicon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        
        # Calculate position to center the logo
        x_offset = (size - resized.width) // 2
        y_offset = (size - resized.height) // 2
        
        # Paste the resized logo onto the centered transparent background
        favicon.paste(resized, (x_offset, y_offset), resized)
        
        return favicon
        
    except Exception as e:
        print(f"Error processing image: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    # Get project root directory
    project_root = Path(__file__).parent
    logo_dir = project_root / 'public' / 'images' / 'logo'
    input_file = logo_dir / 'Pathfinder_Logo_Transparent.png'
    output_dir = logo_dir / 'favicons'
    
    if not input_file.exists():
        print(f"Error: Transparent logo file not found at {input_file}")
        return
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Creating large, prominent favicons from: {input_file}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Create favicons at key sizes with logo filling 90% of space (like YouTube)
    sizes = [16, 32, 48, 64, 96, 128, 192, 256, 512]
    created_files = []
    
    for size in sizes:
        # Use 90% fill ratio for larger appearance (YouTube style)
        padding_ratio = 0.90 if size >= 32 else 0.85
        
        favicon = create_large_favicon(input_file, output_dir, size, padding_ratio)
        
        if favicon:
            output_file = output_dir / f'favicon-{size}x{size}.png'
            favicon.save(output_file, 'PNG', optimize=True)
            created_files.append(output_file)
            print(f"Created: {output_file} ({size}x{size}, logo fills {int(padding_ratio*100)}%)")
    
    # Create ICO file with multiple sizes (16, 32, 48)
    ico_sizes = [16, 32, 48]
    ico_images = []
    for size in ico_sizes:
        padding_ratio = 0.90 if size >= 32 else 0.85
        ico_img = create_large_favicon(input_file, output_dir, size, padding_ratio)
        if ico_img:
            ico_images.append(ico_img)
    
    if ico_images:
        ico_file = output_dir / 'favicon.ico'
        # Save as ICO - use the largest image
        ico_images[-1].save(ico_file, format='ICO')
        created_files.append(ico_file)
        print(f"Created: {ico_file} (multi-resolution ICO)")
    
    print()
    print(f"[SUCCESS] Created {len(created_files)} optimized favicon files.")
    print("The logo now fills 85-90% of the favicon space for a larger appearance!")

if __name__ == '__main__':
    main()

