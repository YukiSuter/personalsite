/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/**/*.{html,js}","./website/static/src/js/*.{html,js}"],
  theme: {
    extend: {  
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '100ch', // add required value here
          }
        }
      }  
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
  safelist: [
    'hidden'
  ]
}

