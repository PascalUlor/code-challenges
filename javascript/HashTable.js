const hashFunc = (s, capacity) =>{
  let hash = 17;
  
  for(let i = 0; i < s.length; i++){
    let value = s.charCodeAt(i) - 96
    hash = (hash + 31 * value)%capacity;
  }
  
  return hash;
}
// loadFactor = numberOfItems/capacity;
class HashTable {
  table = new Array(3);
  numItems = 0;

  resizeTable(){
    const newTable = new Array(this.table.length * 2)
    for (let i=0; i < this.table.length; i++){
      if(this.table[i]){
        for(let k = 0; k < this.table[i].length; k++){
          const [key, value] = this.table[i][k];
          const index = hashFunc(key, newTable.length)
          if(newTable[index]){
            newTable[index].push([key, value])
          } else {
            newTable[index] = [[key, value]]
          }
        }
      }
    }
    return this.table = newTable
  }
  setItem (key, value) {
    this.numItems++;
    const loadFactor = this.numItems / this.table.length;
    if(loadFactor > 0.8){
      console.log('resizing now===')
      this.resizeTable()
    }
    const index = hashFunc(key, this.table.length)
    console.log(index)
    if(this.table[index]){
      this.table[index].push([key, value])
    } else {
      this.table[index] = [[key, value]]
    }
 
  };
  
  getItem = (key) => {
    const index = hashFunc(key, this.table.length)
    if(!this.table[index]){
      return null;
    }
    return this.table[index].find(x=> x[0] === key)[1];
  };
};

const hTable = new HashTable();
hTable.setItem("firstName", "Barry")
console.log(hTable.table.length)
hTable.setItem("lastName", "Allen")
console.log(hTable.table.length)
hTable.setItem("age", 30)
console.log(hTable.table.length)
hTable.setItem("dob", '1/2/3')
// hTable.setItem('status', 'single')
// hTable.setItem('location', 'Nigeria')
hTable.setItem("role", "SE")
console.log(hTable.table)
console.log(hTable.table.length)