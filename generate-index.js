import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Read the manifest
const manifestPath = path.join(__dirname, 'public', 'build', 'manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

// Get the app entry point
const appEntry = manifest['resources/js/app.js'];
const appJs = `/build/${appEntry.file}`;
const appCss = appEntry.css ? `/build/${appEntry.css[0]}` : '';

// Generate HTML
const html = `<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Pathfinder</title>
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=poppins:400,500,600&display=swap" rel="stylesheet" />
        ${appCss ? `<link rel="stylesheet" href="${appCss}">` : ''}
    </head>
    <body class="font-sans antialiased">
        <div id="app" data-page='{"component":"Research/Home","props":{},"url":"/","version":null}'></div>
        <script>
            window.Ziggy = {};
        </script>
        <script type="module" src="${appJs}"></script>
    </body>
</html>`;

// Write to public/index.html
fs.writeFileSync(path.join(__dirname, 'public', 'index.html'), html);
console.log('Generated index.html with correct asset paths');

