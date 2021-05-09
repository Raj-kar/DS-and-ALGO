function collectOddValues(arr) {
    let newArr = [];

    if (arr.length == 0)
        return newArr

    if (arr[0] % 2 != 0)
        newArr.push(arr[0])

    newArr = newArr.concat(collectOddValues(arr.splice(1)));
    return newArr;
}

console.log(collectOddValues([11, 22, 4131, 1246, 9984, 3525]))
console.log(collectOddValues([3, 21, 531, 316, 984, 125]))
