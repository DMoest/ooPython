module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
        fontFamily: {
            'header': ['Oswald'],
            'subheader': ['Oswald'],
            'paragraph': ['Merriweather'],
            'button': ['Oswald'],
        },
        extend: {
            colors: {
                primary: {
                    10: '#FFF5C3',
                },
                secondary: {
                    10: '#505050',
                    20: '#2f2f2f',
                },
                tertiary: {
                    10: '#FF7260',
                },
                quaternary: {
                    10: '#129793',
                },
                quinary: {
                    10: '#9BD7D5',
                },
            }
        },  },
    plugins: [],
};
