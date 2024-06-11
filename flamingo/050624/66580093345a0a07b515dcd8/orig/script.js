document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.newcar');
    const dotsContainer = document.querySelector('.dots-container');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    let count = 0;
    let interval = 3000;
  
    // Create indicator dots
    for (let i = 0; i < images.length; i++) {
      const dot = document.createElement('span');
      dot.className = 'dot';
      dotsContainer.appendChild(dot);
    }
  
    const dots = document.querySelectorAll('.dot');
  
    // Set initial image and dot
    images[count].style.display = 'block';
    dots[count].classList.add('active');
  
    // Function to show the next image
    function showNextImage() {
      images[count].style.display = 'none';
      dots[count].classList.remove('active');
      count = (count + 1) % images.length;
      images[count].style.display = 'block';
      dots[count].classList.add('active');
    }
  
    // Function to show the previous image
    function showPrevImage() {
      images[count].style.display = 'none';
      dots[count].classList.remove('active');
      count = (count - 1 + images.length) % images.length;
      images[count].style.display = 'block';
      dots[count].classList.add('active');
    }
  
    // Function to adjust carousel to different screen sizes
    function adjustCarousel() {
      const screenWidth = window.innerWidth;
      const imagesPerScreen = Math.floor(screenWidth / images[0].offsetWidth);
      const visibleImages = Array.from(images).slice(count, count + imagesPerScreen);
      images.forEach((image) => {
        image.style.display = 'none';
      });
      visibleImages.forEach((image) => {
        image.style.display = 'block';
      });
    }
  
    // Add event listeners for navigation buttons
    nextButton.addEventListener('click', showNextImage);
    prevButton.addEventListener('click', showPrevImage);
  
    // Add event listener for window resize
    window.addEventListener('resize', adjustCarousel);
  
    // Set interval for automatic carousel
    setInterval(showNextImage, interval);
  
    // Initial adjustment for the carousel
    adjustCarousel();
  });
  