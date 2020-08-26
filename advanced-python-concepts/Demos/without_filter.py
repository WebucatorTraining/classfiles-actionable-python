def is_odd(num):
    return num % 2

def main():
    nums = range(0, 10)

    odd_nums = []
    for num in nums:
        if is_odd(num):
            odd_nums.append(num)

    for num in odd_nums:
        print(num)

main()