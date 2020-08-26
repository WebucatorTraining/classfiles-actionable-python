def is_odd(num):
    return num % 2

def main():
    nums = range(0, 10)

    odd_nums = filter(is_odd, nums)
    
    for num in odd_nums:
        print(num)

main()