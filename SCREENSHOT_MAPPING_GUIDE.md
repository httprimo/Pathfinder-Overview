# Screenshot Mapping Guide

## Overview

All 27 pages from the PATHFINDER User Manual PDF have been extracted and saved as:
- `page-01.png` through `page-27.png` in `public/images/screenshots/`

## How to Map Pages to Steps

1. **Review the PDF**: Open `public/documents/PATHFINDER - User Manual.pdf` and identify which pages contain the screenshots you want to display.

2. **Review the Extracted Pages**: Look at the `page-XX.png` files in `public/images/screenshots/` to see what each page contains.

3. **Update Features.vue**: 
   - Open `resources/js/Pages/Research/Features.vue`
   - Find the `screenshotSteps` array
   - For each step, update:
     - `title`: The actual step title from the manual (e.g., "Registration", "Login", etc.)
     - `description`: What the screenshot shows
     - `image`: The path to the correct page image (e.g., `/images/screenshots/page-05.png`)
     - `details`: Key features visible in that screenshot

## Example Mapping

If page 3 of the manual shows the Dashboard:
```javascript
{
    title: 'Dashboard',
    description: 'Overview of your account activities, applications, and training registrations.',
    image: '/images/screenshots/page-03.png',
    details: [
        'Activity summary',
        'Quick access to key features',
        'Recent updates and notifications'
    ]
}
```

## Tips

- **Not all pages may be needed**: You might only want to use 11 key screenshots (as currently configured), or you might want to add more steps
- **Page order may differ**: The pages in the PDF might not be in the exact order you want for the carousel
- **You can rename files**: If you want, you can rename `page-05.png` to `step-03-dashboard.png` for better organization
- **Add or remove steps**: You can add more steps to the array or remove steps you don't need

## Current Configuration

The carousel is currently set up for 11 steps. If your manual has more or fewer steps:

1. **To add more steps**: Add more objects to the `screenshotSteps` array
2. **To remove steps**: Remove objects from the array
3. **To reorder steps**: Rearrange the objects in the array

## Quick Reference

All available page images:
- `page-01.png` through `page-27.png`

Update the `image` property in each step object to point to the correct page.

