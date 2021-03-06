/* jshint esversion: 8 */
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')     // replace '&' with '-and-'
        .replace(/[\s]+/g, '-')     // replace spaces, special characters and dashes with a single dash
        .replace(/(\'|\")+/g, '');     // replace spaces, special characters and dashes with a single dash
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});
