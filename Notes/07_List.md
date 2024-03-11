## Lists and Methods in Python

Lists are fundamental data structures in Python used to store ordered collections of items. They are versatile and can hold elements of different data types (e.g., strings, numbers, even other lists). Here, we'll explore essential methods for creating, manipulating, and extracting information from lists.

**1. Creating Lists:**

There are two primary ways to create lists in Python:

* **Using square brackets (`[]`) and separating elements with commas:**

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3.14, 42]
mixed_list = ["hello", 10, True]
```

* **Using the `list()` constructor:**

```python
empty_list = list()  # Creates an empty list
another_list = list(fruits)  # Creates a copy of an existing list
```

**2. Accessing Elements:**

- **Indexing:** Elements in a list are accessed using zero-based indexing. The first element has an index of 0, the second is 1, and so on. Negative indexing starts from the end, with -1 referring to the last element.

```python
fruits = ["apple", "banana", "orange"]
first_fruit = fruits[0]  # Output: apple
last_fruit = fruits[-1]  # Output: orange
second_to_last_fruit = fruits[-2]  # Output: banana
```

- **Slicing:** Extracting a segment of the list using slice notation (`[start:end:step]`). `start` specifies the starting index (inclusive), `end` specifies the ending index (exclusive), and `step` defines the increment between elements (defaults to 1).

```python
fruits = ["apple", "banana", "orange", "mango"]
sublist = fruits[1:3]  # Output: ["banana", "orange"]
all_but_first = fruits[1:]  # Output: ["banana", "orange", "mango"]
first_two = fruits[:2]  # Output: ["apple", "banana"]
reverse_order = fruits[::-1]  # Output: ["mango", "orange", "banana", "apple"] (step of -1 reverses)
```

**3. Modifying Lists:**

* **Appending:** Use the `append()` method to add an element to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("orange")  # Modified list: ["apple", "banana", "orange"]
```

* **Inserting:** Use the `insert(index, element)` method to insert an element at a specific index.

```python
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "kiwi")  # Modified list: ["apple", "kiwi", "banana", "mango"]
```

* **Extending:** Use the `extend(iterable)` method to add all elements from an iterable (e.g., another list or tuple) to the end of the existing list.

```python
fruits = ["apple", "banana"]
new_fruits = ["orange", "mango"]
fruits.extend(new_fruits)  # Modified list: ["apple", "banana", "orange", "mango"]
```

* **Removing Elements:**
    - `remove(element)`: Removes the first occurrence of a specified element.
    - `pop(index=-1)`: Removes and returns the element at a given index (default is the last element).
    - `del list[index]`: Deletes the element at a specific index.

```python
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")  # Modified list: ["apple", "orange"]
removed_last = fruits.pop()  # Removed item: "orange", Modified list: ["apple"]
del fruits[0]  # Modified list: [] (empty list)
```

**4. Common List Methods:**

- **`clear()`:** Removes all elements from the list, leaving it empty.
- **`count(element)`:** Counts the number of occurrences of a specified element within the list.
- **`copy()`:** Creates a shallow copy of the list (changes to the copy won't affect the original).
- **`index(element, start=0, end=len(list))`:** Returns the index of the first occurrence of an element within the specified range. Raises a `ValueError` if not found.
- **`sort(key=None, reverse=False)`:** Sorts