#!/usr/bin/env python3
"""
Create a zoomed/cropped favicon where the logo appears 3x larger by showing only the center portion.
"""

from pathlib import Path
from PIL import Image

def create_zoomed_favicon(input_path, output_path, size=32, zoom_factor=3.0):
    """
    Create a favicon where the logo is zoomed in 3x to appear much larger.
    This crops to the center and scales it up.
    """
    img = Image.open(input_path)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get original dimensions
    orig_width, orig_height = img.size
    
    # Calculate crop box to get center portion (1/zoom_factor of original)
    crop_size = int(min(orig_width, orig_height) / zoom_factor)
    left = (orig_width - crop_size) // 2
    top = (orig_height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size
    
    # Crop to center
    cropped = img.crop((left, top, right, bottom))
    
    # Resize the cropped portion to fill the entire favicon
    resized = cropped.resize((size, size), Image.Resampling.LANCZOS)
    
    # Create transparent background (though it should fill completely)
    favicon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    favicon.paste(resized, (0, 0), resized)
    
    # Save
    favicon.save(output_path, 'PNG', optimize=True)
    print(f"Created zoomed favicon: {output_path} ({size}x{size}, {zoom_factor}x zoom)")

def main():
    project_root = Path(__file__).parent
    logo_dir = project_root / 'public' / 'images' / 'logo'
    input_file = logo_dir / 'Pathfinder_Logo_Transparent.png'
    
    # Create zoomed versions (3x larger appearance)
    sizes = [16, 32, 48]
    zoom_factor = 3.0  # 3x zoom
    
    for size in sizes:
        output_file = project_root / 'public' / f'favicon-{size}x{size}.png'
        create_zoomed_favicon(input_file, output_file, size, zoom_factor)
    
    # Create ICO with 32x32 zoomed version
    ico_img = Image.open(input_file)
    if ico_img.mode != 'RGBA':
        ico_img = ico_img.convert('RGBA')
    
    orig_w, orig_h = ico_img.size
    crop_size = int(min(orig_w, orig_h) / 3.0)
    left = (orig_w - crop_size) // 2
    top = (orig_h - crop_size) // 2
    cropped = ico_img.crop((left, top, left + crop_size, top + crop_size))
    zoomed = cropped.resize((32, 32), Image.Resampling.LANCZOS)
    
    ico_final = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    ico_final.paste(zoomed, (0, 0), zoomed)
    ico_final.save(project_root / 'public' / 'favicon.ico', format='ICO')
    print("Created favicon.ico (3x zoomed)")

if __name__ == '__main__':
    main()

