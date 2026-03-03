
# Algorithmic Efficiency & Recursion Toolkit (AERT)


# Part A: Stack ADT
class StackADT:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)



# Part B: Factorial (Recursive)


def factorial(n):
    if n < 0:
        return "Invalid input (n must be >= 0)"
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Fibonacci (Naive + Memo)


naive_calls = 0
memo_calls = 0


def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# Part C: Tower of Hanoi


def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)


# Part D: Recursive Binary Search


def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)  # store mid index visited

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)



# Main Function (All Test Cases)


def main():
    print("AERT TOOLKIT OUTPUT\n")

    # Factorial Tests 
    print("Factorial Tests:")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) = {factorial(n)}")

    #  Fibonacci Tests
    print("\nFibonacci Tests (Naive vs Memoized):")

    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls
        naive_calls = 0
        memo_calls = 0

        naive_result = fib_naive(n)
        naive_count = naive_calls

        memo_calls = 0
        memo_result = fib_memo(n, {})
        memo_count = memo_calls

        print(f"\nn = {n}")
        print(f"Naive Fibonacci = {naive_result}, Calls = {naive_count}")
        print(f"Memoized Fibonacci = {memo_result}, Calls = {memo_count}")

    # Tower of Hanoi 
    print("\nTower of Hanoi (N = 3):")
    hanoi_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', hanoi_stack)

    while not hanoi_stack.is_empty():
        print(hanoi_stack.pop())

    # Binary Search
    print("\nBinary Search Tests:")
    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        bs_stack = StackADT()
        index = binary_search(arr, key, 0, len(arr) - 1, bs_stack)
        print(f"\nSearch key = {key}")
        print(f"Index = {index}")
        print(f"Mid indices visited = {bs_stack}")

    # Empty array test
    empty_arr = []
    bs_stack = StackADT()
    index = binary_search(empty_arr, 5, 0, len(empty_arr) - 1, bs_stack)
    print("\nEmpty Array Search:")
    print(f"Index = {index}")


if __name__ == "__main__":
    main()