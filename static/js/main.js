document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".reveal-on-scroll");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, {
        threshold: 0.2  // 20% dell'elemento deve entrare in view
    });

    elements.forEach(el => observer.observe(el));
});




document.addEventListener("DOMContentLoaded", () => {
    const banner = document.getElementById("cookie-banner");
    const acceptBtn = document.getElementById("cookie-accept");

    if (!banner || !acceptBtn) return;

    const accepted = localStorage.getItem("cookieAccepted");

    if (!accepted) {
        banner.style.display = "flex";
    } else {
        banner.style.display = "none";
    }

    acceptBtn.addEventListener("click", () => {
        localStorage.setItem("cookieAccepted", "true");
        banner.style.display = "none";
    });
});

