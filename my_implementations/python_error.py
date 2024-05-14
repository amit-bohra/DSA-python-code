# Common Python Errors and Examples

# 1. SyntaxError
try:
    # SyntaxError: invalid syntax
    print "Hello, World!"
except SyntaxError as e:
    print("SyntaxError:", e)

# 2. IndentationError
try:
    def my_function():
    print("Hello, World!")
except IndentationError as e:
    print("IndentationError:", e)

# 3. NameError
try:
    # NameError: name 'x' is not defined
    print(x)
except NameError as e:
    print("NameError:", e)

# 4. TypeError
try:
    # TypeError: can only concatenate str (not "int") to str
    result = "Hello, " + 123
except TypeError as e:
    print("TypeError:", e)

# 5. ValueError
try:
    # ValueError: invalid literal for int() with base 10: 'abc'
    number = int('abc')
except ValueError as e:
    print("ValueError:", e)

# 6. IndexError
try:
    # IndexError: list index out of range
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print("IndexError:", e)

# 7. KeyError
try:
    # KeyError: 'c'
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError as e:
    print("KeyError:", e)

# 8. AttributeError
try:
    # AttributeError: 'list' object has no attribute 'appendx'
    my_list = []
    my_list.appendx(1)
except AttributeError as e:
    print("AttributeError:", e)

# 9. FileNotFoundError (IOError in Python 2)
try:
    # FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# 10. ImportError
try:
    # ImportError: No module named 'nonexistent_module'
    import nonexistent_module
except ImportError as e:
    print("ImportError:", e)

# 11. ZeroDivisionError
try:
    # ZeroDivisionError: division by zero
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# 12. TypeError (missing arguments)
try:
    # TypeError: my_function() missing 1 required positional argument: 'b'
    def my_function(a, b):
        return a + b

    my_function(1)
except TypeError as e:
    print("TypeError (missing arguments):", e)

# 13. TypeError (unsupported operation)
try:
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    result = 123 + "abc"
except TypeError as e:
    print("TypeError (unsupported operation):", e)

# 14. TypeError (not iterable)
try:
    # TypeError: 'int' object is not iterable
    for i in 123:
        print(i)
except TypeError as e:
    print("TypeError (not iterable):", e)

# 15. KeyboardInterrupt
try:
    # KeyboardInterrupt
    while True:
        pass
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")

