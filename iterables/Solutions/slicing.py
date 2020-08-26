import math

def split_list(orig_list):
    list_len = len(orig_list)
    mid_pos = math.ceil(list_len/2)
    list1 = orig_list[:mid_pos]
    list2 = orig_list[mid_pos:]
    return [list1, list2]

def main():
    colors = ["red", "blue", "green", "orange", "purple"]
    colors_split = split_list(colors)
    print(colors_split[0])
    print(colors_split[1])

main()