function compressBoxTwice(boxes1, boxes2) {
    boxes1.forEach(element => {
        console.log(element);
    });

    boxes2.forEach(element => {
        console.log(element);
    });
}

// Time Complexity - O(a + b)
compressBoxTwice([1, 2, 3, 4], [1])