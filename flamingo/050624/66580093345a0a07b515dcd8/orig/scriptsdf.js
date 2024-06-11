document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.newcar');
    const leftBtn = document.getElementById('leftBtn');
    const rightBtn = document.getElementById('rightBtn');
    const indicators = document.querySelectorAll('.indicator');
    let count = 0;
    const interval = 3000;

    // Corrected Carousel function to avoid overlapping and manage display correctly
    function Carousel() {
        images.forEach(img => img.style.display = 'none');
        indicators.forEach(ind => ind.classList.remove('active'));

        images[count].style.display = 'block';
        indicators[count].classList.add('active');

        count = (count + 1) % images.length;
    }

    // Initial display
    Carousel();

    // Navigation buttons
    function showImage(index) {
        count = index;
        Carousel();
    }

    function nextImage() {
        count = (count + 1) % images.length;
        showImage(count);
    }

    function prevImage() {
        count = (count - 1 + images.length) % images.length;
        showImage(count);
    }

    rightBtn.addEventListener('click', nextImage);
    leftBtn.addEventListener('click', prevImage);

    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            showImage(index);
        });
    });

    setInterval(Carousel, interval);
});
