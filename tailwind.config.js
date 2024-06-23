/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/**/*.{html,js}","./website/static/src/js/*.{html,js}"],
  theme: {
    extend: {    
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
  safelist: [
    'hidden'
  ]
}

