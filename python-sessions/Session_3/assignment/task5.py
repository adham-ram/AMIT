def perfect_numbers(n):
    perfect_nums = []
    for num in range(1, n + 1):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            perfect_nums.append(num)
    return perfect_nums
perfect_numbers_list = perfect_numbers(10000)
print(f"Perfect numbers up to 10000: {perfect_numbers_list}")