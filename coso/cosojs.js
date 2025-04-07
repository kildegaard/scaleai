// // const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// // const newArray = [9, ...originalArray, 11]; // [9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// // const mergedArray = [...originalArray, ...newArray]; // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// // console.log(originalArray);
// // console.log(newArray);

// // console.log(mergedArray);

// const originalArray = [1, 2, 3];

// // Using destructuring
// const [first, ...rest] = originalArray;
// console.log(first); // 1
// console.log(rest); // [2, 3]

// // Using slice
// const shiftedArray = originalArray.slice(1);
// console.log(shiftedArray); // [2, 3]

const originalArray = [1, 2, 3, 4];
const [, ...newArray] = originalArray;

console.log(newArray); // Output: [2, 3, 4]