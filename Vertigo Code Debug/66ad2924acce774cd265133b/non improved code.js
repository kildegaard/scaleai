function shuffleArray(array) {
    let result = []
    let tempArray = array.slice() // create a copy of the original array

    while (tempArray.length > 0) {
        let randomIndex = Math.floor(Math.random() * tempArray.length)
        result.push(tempArray[randomIndex])
        tempArray.splice(randomIndex, 1) // remove the element from the temporary array
    }

    return result
}

const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log("Original Array:", originalArray)

const shuffledArray = shuffleArray(originalArray)
console.log("Shuffled Array:", shuffledArray)