const defaultTheme = require('tailwindcss/defaultTheme');
const plugin = require('tailwindcss/plugin');

module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    content: [
        './templates/**/*.{html}',
        './templates/*.{html}',
        './**/*.{html}',
        './static/js/**/*.{js}',
        './static/**/*.{html,js}',
    ],
    corePlugins: {    preflight: true,  },
    purge: [
        'static/dist/*.css',
        'static/dist/*.scss',
        'static/dist/*.js',
    ],
    theme: {
        // screens: {
        //     sm: '480px',
        //     md: '768px',
        //     lg: '976px',
        //     xl: '1440px',
        // },
        // colors: {
        //     transparent: 'transparent',
        //     black: '#000',
        //     white: '#fff',
        // },
        // extend: {
        //     spacing: {
        //
        //     },
        //     borderRadius: {
        //         '4xl': '2rem',
        //     }
        // },
        fontFamily: {
            // sans: ['Inter var', ...defaultTheme.fontFamily.sans],
            sans: ['Graphik', 'sans-serif'],
            serif: ['Merriweather', 'serif'],
            // title: ['Acme'],
            // header: ['Lato'],
            // body: ['Roboto'],
            // link: ['Lato'],
        },
    },
    variants: {
        // extend: {
        //     backgroundColor: ['odd'],
        //     backgroundColor: ['even']
        // },
    },
    plugins: [
        // require('@tailwindcss/ui'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),

        plugin(function({
            addUtilities,
            addComponents,
            e,
            prefix,
            config }) {
            // Add your custom styles / plugin here
        }),
    ],
};
