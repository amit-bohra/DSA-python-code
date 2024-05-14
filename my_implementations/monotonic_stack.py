def next_greater(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_greater_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_smaller(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_smaller_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def prev_greater(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    return result

def prev_greater_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            result[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    return result

def prev_smaller(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    return result

def prev_smaller_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            result[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    return result

# Example usage:
arr = [3, 1, 4, 6, 5, 2, 8, 7, 10, 9]
n = len(arr)

print('arr', arr)

print("Next greater elements:", next_greater(arr, n))
print("Next greater or equal elements:", next_greater_equal(arr, n))
print("Next smaller elements:", next_smaller(arr, n))
print("Next smaller or equal elements:", next_smaller_equal(arr, n))
print("Previous greater elements:", prev_greater(arr, n))
print("Previous greater or equal elements:", prev_greater_equal(arr, n))
print("Previous smaller elements:", prev_smaller(arr, n))
print("Previous smaller or equal elements:", prev_smaller_equal(arr, n))


def next_greater(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_greater_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_smaller(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def next_smaller_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

def prev_greater(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            result[i] = arr[stack[-1]]
            stack.append(i)
            break
        if not stack:
            stack.append(i)
    return result

def prev_greater_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            result[i] = arr[stack[-1]]
            stack.append(i)
            break
        if not stack:
            stack.append(i)
    return result

def prev_smaller(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            result[i] = arr[stack[-1]]
            stack.append(i)
            break
        if not stack:
            stack.append(i)
    return result

def prev_smaller_equal(arr, n):
    stack = []
    result = [-1] * n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            result[i] = arr[stack[-1]]
            stack.append(i)
            break
        if not stack:
            stack.append(i)
    return result

# Example usage:
arr = [3, 1, 4, 6, 5, 2, 8, 7, 10, 9]
n = len(arr)

print("Next greater elements:", next_greater(arr, n))
print("Next greater or equal elements:", next_greater_equal(arr, n))
print("Next smaller elements:", next_smaller(arr, n))
print("Next smaller or equal elements:", next_smaller_equal(arr, n))
print("Previous greater elements:", prev_greater(arr, n))
print("Previous greater or equal elements:", prev_greater_equal(arr, n))
print("Previous smaller elements:", prev_smaller(arr, n))
print("Previous smaller or equal elements:", prev_smaller_equal(arr, n))
