document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Get the target anchor's href attribute value
        const targetId = this.getAttribute('href');

        // Scroll to the target anchor point
        
        document.querySelector(Kashi).scrollIntoView({
            behavior: 'smooth'
        });
       document.querySelector(Kedarnath).scrollIntoView({
        behavior: 'smooth'
    });
   document.querySelector(Ujjain_Mahakaleshwar).scrollIntoView({
    behavior: 'smooth'
 });
document.querySelector(Kashi).scrollIntoView({
    behavior: 'smooth'
 });
document.querySelector(Somnath).scrollIntoView({
    behavior: 'smooth'
 });
document.querySelector(Nageshwar).scrollIntoView({
    behavior: 'smooth'
 });
    });
});
