let currentIndex = 0;
const slidesToShow = 3; // Number of visible slides
const sliderContainer = document.querySelector(".slider-container");
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;

// Clone slides for looping effect
for (let i = 0; i < slidesToShow; i++) {
    sliderContainer.appendChild(slides[i].cloneNode(true));
}

function moveSlide(direction) {
    currentIndex += direction;

    // Adjust to loop
    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
        sliderContainer.style.transition = "none"; // Disable animation temporarily
        sliderContainer.style.transform = `translateX(-${totalSlides * (100 / slidesToShow)}%)`;
        setTimeout(() => {
            sliderContainer.style.transition = "transform 1s ease";
            moveSlide(-1);
        }, 10);
        return;
    } else if (currentIndex > totalSlides) {
        currentIndex = 0;
        sliderContainer.style.transition = "none"; // Disable animation temporarily
        sliderContainer.style.transform = "translateX(0)";
        setTimeout(() => {
            sliderContainer.style.transition = "transform 1s ease";
            moveSlide(1);
        }, 10);
        return;
    }

    const offset = -(currentIndex * (100 / slidesToShow));
    sliderContainer.style.transform = `translateX(${offset}%)`;
}

// Auto-slide every 4 seconds
setInterval(() => {
    moveSlide(1);
}, 10000);
