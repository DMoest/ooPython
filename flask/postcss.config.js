const path = require('path');

module.exports = (ctx) => ({
    plugins: {
        tailwindcss: {

        },
        autoprefixer: {

        },
        content: [
            path.resolve(__dirname, './templates/**/*.html')
        ],
        // require('tailwindcss')(path.resolve(__dirname, './tailwind.config.js')),
        // require('autoprefixer'),
        process.flaskenv.FLASK_ENV === 'production' && require('@fullhuman/postcss-purgecss')({
            content: [
                path.resolve(__dirname, './templates/**/*.html')
            ],
            defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
        })
    },
});
