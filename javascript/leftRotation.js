function rotLeft(a, d) {
  while (d > 0) {
    let first = a.shift();
    a.push(first);
    d -= 1;
  }
  return a;
}

console.log(rotLeft([1, 2, 3, 4, 5], 4));
