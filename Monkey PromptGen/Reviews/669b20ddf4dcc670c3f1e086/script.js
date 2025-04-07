// Data Storage (Local Storage)
const sightings = JSON.parse(localStorage.getItem('birdSightings')) || [];

// Form Handling
const sightingForm = document.querySelector('#sighting-form form');
sightingForm.addEventListener('submit', event => {
    event.preventDefault();

    const species = document.getElementById('species').value;
    const date = document.getElementById('date').value;
    const location = document.getElementById('location').value;
    const photoUrl = document.getElementById('photo-url').value;

    const newSighting = { species, date, location, photoUrl };
    sightings.push(newSighting);
    localStorage.setItem('birdSightings', JSON.stringify(sightings));

    displaySightings(sightings);
    sightingForm.reset();
});

// Gallery Display
const sightingGallery = document.getElementById('gallery-content');
function displaySightings(sightingsToDisplay) {
    sightingGallery.innerHTML = '';
    sightingsToDisplay.forEach(sighting => {
        const item = document.createElement('div');
        item.className = 'gallery-item';
        item.innerHTML = `
            <img src="${sighting.photoUrl}" alt="${sighting.species}">
            <div class="gallery-item-details">
                <p><strong>Species:</strong> ${sighting.species}</p>
                <p><strong>Date:</strong> ${sighting.date}</p>
                <p><strong>Location:</strong> ${sighting.location}</p>
            </div>
        `;
        sightingGallery.appendChild(item);
    });
}

// Infinite Scroll
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadMoreSightings();
    }
});

let currentIndex = 0;
const loadMoreSightings = () => {
    const nextSightings = sightings.slice(currentIndex, currentIndex + 10);
    displaySightings(nextSightings);
    currentIndex += 10;
}

// Search Functionality
const searchInput = document.getElementById('input');
searchInput.type = 'text';
searchInput.placeholder = 'Search by species, date, or location';
searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredSightings = sightings.filter(sighting =>
        sighting.species.toLowerCase().includes(searchTerm) ||
        sighting.date.includes(searchTerm) ||
        sighting.location.toLowerCase().includes(searchTerm)
    );
    displaySightings(filteredSightings);
});
document.body.insertBefore(searchInput, sightingGallery);

// Initial Display
displaySightings(sightings.slice(0, 10));
