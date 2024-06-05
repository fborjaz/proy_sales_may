/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./core/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#212121',
        'secondary': '#333333',
        'accent': '#12c064',
        'text': '#f2f2f2',
        'text-secondary': '#aaaaaa',
        'error': '#dc3545',
      },
      fontFamily: {
        'title': ['Roboto', 'sans-serif'],
        'body': ['Roboto', 'sans-serif']
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}
