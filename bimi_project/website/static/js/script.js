const header = document.querySelector(".header");
window.addEventListener("scroll", () => {
    header.classList.toggle("scrolled", window.scrollY > 40);
});

const navToggle = document.getElementById("navToggle");
const mobileMenu = document.getElementById("mobileMenu");
navToggle.addEventListener("click", () => {
        navToggle.classList.toggle("active");
        mobileMenu.classList.toggle("open");
    }

);


// ----------------------------------------------

const openPopup = document.getElementById("openPopup");
const popup = document.getElementById("popupForm");
const closePopup = document.getElementById("closePopup");

openPopup.addEventListener("click", (e) => {
    e.preventDefault();
    popup.classList.add("active");
    document.body.style.overflow = "hidden";
});

closePopup.addEventListener("click", () => {
    popup.classList.remove("active");
    document.body.style.overflow = "auto";
});

window.addEventListener("click", (e) => {

    if (e.target === popup) {
        popup.classList.remove("active");
    }

});