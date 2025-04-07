I’m building a concurrent image processing system and need to write the JavaScript code for image processing threads. Can you explain how it initiates, coordinates and manages multiple threads for different images, including setup and sync mechanisms?

```javascript
// Managing Image Processing Threads JavaScript Code

const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');
const path = require('path');
const fs = require('fs');

if (isMainThread) {
    const imageFiles = ['image1.jpg', 'image2.jpg', 'image3.jpg'];
    const workers = [];
    let completedImages = 0;
    const results = [];

    /**
     * @function initializeImageProcessingThreads
     * @description Initializes worker threads for image processing tasks.
     */
    function initializeImageProcessingThreads() {
        imageFiles.forEach((file, index) => {
            const worker = new Worker(__filename, { workerData: { file, index } });
            workers.push(worker);
            worker.on('message', (result) => handleProcessingResult(result, index));
            worker.on('error', handleWorkerError);
        });
    }

    /**
     * @function handleProcessingResult
     * @description Handles the processing result from a worker thread.
     * @param {Object} result - The result object containing status and information.
     * @param {number} index - The index of the processed image.
     */
    function handleProcessingResult(result, index) {
        results[index] = result;
        completedImages += 1;
        if (completedImages === imageFiles.length) {
            console.log('All images processed:', results);
        }
    }

    /**
     * @function handleWorkerError
     * @description Logs any errors that occur in the worker threads.
     * @param {Error} error - The error object received from a worker.
     */
    function handleWorkerError(error) {
        console.error('Worker error:', error);
    }

    initializeImageProcessingThreads();
} else {
    const { file, index } = workerData;
    const sharp = require('sharp');
    const inputPath = path.join(__dirname, 'images', file);
    const outputPath = path.join(__dirname, 'processed', `processed_${file}`);

    sharp(inputPath)
        .resize(800, 600)
        .toFile(outputPath, (err, info) => {
            if (err) {
                parentPort.postMessage({ index, status: 'error', error: err.message });
            } else {
                parentPort.postMessage({ index, status: 'success', info });
            }
        });
}
```