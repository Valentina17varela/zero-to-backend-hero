# 📘 Data Structures and Algorithms - University of Helsinki - Week 2

---

## 📝 Overview

The aim of the course Data Structures and Algorithms is to advance your programming skills and teach you techniques and ways of thinking that help you in implementing programs that are correct and efficient in all circumstances.


## 📚  Notes

## List
The memory of a computer consists of a sequence of memory locations capable of storing data. Each memory location has an address that can be used for access. When a program is executed, the data it processes is stored in the memory.


```python
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99

100	101	102	103	104	105	106	107	108	109	110
7	-3	1	2	3	1	2	0	0	0	99
a	b	c	 	 	 	 	 	 	 	d

```

The elements of the list are stored in consecutive memory locations, which makes it easy to determine the location of a given list element. The memory address of an element is obtained by adding the element index to the address of the first element.

## List operations
Knowing the time complexities of the list operations is important for algorithm design, because they determine which operations can be used as components of an efficient algorithm. Most list operations have one of the following time complexities:

- O(1): the operation is always efficient independent of the size of the list
- O(n): the efficiency depends on the size of the list and the operation can be slow for large lists

### Indexing
The elements of a list can be accessed and modified using the index operator [].
```python
numbers = [4, 3, 7, 3, 2]
print(numbers[2]) # 7
numbers[2] = 5
print(numbers[2]) # 5
```
The access or modification needs O(1) time, because the elements are in consecutive memory locations and the address of an element can be computed quickly.

### List size
The function len tells how many elements the list contains:
```python
numbers = [4, 3, 7, 3, 2]
print(len(numbers)) # 5
```
The function needs O(1) time, because the length is stored in memory with the list.

### Searching
The operator in tells if a given element is on the list or not. The method index returns the index of the first occurrence of the element on the list. The method count counts the occurrences of the element on the list.
```python
numbers = [4, 3, 7, 3, 2]

print(3 in numbers) # True
print(8 in numbers) # False

print(numbers.index(3)) # 1
print(numbers.count(3)) # 2
```
All of these operations need O(n) time, because they have to scan through the list. Notice that some of the operations can be fast in some situations. For example, if the element we are searching for is in the beginning of the list, the operator in is fast since it can stop immediately after finding the element. However, in the worst case the element is not on the list and the operation has to go through the whole list to verify this.

### Adding an element
The method append adds an element to the end of the list, and the method insert adds an element to a given position on the list.
```python
numbers = [1, 2, 3, 4]

numbers.append(5)
print(numbers) # [1, 2, 3, 4, 5]

numbers.insert(1, 6)
print(numbers) # [1, 6, 2, 3, 4, 5]
```
The time complexities of these operations are affected by the way the elements are stored in memory. In this case, the contents of the memory before additions look something like this:

```python
100	101	102	103	104	105	106	107
1	2	3	4	0	0	0	0
```
The method append needs O(1) time, because adding an element to the end of a list does not require changes to other memory locations. In the example, the element 5 is stored in the memory location 104:

```python
100	101	102	103	104	105	106	107
1	2	3	4	5	0	0	0
```
If the memory area reserved for the list is already full and there is no room for the new element, more work is required. In such a case, a new bigger memory area is reserved for the list and all elements are moved to the new area, which needs O(n) time.

The method insert has time complexity O(n) because, when an element is added to somewhere else than the end of the list, other elements need to be moved forward to make room for the new element. In our example, when the element 6 is inserted to the index 1, the elements are relocated as follows:

```python
100	101	102	103	104	105	106	107
1	6	2	3	4	5	0	0
```
Notice however, that the methdod insert is efficient when the element is inserted somewhere near the end of the list, because only a small number of elements needs to be relocated.

### Removing an element
The method pop removes an element from a list. If the method is called without a parameter, it removes the last element. If a parameter is given, the operation removes the element at the specified index.

```python
numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()
print(numbers) # [1, 2, 3, 4, 5]

numbers.pop(1)
print(numbers) # [1, 3, 4, 5]
```

Let us again consider how removing an element affects the contents of the memory. Before the removes, the contents of the memory look something like this:

```python
100	101	102	103	104	105	106	107
1	2	3	4	5	6	0	0
```
As with adding, removing an element at the end of a list takes O(1) time, because the other elements are not affected. After removing the element 6, the memory might look like this:

```python
100	101	102	103	104	105	106	107
1	2	3	4	5	0	0	0
```
Removing an element in the middle of a list needs O(n) time, because now all the following elements have to be relocated in memory. Removing the element 2 has the following effect on the contents of the memory:

```python
100	101	102	103	104	105	106	107
1	3	4	5	0	0	0	0
```
Python also has a list method remove that removes the first occurrence of a given element:

```python
numbers = [1, 2, 3, 1, 2, 3]

numbers.remove(3)
print(numbers) # [1, 2, 1, 2, 3]
```
The time complexity of the method is always O(n), because it first has to find the first occurrence (similarly to the method index), and then remove the element and relocate the following elements.

### References and copying
Assigning a list to a variable only copies the reference, not the contents of the list. Here executing the line b = a causes the variables a and b to refer to the same list in memory. When a new element is added to the list a, the same addition happens to the list b:
```python
a = [1, 2, 3, 4]
b = a
a.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
```

For copying the contents, we can use the method copy:
```python
a = [1, 2, 3, 4]
b = a.copy()
a.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4]
```
Now the variables a and b refer to separate lists, and adding an element to the list a has no effect on the contents of the list b.

There is a big difference in the efficiency of the above operations: copying a reference takes O(1) time, while copying the contents needs O(n) time. Thus the line b = a takes O(1) time, and the line b = a.copy() takes O(n) time.

> [!NOTE]  
> When a function is given a data structure as a parameter, only a reference is copied. Then the function can cause side effects, if it changes the contents of the data structure. This is not good when the intention is to create a new list without changing the original list. The function can be corrected with the method copy

### Slicing and concatenation
The Python slice operator ([:]) creates a new list that contains a copy of a segment of the given list:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6]) # [3, 4, 5, 6]
```
This operator needs O(n) time because it copies the contents from the old list to the new list.

And the operator + can be used for concatenating lists:
```python
first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second) # [1, 2, 3, 4, 5, 6, 7, 8]
```
This takes O(n) time, because the operator copies the elements from the original lists to the new list.



## Summary
| Operation | Time complexity |
|---|---|
| Indexing (`[]`) | O(1) |
| Size (`len`) | O(1) |
| Is element on list? (`in`) | O(n) |
| Searching (`index`) | O(n) |
| Counting (`count`) | O(n) |
| Adding to end (`append`) | O(1) |
| Adding to middle (`insert`) | O(n) |
| Removing from end (`pop`) | O(1) |
| Removing from middle (`pop`) | O(n) |
| Searching and removing (`remove`) | O(n) |
| Reference (`b = a`) | O(1) |
| Copy (`b = a.copy()`) | O(n) |
| Slicing (`array[:]`) | O(n) |
| Concatenation (`+`) | O(n) |



## 🔗 Resources

- [Course](https://tira.mooc.fi/spring-2025)
