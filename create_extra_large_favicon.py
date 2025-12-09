#!/usr/bin/env python3
"""
Create an extra large favicon that fills 95% of the space for maximum visibility.
"""

from pathlib import Path
from PIL import Image

def create_extra_large_favicon(input_path, output_path, size=32, fill_ratio=0.95):
    """Create a favicon where the logo fills 95% of the space."""
    img = Image.open(input_path)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Calculate logo size to fill 95% of space
    logo_size = int(size * fill_ratio)
    
    # Resize logo
    resized = img.copy()
    resized.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
    
    # Create transparent background
    favicon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # Center the logo
    x_offset = (size - resized.width) // 2
    y_offset = (size - resized.height) // 2
    
    # Paste logo
    favicon.paste(resized, (x_offset, y_offset), resized)
    
    # Save
    favicon.save(output_path, 'PNG', optimize=True)
    print(f"Created extra large favicon: {output_path} ({size}x{size}, fills {int(fill_ratio*100)}%)")

def main():
    project_root = Path(__file__).parent
    logo_dir = project_root / 'public' / 'images' / 'logo'
    input_file = logo_dir / 'Pathfinder_Logo_Transparent.png'
    
    # Create extra large versions for public root
    sizes = [16, 32, 48]
    for size in sizes:
        fill_ratio = 0.95 if size >= 32 else 0.90
        output_file = project_root / 'public' / f'favicon-{size}x{size}.png'
        create_extra_large_favicon(input_file, output_file, size, fill_ratio)
    
    # Create ICO with largest size
    ico_img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    logo = Image.open(input_file)
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')
    logo.thumbnail((int(32 * 0.95), int(32 * 0.95)), Image.Resampling.LANCZOS)
    x = (32 - logo.width) // 2
    y = (32 - logo.height) // 2
    ico_img.paste(logo, (x, y), logo)
    ico_img.save(project_root / 'public' / 'favicon.ico', format='ICO')
    print("Created favicon.ico")

if __name__ == '__main__':
    main()

