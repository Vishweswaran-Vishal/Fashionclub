// JavaScript is used for toggling loading state
var form = document.querySelector('form');
form.onsubmit = function (event) {
    event.preventDefault();
    form.classList.add('signed');
};