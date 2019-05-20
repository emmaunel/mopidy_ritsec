var hamburgerButton = document.querySelector('.ritsec__button');
var mobileNav = document.querySelector('.mobile');

function navOpen() {
  mobileNav.classList.add('open');
}

function navClose() {
    mobileNav.classList.remove('open');
}

hamburgerButton.addEventListener('click', navOpen);
mobileNav.addEventListener('click', navClose);
