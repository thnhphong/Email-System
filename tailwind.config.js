const patterns = require('tailwindcss-patterns');
module.exports = {
  mode: 'jit',
  content: ["./dist/**/*.{html,js}", "./src/**/*.{html,js}"],
  theme: {
    extend: {
    },
  },
  plugins: [patterns],
};
