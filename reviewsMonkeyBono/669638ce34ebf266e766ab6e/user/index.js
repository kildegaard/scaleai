document.addEventListener('DOMContentLoaded', () => {
    const emailForm = document.getElementById('email-form');
    const emailInput = document.getElementById('email');
    const emailDisplay = document.getElementById('email-display');

    emailForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the form from submitting
        if (emailInput.checkValidity()) {
            emailDisplay.textContent = "You subscribed with: " + emailInput.value;
            emailDisplay.style.display = 'block';
        }
    });
});