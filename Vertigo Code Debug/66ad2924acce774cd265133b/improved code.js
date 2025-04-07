const _ = require('underscore')

function shuffleWithUnderscore(array) {
    return _.shuffle(array)
}

const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log("Original Array:", originalArray)

const shuffledArray = shuffleWithUnderscore(originalArray)
console.log("Shuffled Array:", shuffledArray)