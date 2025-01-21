document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(Formation).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Temple).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(WorshippingMethods).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Significance).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Timings).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Transportation).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Prasadam).scrollIntoView({
            behavior: 'smooth'
        });
        document.querySelector(Stotram).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
