function repeatedString(s, n) {
  // let count = 0;
  const unique = new Set(s);
  const item = [...unique];
  // if (item.length === 1 && item[0] === 'a') {
  //   count = n;
  // } else {
  //   const check = x => {
  //     for (let i = 0; i < x.length; i += 1) {
  //       if (x[i] === 'a') {
  //         count += 1;
  //       }
  //     }
  //     return count;
  //   };

  //   const lengthOfStr = s.length;
  //   const numOfAsInInputString = check(s);
  //   if (n % lengthOfStr === 0) return numOfAsInInputString * (n / lengthOfStr);

  //   let stringInRepeatedString = Math.floor(n / lengthOfStr);
  //   let stringRemaining = n % lengthOfStr;
  //   let aInRem = numbersOfAs(s.slice(0, stringRemaining));
  // }
  // return numOfAsInInputString * stringInRepeatedString + aInRem;

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

  if (n % lengthOfStr === 0) return numOfAsInInputString * (n / lengthOfStr);

  const stringInRepeatedSting = Math.floor(n / lengthOfStr);
  const stringRemaining = n % lengthOfStr;
  const aInRem = numbersOfAs(s.slice(0, stringRemaining));

  return numOfAsInInputString * stringInRepeatedSting + aInRem;
}

console.log(
  repeatedString(
    'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm',
    736778906400
  )
);
51574523448;
