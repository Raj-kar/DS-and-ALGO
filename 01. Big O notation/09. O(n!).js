function nFacRuntimeFunc(n) {
    console.log(n)
    for (let i = 0; i < n; i++) {
        nFacRuntimeFunc(n - 1);
    }
}

nFacRuntimeFunc(3)

// Any algorithm that calculates all permutation of a given array is O(N!).