// static/js/sidebar.js
document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('#sidebar');
    const mainContent = document.querySelector('#main-content');
    const burger = document.querySelector('.burger');

    if (burger && sidebar && mainContent) {
        burger.addEventListener('click', () => {
            sidebar.classList.toggle('open');
            mainContent.classList.toggle('shifted');
        });

        document.addEventListener('click', (e) => {
            if (!sidebar.contains(e.target) && !burger.contains(e.target)) {
                sidebar.classList.remove('open');
                mainContent.classList.remove('shifted');
            }
        });
    } else {
        console.error('Не найдены элементы: burger, sidebar или main-content');
    }
});