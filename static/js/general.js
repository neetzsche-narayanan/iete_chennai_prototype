function toggleMobileMenu(menuEl){
    let hamMenu = document.getElementById('mobile-menu');
    let mainCont = document.getElementById('main-container');
    let footCont = document.getElementById('page-footer');

    hamMenu.classList.toggle('open');
    mainCont.classList.toggle('menu-open');
    footCont.classList.toggle('menu-open');
};

function changeBackground(element){
    element.target.style.backgroundColor = 'var(--space-cadet)';
    element.target.style.color = 'var(--cornsilk)';
}