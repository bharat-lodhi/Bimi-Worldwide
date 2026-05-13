// Header shadow
const header = document.querySelector(".header");
window.addEventListener("scroll", () => {
    header.classList.toggle("scrolled", window.scrollY > 40);
});

// Mobile menu toggle
const toggle = document.querySelector(".nav-toggle");
const mobileMenu = document.querySelector(".mobile-menu");
toggle.addEventListener("click", () => {
    mobileMenu.style.display =
        mobileMenu.style.display === "block" ? "none" : "block";
});

// Scroll reveal
const reveals = document.querySelectorAll(".reveal");
const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) e.target.classList.add("show");
    });
}, { threshold: .2 });
reveals.forEach(el => observer.observe(el));