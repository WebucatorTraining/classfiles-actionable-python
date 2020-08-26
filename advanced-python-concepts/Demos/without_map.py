def multiply(x, y):
    return x * y

def main():
    nums1 = range(0, 10)
    nums2 = range(10, 0, -1)

    multiples = []
    for i in range(len(nums1)):
        multiple = multiply(nums1[i], nums2[i])
        multiples.append(multiple)

    for multiple in multiples:
        print(multiple)

main()