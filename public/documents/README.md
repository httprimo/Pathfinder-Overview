# Research Documents Folder

Place your research paper file in this folder:

1. `research-paper.pdf` (or your preferred filename) - Your complete research paper document

## File Requirements:
- Recommended format: PDF (`.pdf`)
- Other supported formats: `.docx`, `.doc` (though PDF is preferred for web viewing)
- Ensure the file is properly named and accessible

## Accessing the Document:
Once placed in this folder, you can access it via:
- URL: `/documents/research-paper.pdf` (or your filename)
- Or link to it from any page using: `/documents/your-filename.pdf`

## Suggested Integration:
You may want to add a download/link button to the research paper in:
- The **Results** page (`resources/js/Pages/Research/Results.vue`)
- The **Home** page (`resources/js/Pages/Research/Home.vue`)
- Or create a dedicated section for it

Example link in Vue:
```vue
<a 
    href="/documents/research-paper.pdf" 
    target="_blank"
    class="bg-customButton text-white px-6 py-3 rounded-lg font-semibold hover:bg-customdarkblue transition-all duration-300"
>
    Download Research Paper
</a>
```

