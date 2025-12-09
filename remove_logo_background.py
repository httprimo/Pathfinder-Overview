#!/usr/bin/env python3
"""
Script to remove white background from Pathfinder logo and create a transparent PNG.
"""

import os
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL (Pillow) is not installed. Install it with: pip install Pillow")

def remove_white_background(input_path, output_path, threshold=240):
    """
    Remove white/light background from an image and make it transparent.
    
    Args:
        input_path: Path to input image
        output_path: Path to save output image with transparency
        threshold: RGB threshold (0-255) for considering a pixel as "white"
    """
    if not HAS_PIL:
        print("Error: PIL (Pillow) is required. Install with: pip install Pillow")
        return False
    
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Get image data
        data = img.getdata()
        
        # Create new image data with transparency
        new_data = []
        for item in data:
            # If pixel is white/light (above threshold), make it transparent
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)  # Keep original
        
        # Update image with new data
        img.putdata(new_data)
        
        # Save the image
        img.save(output_path, 'PNG')
        print(f"Successfully created transparent logo: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def main():
    # Get project root directory
    project_root = Path(__file__).parent
    logo_dir = project_root / 'public' / 'images' / 'logo'
    input_file = logo_dir / 'Pathfinder_Logo.png'
    output_file = logo_dir / 'Pathfinder_Logo_Transparent.png'
    
    if not input_file.exists():
        print(f"Error: Logo file not found at {input_file}")
        return
    
    print(f"Processing logo: {input_file}")
    print(f"Output will be saved to: {output_file}")
    
    # Remove background with threshold of 240 (adjust if needed)
    success = remove_white_background(input_file, output_file, threshold=240)
    
    if success:
        print("\n[SUCCESS] Logo processed successfully!")
        print(f"  Original: {input_file}")
        print(f"  Transparent: {output_file}")
        print("\nYou can now use Pathfinder_Logo_Transparent.png as your favicon.")
        print("Update the favicon links in resources/views/app.blade.php to use the new file.")
    else:
        print("\n[ERROR] Failed to process logo.")

if __name__ == '__main__':
    main()

