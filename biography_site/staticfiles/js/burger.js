// static/js/burger.js
document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('#nav-menu');

    if (burger && nav) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('open');
        });

        // Закрытие меню при клике вне его
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !burger.contains(e.target)) {
                nav.classList.remove('open');
            }
        });
    }
});