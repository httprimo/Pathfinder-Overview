#!/usr/bin/env python3
"""
Script to create optimized favicon sizes from the Pathfinder logo.
Creates multiple sizes optimized for browser tabs.
"""

import os
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL (Pillow) is not installed. Install it with: pip install Pillow")

def create_favicon_sizes(input_path, output_dir, sizes=[16, 32, 48, 64, 96, 128, 192, 256, 512]):
    """
    Create optimized favicon sizes from the input image.
    
    Args:
        input_path: Path to input image (transparent PNG)
        output_dir: Directory to save favicon files
        sizes: List of sizes to create
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
        
        # Get the original size
        original_size = img.size
        print(f"Original image size: {original_size}")
        
        # Create output directory if it doesn't exist
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        created_files = []
        
        for size in sizes:
            # Resize maintaining aspect ratio, using high-quality resampling
            # Use thumbnail to maintain aspect ratio
            resized = img.copy()
            resized.thumbnail((size, size), Image.Resampling.LANCZOS)
            
            # Create a new image with the exact size and transparent background
            favicon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            
            # Calculate position to center the logo
            x_offset = (size - resized.width) // 2
            y_offset = (size - resized.height) // 2
            
            # Paste the resized logo onto the centered transparent background
            favicon.paste(resized, (x_offset, y_offset), resized)
            
            # Save the favicon
            output_file = output_dir / f'favicon-{size}x{size}.png'
            favicon.save(output_file, 'PNG', optimize=True)
            created_files.append(output_file)
            print(f"Created: {output_file} ({size}x{size})")
        
        # Also create a standard favicon.ico (multi-resolution ICO file)
        # Create ICO with multiple sizes
        ico_sizes = [16, 32, 48]
        ico_images = []
        for size in ico_sizes:
            resized = img.copy()
            resized.thumbnail((size, size), Image.Resampling.LANCZOS)
            ico_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            x_offset = (size - resized.width) // 2
            y_offset = (size - resized.height) // 2
            ico_img.paste(resized, (x_offset, y_offset), resized)
            ico_images.append(ico_img)
        
        # Save as ICO (PIL supports saving ICO with multiple sizes)
        ico_file = output_dir / 'favicon.ico'
        ico_images[0].save(ico_file, format='ICO', sizes=[(img.width, img.height) for img in ico_images])
        created_files.append(ico_file)
        print(f"Created: {ico_file} (multi-resolution ICO)")
        
        return True, created_files
        
    except Exception as e:
        print(f"Error processing image: {e}")
        import traceback
        traceback.print_exc()
        return False, []

def main():
    # Get project root directory
    project_root = Path(__file__).parent
    logo_dir = project_root / 'public' / 'images' / 'logo'
    input_file = logo_dir / 'Pathfinder_Logo_Transparent.png'
    output_dir = logo_dir / 'favicons'
    
    if not input_file.exists():
        print(f"Error: Transparent logo file not found at {input_file}")
        print("Run remove_logo_background.py first to create the transparent version.")
        return
    
    print(f"Creating optimized favicons from: {input_file}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Create favicons in multiple sizes
    success, files = create_favicon_sizes(
        input_file, 
        output_dir,
        sizes=[16, 32, 48, 64, 96, 128, 192, 256, 512]
    )
    
    if success:
        print()
        print("[SUCCESS] Favicons created successfully!")
        print(f"Created {len(files)} favicon files.")
        print("\nYou can now update resources/views/app.blade.php to use these optimized favicons.")
    else:
        print()
        print("[ERROR] Failed to create favicons.")

if __name__ == '__main__':
    main()

