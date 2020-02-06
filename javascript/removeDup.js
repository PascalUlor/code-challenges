    /** Build on the solution we got in class by writing function that takes an
     * array (list) as an input parameter and outputs an array (list) of all the
     * items in the list that were duplicates. Eg. getDuplicates([e,b,c,b,c,a])
     * would return [b,c] or [c,b]. The order of the duplicates in your output
     * is not important. BONUS: Modify the function so that it outputs the
     * original input list without the duplicates. Eg.
     * removeDuplicates([e,b,c,b,c,a]) would return [e,b,c,a].*/
  var num = ['e','b','c','b','c','a'];

function getDuplicate(array){
	let cache = {};

  for( let i = 0; i < array.length; i++) {
    if (array[i] in cache) {
      cache[array[i]] = cache[array[i]] + 1;
    } else {
      cache[array[i]] = 1;
    }    
  }

  let duplicates = [];
  let cacheKeys = Object.keys(cache);
  
  for(let j = 0; j < cacheKeys.length; j++){
    if(cache[cacheKeys[j]] > 1) {
      duplicates.push(cacheKeys[j])
    }
  }
  return duplicates
}

function removeDuplicates(array){
	let cache = {};

  for( let i = 0; i < array.length; i++) {
    if (array[i] in cache) {
      cache[array[i]] = cache[array[i]] + 1;
    } else {
      cache[array[i]] = 1;
    }    
  }

  let uniques = [];
  let unique = []
  let cacheKeys = Object.keys(cache);
  
  for(let j = 0; j < cacheKeys.length; j++){
    if(cache[cacheKeys[j]] === 1) {
      uniques.push(cacheKeys[j])
    }
  }
  return uniques;
}

getDuplicate(num)
removeDuplicates(num)
