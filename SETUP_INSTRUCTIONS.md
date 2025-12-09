# Research Display Website - Setup Instructions

## Project Structure

This Laravel + Inertia.js + Vue 3 + TailwindCSS project has been set up with the following structure:

```
├── app/Http/Controllers/
│   └── ResearchController.php
├── routes/
│   └── web.php
├── resources/
│   ├── js/
│   │   ├── app.js
│   │   ├── Layouts/
│   │   │   └── MainLayout.vue
│   │   ├── Components/
│   │   │   ├── Navbar.vue
│   │   │   ├── Footer.vue
│   │   │   └── SectionTitle.vue
│   │   └── Pages/
│   │       └── Research/
│   │           ├── Home.vue
│   │           ├── About.vue
│   │           ├── Objectives.vue
│   │           ├── Features.vue
│   │           ├── Methodology.vue
│   │           ├── Architecture.vue
│   │           ├── Results.vue
│   │           └── Team.vue
│   └── css/
│       └── app.css
└── tailwind.config.js
```

## Installation Steps

1. **Install PHP Dependencies**:
   ```bash
   composer install
   ```

2. **Install Node Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment**:
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```
   - Edit `.env` file and set your database credentials if needed
   - Set `APP_NAME` to your project name

4. **Build Assets**:
   ```bash
   npm run dev
   # or for production:
   npm run build
   ```

5. **Start Development Server**:
   ```bash
   php artisan serve
   ```
   Then visit `http://localhost:8000` in your browser

## Routes Available

- `/` - Home page
- `/about` - About page
- `/objectives` - Objectives page
- `/features` - Features page
- `/methodology` - Methodology page
- `/architecture` - Architecture page
- `/results` - Results page
- `/team` - Team page

## Customization

All content uses placeholder text that you can easily replace:

- **Project Title**: Search for "Project Title Here" across all files
- **Descriptions**: Look for "Lorem ipsum" or "Replace this with" comments
- **Team Members**: Edit the `teamMembers` array in `Team.vue`
- **Features**: Edit the `features` array in `Features.vue`
- **Technologies**: Edit the `technologies` array in `Methodology.vue`

## Features

- ✅ Fully responsive design
- ✅ Modern UI with TailwindCSS
- ✅ Smooth scrolling
- ✅ Mobile-friendly navigation
- ✅ Clean, editable placeholder content
- ✅ Vue 3 with `<script setup>` syntax
- ✅ Inertia.js routing
- ✅ Consistent component structure

## Notes

- All pages use the `MainLayout` component
- The Navbar automatically highlights the active page
- Screenshot placeholders are included in the Features page
- Diagram placeholders are included in the Architecture page
- All content is easily replaceable with your actual research content

