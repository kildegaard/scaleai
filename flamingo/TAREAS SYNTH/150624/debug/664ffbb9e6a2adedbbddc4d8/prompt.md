I’m setting up a customer review system for my metalworks shop. The js for submitting and showing reviews isn’t working right and reviews aren’t posting or showing up. Can you help me debug? Here’s the html and js

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Reviews</title>
</head>
<body>
    <div id="review-system">
        <h2>Submit Your Review</h2>
        <input type="text" id="reviewer-name" placeholder="Your Name">
        <textarea id="review-text" placeholder="Your Review"></textarea>
        <input type="number" id="review-rating" placeholder="Rating (1-5)">
        <button id="submit-review">Submit Review</button>
        <h2>Reviews</h2>
        <div id="reviews"></div>
    </div>
    <script src="reviews.js"></script>
</body>
</html>
```

```javascript
const reviewerNameInput = document.getElementById('reviewer-name');
const reviewTextInput = document.getElementById('review-text');
const reviewRatingInput = document.getElementById('review-rating');
const submitReviewButton = document.getElementById('submit-review');
const reviewsContainer = document.getElementById('reviews');

submitReviewButton.addEventListener('click', submitReview);

function submitReview() {
    const name = reviewerNameInput.value;
    const text = reviewTextInput.value;
    const rating = parseInt(reviewRatingInput.value);

    if (!name || !text || isNaN(rating) || rating < 1 || rating > 5) {
        alert('Please enter your name, review, and a rating between 1 and 5.');
        return;
    }

    const review = {
        name,
        text,
        rating
    };

    addReviewToDOM(review);
    clearInputs();
}

function addReviewToDOM(review) {
    const reviewElement = document.createElement('div');
    reviewElement.className = 'review';

    reviewElement.innerHTML = `
        <h3>${review.name}</h3>
        <p>${review.text}</p>
        <p>Rating: ${review.rating}</p>
    `;

    reviewsContainer.appendChild(reviewElement);
}

function clearInputs() {
    reviewerNameInput.value = '';
    reviewTextInput.value = '';
    reviewRatingInput.value = '';
}
```