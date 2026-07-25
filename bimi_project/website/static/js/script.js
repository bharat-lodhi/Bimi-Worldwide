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

if (openPopup && popup) {
    openPopup.addEventListener("click", (e) => {
        e.preventDefault();
        popup.classList.add("active");
        document.body.style.overflow = "hidden";
    });
}

if (closePopup && popup) {
    closePopup.addEventListener("click", () => {
        popup.classList.remove("active");
        document.body.style.overflow = "auto";
    });
}

window.addEventListener("click", (e) => {
    if (popup && e.target === popup) {
        popup.classList.remove("active");
    }
});

// Rotating border effect on hover for .dark-card, .philosophy-wrapper, .worldwide-card, .feature-card, and .cta-premium-card
document.addEventListener("DOMContentLoaded", () => {
    const darkCards = document.querySelectorAll(".dark-card, .philosophy-wrapper, .worldwide-card, .feature-card, .cta-premium-card");
    darkCards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            const angle = Math.atan2(y, x);
            card.style.setProperty("--rotation", `${angle}rad`);
        });
        card.addEventListener("mouseleave", () => {
            card.style.setProperty("--rotation", "0deg");
        });
    });
});