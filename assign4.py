class FibonacciCalculator:
    def __init__(self, n):
        self.n = n

    def calculate_fibonacci(self):
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1

        fib_sequence = [0] * (self.n + 1)
        fib_sequence[1] = 1

        for i in range(2, self.n + 1):
            fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

        return fib_sequence[self.n]

    def display_result(self):
        result = self.calculate_fibonacci()
        print(f"The {self.n}th Fibonacci number is: {result}")


if __name__ == "__main__":
    number = int(input("Enter the value of n: "))
    calculator = FibonacciCalculator(number)
    calculator.display_result()