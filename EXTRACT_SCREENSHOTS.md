# How to Extract Screenshots from the User Manual PDF

This guide will help you extract screenshots from the `PATHFINDER - User Manual.pdf` file.

## Method 1: Using the Python Script (Recommended)

### Step 1: Install Required Library

Open a terminal in the project root and run:

```bash
pip install PyMuPDF
```

Or if you prefer pdf2image:

```bash
pip install pdf2image
# On Windows, also download poppler from: https://github.com/oschwartz10612/poppler-windows/releases
```

### Step 2: Run the Extraction Script

```bash
python extract_screenshots.py
```

This will extract all images from the PDF and save them to `public/images/screenshots/`.

### Step 3: Rename and Organize

After extraction, you'll need to:
1. Review the extracted images
2. Rename them according to the steps in the manual (e.g., `step-01-registration.png`)
3. Update the `screenshotSteps` array in `resources/js/Pages/Research/Features.vue` with the correct titles and descriptions

## Method 2: Manual Extraction (Alternative)

If you prefer to extract screenshots manually:

### Using Adobe Acrobat Reader:
1. Open the PDF in Adobe Acrobat Reader
2. Go to each page with a screenshot
3. Right-click on the image → "Copy Image"
4. Paste into an image editor (Paint, Photoshop, etc.)
5. Save as PNG to `public/images/screenshots/` with appropriate names

### Using Windows Snipping Tool:
1. Open the PDF in any PDF viewer
2. Navigate to the page with the screenshot
3. Use Windows Snipping Tool (Win + Shift + S) to capture the screenshot
4. Save to `public/images/screenshots/` with appropriate names

### Using Online Tools:
1. Upload the PDF to an online PDF to image converter
2. Download the converted images
3. Save to `public/images/screenshots/` with appropriate names

## Method 3: Using PDF Viewers with Export

Some PDF viewers allow you to export pages as images:

### Using Chrome/Edge:
1. Open the PDF in Chrome or Edge
2. Use browser extensions to export pages as images
3. Save to `public/images/screenshots/`

## After Extraction

Once you have the screenshots:

1. **Rename them** following the pattern: `step-XX-description.png`
   - Example: `step-01-registration.png`, `step-02-login.png`, etc.

2. **Update the step data** in `resources/js/Pages/Research/Features.vue`:
   - Open the file
   - Find the `screenshotSteps` array
   - Update each step with:
     - Correct `title` (from the manual)
     - Accurate `description` (what the screenshot shows)
     - Correct `image` path
     - Relevant `details` array

3. **Test the carousel** by running the development server and navigating to the Features page

## Naming Convention

Use this naming pattern for consistency:
- `step-01-registration.png`
- `step-02-login.png`
- `step-03-dashboard.png`
- etc.

Use two-digit numbers (01, 02, 03...) for proper sorting.

## Image Requirements

- **Format**: PNG or JPG
- **Recommended size**: 1200px width minimum
- **File size**: Keep under 1MB per image for optimal loading
- **Aspect ratio**: 16:9 or 4:3 works best

