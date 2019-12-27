/*
Lilah has a string, , of lowercase English letters that 
she repeated infinitely many times.
Given an integer, , find and print the number of letter a's in the first  
n letters of Lilah's infinite string.
*/
function repeatedString(s, n) {
  // let count = 0;
  const unique = new Set(s);
  const item = [...unique];

  if (item.length === 1 && item[0] === 'a') {
    count = n;
  }
  const numbersOfAs = s => {
    let count = 0;

    for (let i = 0; i < s.length; i++) {
      if (s[i] === 'a') count++;
    }

    return count;
  };

  const lengthOfStr = s.length;
  const numOfAsInInputString = numbersOfAs(s);

  if (n % lengthOfStr === 0) return numOfAsInInputString * (n / lengthOfStr), (n / lengthOfStr);

  const stringInRepeatedSting = Math.floor(n / lengthOfStr);
  const stringRemaining = n % lengthOfStr;
  const aInRem = numbersOfAs(s.slice(0, stringRemaining));

  return numOfAsInInputString * stringInRepeatedSting + aInRem, lengthOfStr, stringInRepeatedSting;
}

console.log(
  repeatedString(
    'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm',
    736778906400
  )
);
console.log(
  repeatedString(
    'abcac',
    10
  )
);
51574523448;
