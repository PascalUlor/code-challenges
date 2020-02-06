const merge = (arrA, arrB) =>{
    const elements = arrA.length + arrB.length;
    let mergedArr;
    if (arrA.length == 0) return arrB
    if (arrB.length == 0) return arrA

    let indexLeft = 0
    let indexRight = 0
    let listMerged = []
    while ( listMerged.length < elements) {
        if (arrA[indexLeft] <= arrB[indexRight]) {
            listMerged.push(arrA[indexLeft])
            indexLeft += 1
        } else {
            listMerged.push(arrB[indexRight])
            indexRight += 1
        }
        

    if (indexRight == arrB.length) {
        listMerged.push(...arrA.splice(indexLeft))
        break
    } 
    if ( indexLeft == arrA.length) {
        listMerged.push(...arrB.splice(indexRight))
        break
    }
        
    }
        
        
    mergedArr = listMerged
    return mergedArr
}
    
    
    
    


const mergeSort = (arr) => {
    if (arr.length <= 1) return arr
    // } else {
        let median = Math.floor(arr.length/2)
        let left = arr.slice(0,median);
        let right = arr.slice(median, arr.length)
        return merge(mergeSort(left), mergeSort(right))
    
    // }
    
}

console.log(mergeSort([10,24,76,73]))