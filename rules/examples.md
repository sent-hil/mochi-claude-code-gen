# Example 1

What's the splat operator?
---
`*`
---
How can it be used when calling a method?
---
It expands arrays into individual elements when calling a method.


```python
a = [1,2,3]


def b(c,d,e):
  print(c,d,e)


b(a) # =>  b() missing 2 required positional arguments: 'd' and 'e;
b(*a) # => 1,2,3
```
---
How can splat operator be used in methods definition?
---
It can be used to collect remaining arguments passed to method into an array


```python
def my_method(arg1, *other_args):
  print(f"First argument: {arg1}")
  print(f"Other arguments: {other_args}")


my_method(1, 2, 3, 4)
# Output:
# First argument: 1
# Other arguments: (2, 3, 4)
```
---
What's the class of `other_args` in above example?
---
Tuple.
---
Given two arrays:
```python
array1 = [1, 2, 3]
array2 = [4, 5, 6]
```


How do you merge them together?
---
`[*array1, *array2]`

---
---
# Example 2

What is reciprocal of n?
---
$\Large \frac{1}{n}$
---
What's another name for it?
---
Multiplicative Inverse.
---

---
---
# Example 3

Using `np` how can you create this array: `array([0, 1, 2, 3])`
---
```python
np.arange(4)
```
---
How about `array([[0, 1, 2],[3, 4, 5]])` ?
---
```python
np.arange(6).reshape((2,3))
```
---
How about:
```
# array([[0, 1, 2, 3, 4, 5],
#       [0, 1, 2, 3, 4, 5],
#       [0, 1, 2, 3, 4, 5]])
```
---
```python
arr = np.arange(6)
np.broadcast_to(arr, (3,6))
```
