// Define an array of animal objects
const animals = [
    { name: 'Elephant', size: 5000 },
    { name: 'Giraffe', size: 4000 },
    { name: 'Hippopotamus', size: 3200 },
    { name: 'Rhino', size: 2500 },
    { name: 'Buffalo', size: 2000 },
    { name: 'Zebra', size: 1000 },
    { name: 'Gazelle', size: 500 },
    { name: 'Rabbit', size: 200 },
    { name: 'Mouse', size: 50 }
];

// Sort the animals by size in ascending order
animals.sort((a, b) => a.size - b.size);

// Log the sorted animals to the console
console.log(animals);
