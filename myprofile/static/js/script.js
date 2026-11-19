
// MOBILE NAVIGATION

const menuBtn = document.getElementById("menuBtn");
const navbar = document.getElementById("navbar");

menuBtn.addEventListener("click", function () {

    navbar.classList.toggle("active");

    const isOpen = navbar.classList.contains("active");
    menuBtn.setAttribute("aria-expanded", String(isOpen));

});


// CLOSE MOBILE MENU AFTER CLICKING A LINK

document.querySelectorAll(".navbar a").forEach(link => {

    link.addEventListener("click", function () {

        navbar.classList.remove("active");
        menuBtn.setAttribute("aria-expanded", "false");

    });

});


// DARK MODE

const themeBtn = document.getElementById("themeBtn");

if (localStorage.getItem("portfolioTheme") === "dark") {

    document.body.classList.add("dark");
    themeBtn.textContent = "☀";

}

themeBtn.addEventListener("click", function () {

    document.body.classList.toggle("dark");

    const darkMode = document.body.classList.contains("dark");

    themeBtn.textContent = darkMode ? "☀" : "☾";

    localStorage.setItem(
        "portfolioTheme",
        darkMode ? "dark" : "light"
    );

});


// PROJECT FILTERS

const filterButtons = document.querySelectorAll(".filter-btn");
const projectCards = document.querySelectorAll(".project-card");

filterButtons.forEach(button => {

    button.addEventListener("click", function () {

        filterButtons.forEach(btn => {
            btn.classList.remove("active");
        });

        this.classList.add("active");

        const filter = this.dataset.filter;

        projectCards.forEach(card => {

            if (
                filter === "all" ||
                card.dataset.category === filter
            ) {

                card.classList.remove("hidden");

            } else {

                card.classList.add("hidden");

            }

        });

    });

});


// SCROLL REVEAL ANIMATION

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("visible");

            observer.unobserve(entry.target);

        }

    });

}, {
    threshold: 0.12
});

document.querySelectorAll(
    ".section-heading, .about-text, .mini-card, .skill-card, .project-card, .timeline-item, .recognition-card, .contact-info, .contact-form"
).forEach(element => {

    element.classList.add("reveal");
    observer.observe(element);

});


// CONTACT FORM

const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    const subject = encodeURIComponent(
        "Portfolio Contact - " + name
    );

    const body = encodeURIComponent(
        "Hello Battina,\n\n" +
        message +
        "\n\nFrom: " + name +
        "\nEmail: " + email
    );

    document.getElementById("formMessage").textContent =
        "Opening your email application...";

    window.location.href =
        "mailto:battinaroy@gmail.com?subject=" +
        subject + "&body=" + body;

});


// CURRENT YEAR

document.getElementById("year").textContent =
    new Date().getFullYear();
