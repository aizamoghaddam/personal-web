
function scrollTrigger(selector) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('navbaractive');
                } else {
                    entry.target.classList.remove('navbaractive');
                }
            });
        }, { threshold: 0.5 });
        observer.observe(element);
    });
}

scrollTrigger('#NavBar');