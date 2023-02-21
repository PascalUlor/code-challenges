/*
 * @lc app=leetcode id=155 lang=javascript
 *
 * [155] Min Stack
 *
 * https://leetcode.com/problems/min-stack/description/
 *
 * algorithms
 * Medium (50.82%)
 * Likes:    10846
 * Dislikes: 712
 * Total Accepted:    1.2M
 * Total Submissions: 2.3M
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 * 
 * Implement the MinStack class:
 * 
 * 
 * MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
 * 
 * 
 * You must implement a solution with O(1) time complexity for each
 * function.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input
 * ["MinStack","push","push","push","getMin","pop","top","getMin"]
 * [[],[-2],[0],[-3],[],[],[],[]]
 * 
 * Output
 * [null,null,null,null,-3,null,0,-2]
 * 
 * Explanation
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin(); // return -3
 * minStack.pop();
 * minStack.top();    // return 0
 * minStack.getMin(); // return -2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * -2^31 <= val <= 2^31 - 1
 * Methods pop, top and getMin operations will always be called on non-empty
 * stacks.
 * At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
 * 
 * 
 */

// @lc code=start

var MinStack = function() {
    this.stack = [];
    this.topIndex = -1;
    this.min = Number.MAX_SAFE_INTEGER;
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack[this.topIndex += 1] = this.min;
    this.stack[this.topIndex += 1] = val;
    val < this.min && (this.min = val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.min = this.stack[this.topIndex -= 1];
    this.topIndex -= 1;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.topIndex];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.min;
};

// var MinStack = function() {
//     this.elements = [];
//   };
  
//   /**
  
//    @param {number} x
//    @return {void}
//    */
//   MinStack.prototype.push = function(x) {
//     this.elements.push({
//       value: x,
//       min: this.elements.length === 0 ? x : Math.min(x, this.getMin()),
//     });
//   };
//   /**
  
//    @return {void}
//    */
//   MinStack.prototype.pop = function() {
//     this.elements.pop();
//   };
//   /**
  
//    @return {number}
//    */
//   MinStack.prototype.top = function() {
//     return this.elements[this.elements.length - 1].value;
//   };
//   /**
  
//    @return {number}
//    */
//   MinStack.prototype.getMin = function() {
//     return this.elements[this.elements.length - 1].min;
//   };

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @lc code=end

