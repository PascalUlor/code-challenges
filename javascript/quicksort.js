const quickSort = (arr)=>{
    if(arr.length <= 1){
        return arr
    }
const left = []
const right = []
const pivot = arr[arr.length - 1]

for(let i = 0; i < arr.length - 1; i++){
    if(arr[i] < pivot){
        left.push(arr[i])
    } else{
        right.push(arr[i])
    }
}
return [...quickSort(left), pivot, ...quickSort(right)]
}

console.log(quickSort([3, 6, 8, 1, 4, 2, 5, 7]))

