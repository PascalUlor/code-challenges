const arr = [19, 473, 500, 511, 750, 2116];

class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


const createMinimalBST = (arr, start, end) => {
    if (end < start) {
        return null;
    }
    const mid = (start + end) >> 1;
    const node = new Node(arr[mid]);
    node.left = createMinimalBST(arr, start, mid - 1);
    node.right = createMinimalBST(arr, mid + 1, end);
    return node;
};

console.log(createMinimalBST(arr, 0, arr.length - 1));
