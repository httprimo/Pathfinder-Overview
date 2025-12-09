import defaultTheme from 'tailwindcss/defaultTheme';

/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
        './storage/framework/views/*.php',
        './resources/views/**/*.blade.php',
        './resources/js/**/*.vue',
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Poppins', ...defaultTheme.fontFamily.sans],
            },
            colors: {
                'dark-slate': '#44576D',
                'customblue': '#59708C',
                'customdarkblue': '#415367',
                'customButton': '#6682A3',
                'blue-gray': '#F6F6F6',
                'chart-1': '#A7B1C2',
                'chart-2': '#DFE3EA',
                'chart-3': '#8FA5B3',
                'chart-4': '#6B7D8F',
            },
        },
    },
    plugins: [],
};

