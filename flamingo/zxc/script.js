// // Add an event listener to the button with the id 'magicDoor' to listen for a click event.
// document.getElementById('magicDoor').addEventListener('click', function () {
//     // Get the element with the id 'storyText' and store it in the storyText variable.
//     const storyText = document.getElementById('storyText');

//     // Update the text content of the storyText element to display a new message.
//     storyText.textContent = 'You have opened the magic door. Welcome to the enchanted world!';

//     // Get the element with the id 'treeImage' and store it in the treeImage variable.
//     const treeImage = document.getElementById('treeImage');

//     // Apply a CSS transform to rotate the treeImage by 360 degrees, creating a spinning effect.
//     treeImage.style.transform = 'rotate(360deg)';

//     // Set the transition property to smoothly animate the transform over a period of 2 seconds.
//     treeImage.style.transition = 'transform 2s';
// });


// let storyStep = 1;

// document.getElementById('magicDoor').addEventListener('click', function () {
//     if (storyStep === 1) {
//         const storyText = document.getElementById('storyText');
//         storyText.textContent = 'You have opened the magic door. Welcome to the enchanted world!';
//         const treeImage = document.getElementById('treeImage');
//         treeImage.style.transform = 'rotate(360deg)';
//         treeImage.style.transition = 'transform 2s';
//         const magicDoorButton = document.getElementById('magicDoor');
//         magicDoorButton.textContent = "Let's start this adventure";
//         storyStep = 2;
//     } else if (storyStep === 2) {
//         const storyText = document.getElementById('storyText');
//         storyText.textContent = 'Hello, I am the fairy of the forest and I will help you on this magical adventure.';
//         const treeImage = document.getElementById('treeImage');
//         treeImage.src = 'fairy.png';
//         treeImage.style.opacity = 0;
//         setTimeout(function () {
//             treeImage.style.transition = 'opacity 5s';
//             treeImage.style.opacity = 1;
//         }, 100);
//     }
// });


let currentStep = 1;

document.getElementById('magicDoor').addEventListener('click', function () {
    if (currentStep === 1) {
        const storyText = document.getElementById('storyText');
        storyText.textContent = 'You have opened the magic door. Welcome to the enchanted world!';
        const treeImage = document.getElementById('treeImage');
        treeImage.style.transform = 'rotate(360deg)';
        treeImage.style.transition = 'transform 2s';
        const magicDoorButton = document.getElementById('magicDoor');
        magicDoorButton.textContent = "Let's start this adventure";
        currentStep = 2;
    } else if (currentStep === 2) {
        const storyText = document.getElementById('storyText');
        storyText.textContent = 'Hello, I am the fairy of the forest and I will help you on this magical adventure.';
        const treeImage = document.getElementById('treeImage');
        treeImage.src = 'fairy.png';
        treeImage.style.opacity = 0;
        setTimeout(function () {
            treeImage.style.transition = 'opacity 5s';
            treeImage.style.opacity = 1;
        }, 100);
        const magicDoorButton = document.getElementById('magicDoor');
        magicDoorButton.style.display = 'none'; // hide the button
    }
});