# System Screenshots Folder

This folder contains screenshots from the PATHFINDER User Manual for display in the System Screenshots carousel.

## How to Add Screenshots

1. **Extract screenshots from the User Manual PDF:**
   - Open `public/documents/PATHFINDER - User Manual.pdf`
   - Extract each screenshot from the manual
   - Save them with descriptive filenames following the naming convention below

2. **Naming Convention:**
   - Use the format: `step-XX-description.png` (or `.jpg`)
   - Example: `step-01-registration.png`, `step-02-login.png`, etc.
   - Use two-digit numbers (01, 02, 03, etc.) for proper sorting

3. **Update the Steps Data:**
   - Open `resources/js/Pages/Research/Features.vue`
   - Find the `screenshotSteps` array in the script section
   - Update each step object with:
     - `title`: The step title (e.g., "Registration", "Login")
     - `description`: A brief description of what the screenshot shows
     - `image`: The path to the screenshot (e.g., `/images/screenshots/step-01-registration.png`)
     - `details`: An array of key features shown in the screenshot (optional)

## Example Step Object

```javascript
{
    title: 'Registration',
    description: 'Create your account by entering your information. Use a valid email address—you\'ll receive a verification email after signing up.',
    image: '/images/screenshots/step-01-registration.png',
    details: [
        'User registration form with validation',
        'Email verification required',
        'Secure password requirements'
    ]
}
```

## Image Requirements

- **Format**: PNG or JPG
- **Recommended size**: 1200px width minimum for best quality
- **Aspect ratio**: 16:9 or 4:3 works best
- **File size**: Keep under 1MB per image for optimal loading

## Current Steps Structure

The carousel is configured for 11 steps. Update the `screenshotSteps` array in `Features.vue` to match the actual steps from your User Manual.

## Notes

- The carousel will automatically handle missing images with a placeholder
- Steps can be navigated using arrow buttons, pagination dots, or keyboard arrows
- The progress bar shows completion status
- All steps should have unique titles and descriptions

