# gp-cseu2-P1D2
the guided project for python I day 2

## Some student Solutions for Centered Average
*Ikechukwu Eze*
```python
def centered_average_with_sorting(arr):
    return int(sum(sorted(arr)[1:-1])/(len(arr) - 2))


def centered_average(arr):
    return int(sum(arr[1:-1])/(len(arr) - 2))
```


*Ezekiel Ekunola*
```python
def centered_average(list):
    sortList = sorted(list)
    sortList.pop(0)
    sortList.pop(len(sortList)  -1)
    sum = 0
    for element in sortList:
        sum += element

    average = sum / len(sortList)
    return average
```


*Aaron Thompson*
```python
import functools 

def centered_average(list):
  copy = list[:]
  copy.sort()
  copy = copy[1:-1]
  total = functools.reduce(lambda a,b : a+b,copy)
  return total / len(copy)
```


*Shola Ayeni*
```python
def centered_average(lst):
    # Sort list
    # get min and max
    minNum = min(lst)
    maxNum = max(lst)

    #remove min and max

    lst.remove(minNum)
    lst.remove(maxNum)

    # find length
    length = len(lst)

    sum_list = sum(lst)

    avg = (sum_list/length)
    return avg
```


*Nabeelah Yousuph*
```python
def centered_average(arr):
    x = sorted(arr)
    y = x[1: len(arr)-1]
    print(y)
    return sum(y)/len(y)
```


*Jakub Maleta*
```python
def centered_average(arr):
  centeredArray = sorted(arr)[1:-1]
  return sum(centeredArray) / (len(centeredArray))
```


