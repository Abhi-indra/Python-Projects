# Numbers in Python

Numbers are fundamental building blocks in Python programming. They represent various numerical values and are used in calculations, comparisons, and other operations. Here's a breakdown of the primary numeric data types in Python:

**1. Integers (int):**

- Represent whole numbers (positive, negative, or zero).
- Example: `age = 25`
- Operations:
    - Arithmetic (+, -, *, /, //, %, **)
    - Comparison (==, !=, <, >, <=, >=)
    - Bitwise operations (&, |, ^, ~, <<, >>)

**2. Floating-Point Numbers (float):**

- Represent real numbers with decimal points.
- Example: `pi = 3.14159`
- Operations: Same as integers, with limitations on exact decimal representation due to computer storage.
- Be aware of potential rounding errors when working with very large or very small floating-point numbers.

**3. Complex Numbers (complex):**

- Represent numbers consisting of a real part and an imaginary part (denoted by `j`).
- Example: `z = 3 + 2j`
- Operations: Arithmetic specific to complex numbers (addition, subtraction, multiplication, division, conjugation, modulus).

**Illustrative Examples:**

**Integer Operations:**

```python
x = 10
y = 5

# Arithmetic operations
sum = x + y
difference = x - y
product = x * y
quotient = x / y  # Integer division (truncates towards zero)
remainder = x % y  # Modulo (remainder after division)
exponent = x ** y  # Exponentiation

# Comparison operations
is_equal = x == y
is_greater = x > y
is_less_than = x < y

print(sum, difference, product, quotient, remainder, exponent, is_equal, is_greater, is_less_than)
```

**Floating-Point Operations:**

```python
pi = 3.14159
radius = 5.0

# Calculate area of a circle
area = pi * radius**2

# Display result with two decimal places (formatted string)
print(f"Area of the circle: {area:.2f}")
```

**Complex Number Operations:**

```python
z1 = 3 + 2j
z2 = 4 - 1j

# Addition and subtraction
sum_complex = z1 + z2
difference_complex = z1 - z2

# Multiplication
product_complex = z1 * z2

# Conjugate (flips the sign of the imaginary part)
conjugate_z1 = z1.conjugate()

print(sum_complex, difference_complex, product_complex, conjugate_z1)
```

**Choosing the Right Number Type:**

- Use `int` for whole numbers when exact values are needed.
- Use `float` for real numbers with decimals, keeping in mind potential rounding errors.
- Use `complex` for calculations involving imaginary numbers.

By understanding these concepts, you'll be well-equipped to effectively work with numbers in your Python programs.

I'd be glad to provide a clear explanation of the differences between `repr`, `str`, and `print` in Python, incorporating examples and adhering to GitHub markdown formatting for clarity:

# Distinguishing `repr`, `str`, and `print` in Python

In Python, these three functions deal with how objects are represented in output, but they serve distinct purposes:

**1. `repr` (Representation):**

- Returns a string representation of an object that can be used to recreate the object.
- Often uses minimal formatting for readability within code.
- Syntax: `object_name.__repr__()` (you usually don't call it directly).

**Example:**

```python
my_list = [1, 2, 3]
my_string = "hello"

list_repr = repr(my_list)   # Output: '[1, 2, 3]'
string_repr = repr(my_string) # Output: "'hello'"
```

**2. `str` (String Conversion):**

- Returns a human-readable string representation of an object.
- Aims for clarity and may include more formatting than `repr`.
- Syntax: `object_name.__str__()` (you usually don't call it directly).

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)

person_str = str(person)  # Output: "Name: Alice, Age: 30"
```

**3. `print` (Output Function):**

- Prints the string representation of an object to the console, followed by a newline character by default.
- Syntax: `print(object_name)`

**Example:**

```python
print(my_list)   # Output: [1, 2, 3]
print(my_string)  # Output: hello
print(person)     # Output: Name: Alice, Age: 30 (assuming __str__ is defined)
```

**Key Differences:**

| Feature        | `repr`                                               | `str`                                            | `print`                                                  |
|----------------|---------------------------------------------------|---------------------------------------------------|----------------------------------------------------------|
| Purpose         | Object recreation                                   | Human-readable string representation              | Console output                                             |
| Formatting      | Minimal (for code readability)                     | More readable, may include custom formatting     | Default formatting (newline at the end)                 |
| User Invocation | Usually not called directly                        | Usually not called directly                        | Called directly for console output                         |

**Choosing the Right Function:**

- Use `repr` when you need to create a string representation of an object that can be used to reconstruct it later (e.g., debugging or serialization).
- Use `str` when you need a human-readable string representation of an object for display or output purposes.
- Use `print` when you want to display an object's value directly to the console.

By understanding these distinctions, you can effectively control how objects are represented in your Python programs.

I'd be glad to provide a clear and concise explanation of sets in Python, incorporating examples and adhering to GitHub markdown formatting for readability:

# Sets in Python

Sets are unordered collections of unique elements in Python. They are useful when you need to:

- Remove duplicate elements from a list.
- Check if an element is present in a collection.
- Perform set operations like union, intersection, and difference.

**1. Creating Sets:**

There are two primary ways to create sets in Python:

- **Set literal:** Use curly braces `{}` to enclose elements.
    ```python
    my_set = {1, 2, 3, "apple"}  # Elements can be of different data types
    ```
- **`set()` function:** Convert an iterable (list, tuple, string) into a set, removing duplicates.
    ```python
    duplicate_list = [1, 2, 2, 3, 4]
    unique_set = set(duplicate_list)
    print(unique_set)  # Output: {1, 2, 3, 4}
    ```

**2. Key Characteristics:**

- Sets are unordered: Elements don't have a specific order, and the order might change between operations.
- Sets are mutable: You can add, remove, or modify elements after creation.
- Sets can only contain unique elements: Duplicate elements are automatically discarded.
- Sets must be hashable: Elements cannot be mutable objects like lists or dictionaries.

**3. Common Set Operations:**

* **Membership (`in`):** Check if an element exists in a set.
    ```python
    my_set = {1, 2, 3}
    is_present = 2 in my_set  # True
    ```
* **Union (`|`):** Combine elements from two sets, retaining all unique elements.
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    combined_set = set1 | set2
    print(combined_set)  # Output: {1, 2, 3, 4, 5}
    ```
* **Intersection (`&`):** Find elements that are common to both sets.
    ```python
    set1 = {1, 2, 3}
    set2 = {2, 4, 5}
    common_elements = set1 & set2
    print(common_elements)  # Output: {2}
    ```
* **Difference (`-`):** Find elements in the first set that are not in the second.
    ```python
    set1 = {1, 2, 3}
    set2 = {2, 4, 5}
    differences = set1 - set2
    print(differences)  # Output: {1, 3}
    ```

**4. Additional Set Methods:**

* **`add(element)`:** Add a new element to a set.
* **`remove(element)`:** Remove an element from a set (raises an error if not found).
* **`discard(element)`:** Remove an element (silently ignores if not found).
* **`pop()`:** Remove and return an arbitrary element from the set.
* **`clear()`:** Remove all elements from the set.

**Example: Finding Unique Words in a String:**

```python
text = "This is a string with some duplicate words."
unique_words = set(text.split())  # Convert text to a list of words, then create a set
print(unique_words)  # Output: {'This', 'a', 'is', 'string', 'with', 'some', 'duplicate', 'words.'}
```

By understanding sets in Python, you can effectively store and manipulate collections of unique elements, enhancing the efficiency and accuracy of your programs.

I'd be glad to provide a clear and concise explanation of Boolean data types in Python, incorporating examples and adhering to GitHub markdown formatting for readability:

# Booleans in Python

Booleans, also known as Boolean values, are fundamental building blocks in Python. They represent logical truths or falsities, forming the basis for conditional statements and decision-making in your code.

**1. Values:**

There are only two possible Boolean values in Python:

- `True`: Represents a logical truth (affirmative).
- `False`: Represents a logical falsehood (negative).

**2. Examples:**

```python
is_raining = True
x > 0  # Evaluates to True if x is a positive number
is_empty = list1 == []  # Checks if list1 is empty
```

**3. Operations:**

Boolean values primarily engage in logical operations, allowing you to combine conditions and make logical decisions in your code. Here's a breakdown of the key logical operators:

**- `and`:** Returns `True` only if both operands are `True`.
  - Example: `is_morning and is_sunny` (True only if it's both morning and sunny)

**- `or`:** Returns `True` if at least one operand is `True`.
  - Example: `is_hungry or is_thirsty` (True if either hungry or thirsty)

**- `not`:** Negates the truth value of an operand.
  - Example: `not is_finished` (True if not finished)

**4. Conditional Statements:**

Booleans are crucial for writing conditional statements, enabling your code to execute different blocks based on specific conditions. Python provides the following conditional statements:

**- `if`:** Executes a block of code if a condition is `True`.
  ```python
  if is_raining:
      print("Bring an umbrella!")
  ```

**- `elif`:** Provides optional alternative conditions after an `if` statement.
  ```python
  if temperature > 30:
      print("It's hot!")
  elif temperature < 10:
      print("It's cold!")
  else:
      print("The temperature is moderate.")
  ```

**- `else`:** Executes a block of code if none of the previous conditions are `True`.

**5. Conversion:**

Certain values can be implicitly converted to `True` or `False` in Python:

- Non-zero numbers, non-empty strings, and lists/tuples with elements are converted to `True`.
- Zero, the empty string (`""`), empty lists/tuples (`[]`, `()`) are converted to `False`.

However, it's generally recommended to use explicit comparisons (`==`, `!=`) for clarity and to avoid unexpected behavior.

**6. Summary:**

By mastering Booleans and their operations, you can guide the flow of your Python programs, make informed decisions based on various conditions, and build robust control structures within your code.