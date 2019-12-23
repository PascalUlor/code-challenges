Array.prototype.reduce = function(cb, accumulator) {
  this.forEach((item, index) => {
    accumulator = cb(accumulator, item, index, this);
  });
  return accumulator;
};
