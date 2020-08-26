def add_nums(num, *nums):
    total = sum(nums, num)

    nums_joined = ', '.join([str(n) for n in nums])
    print(f"The sum of {nums_joined} and {num} is {total}.")

def main():
    add_nums(1, 2)
    add_nums(1, 2, 3, 4, 5)
    add_nums(11, 12, 13, 14)
    add_nums(101, 201, 301)

main()