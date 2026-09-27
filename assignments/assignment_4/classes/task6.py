class PerfectNumbers:
    def __init__(self, limit):
        self.limit = limit

    def _is_perfect(self, num):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        return divisors_sum == num

    def generate(self):
        return [num for num in range(1, self.limit + 1) if self._is_perfect(num)]


perfect_numbers = PerfectNumbers(10000)
print(f"Perfect numbers up to 10000: {perfect_numbers.generate()}")