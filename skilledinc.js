// asdf => false
// aabb => baab => true
// raaccer => racecar => true
// bbc => bcb => true
// qwero => false
// aacccddbbb => false

const checkPalindrom = str => {
  //get the number of occurrence of each character
  // create a counter to log number of occurrnce of charaters
  // cache number of occurrence of each character
  // if  all char occur is even or odd occur not > 1 return true
  // else false
  const countedCharacter = {};
  for (let i = 0; i < str.length; i++) {
    if (str[i] in countedCharacter) {
      countedCharacter[str[i]] = countedCharacter[str[i]] + 1;
    }

    countedCharacter[str[i]] = 1;
  }

  let oddCharacterCount = 0;
  let counts = Object.values(countedCharacter);
  counts.forEach(charCount => {
    if (charCount % 2 !== 0) {
      oddCharacterCount++;
    }
  });

  return oddCharacterCount <= 1;
};

// Input
// flightLength: duration of the flight in minutes (integer)
// movieLengths: array of movie times in minutes (array of integers)
// Output
// boolean, true if there exists TWO movies that add up EXACTLY to the flightLength
// Examples
// flightLength 160
// [80, 110, 40] => false
// [80, 110, 80] => true
// [20, 30, 110, 40, 50] => true

// { 20, 30, 110, 40,
const flightMovies = (moviesArr, flightTime) => {
  seenMovies = new Set();
  for (let i = 0; i < moviesArr.length; i++) {
    let TimeMovie1 = moviesArr[i];
    let TimeMovie2 = flightTime - TimeMovie1;

    if (seenMovies.has(TimeMovie2)) {
      return true;
    }

    seenMovies.add(TimeMovie1);
  }

  return false;
};
