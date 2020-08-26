def multiply(x, y):
    return x * y

def main():
    nums1 = range(0, 10)
    nums2 = range(10, 0, -1)

    multiples = map(multiply, nums1, nums2)

    for multiple in multiples:
        print(multiple)

main()