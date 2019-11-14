#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
  a = 0 #O(1)
    while (a < n * n * n): #O(n) ==> O(n)
      a = a + n * n #O(1) * O(n) ==> O(n)
```

O(1) + O(n) + O(n) ==> O(2n) ==> O(n)
The above has a linear runtime i.e `O(n)`.
No matter the size of `n` the `while loop` iteration multiplies and increases the number `comparison` and returns a `single value` which is `a` till the set condition is met.
Ingoring all constants the runtime is the runtime of the `while loop`

b)

````
sum = 0 #O(1)
    for i in range(n): #O(n)
      j = 1 #O(1) * #O(n) ==> #O(n)
      while j < n: # O(n)
        ```
        j *= 2 #O(log) * #O(n) ==> O(log n) * O(n) ==> O(nlogn)
        sum += 1
        #==> O(nlogn)
        ```
````

`O(nlogn)`
The above has a linear runtime of `O(nlogn)`.
As n increases the number of iterations of the `for loop` increases and since the `while` is nested inside a loop its BigO is `O(n) * O(n)`. Ingoring all constants the runtime is the runtime of the`for loop`time the runtime of the`while loop`

c)

```
def bunnyEars(bunnies):
      if bunnies == 0: #O(1)
        return 0 #O(1)

      return 2 + bunnyEars(bunnies-1) #O(n) + 2 ==> O(n)
```

O(1) + O(1) + O(n) ==> `O(n)`

The above has a linear runtime since it is recursive and will loop till the user input gets to `zero`

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

STEPS:

1. Get the range of the n-story
2. Get a the median of the range of n-story
3. Set median as `f` which is our pivot
4. Loop through the range of n-story.
   a. Eggs dropped from `f` or ranges above or equal to `f` add to `Broken eggs array`
   a. Eggs dropped from `f` or ranges below `f` add to `Not Broken eggs array`
5. Get the length of `Not Broken eggs array` and `Broken eggs array`
6. If the `Broken eggs array` is greater than `Not Broken eggs array`
   then move `f` higher i.e `f` + 1 and repeat Step 1 to 5
7. If the `Broken eggs array` is less than `Not Broken eggs array`
   then `f` is optimal and stop

   ```
   uses binary sort
   O(logn)
