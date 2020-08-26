from pathlib import Path

def file_path(relative_path):
    """Returns absolute path from relative path"""
    start_dir = Path(__file__).parent
    return Path(start_dir, relative_path)

def file_to_list(path):
    """Returns content of file at path as list"""
    with open(file_path(path), encoding='utf-8') as f:
        lines = f.read().splitlines()
    return lines

def subtract_lists(list1, list2):
    """Returns a list of all items in list1, but not in list2"""
    return [x for x in list1 if x not in list2]

def dups(list1, list2, sort=True):
    """Returns a list containing items in both lists"""
    dup_list = []
    for item in list1:
        if item in list2:
            dup_list.append(item)

    if sort:
        dup_list.sort()

    return dup_list

def list_to_file(path, the_list):
    """Creates/Overwrites file at path with content from the_list"""
    content = '\n'.join(the_list)

    with open(file_path(path), 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    boys_2018_path = Path('../data/2018-boys.txt')
    girls_2018_path = Path('../data/2018-girls.txt')
    boys_1880_path = Path('../data/1880-boys.txt')
    girls_1880_path = Path('../data/1880-girls.txt')

    boys_2018 = file_to_list(boys_2018_path)
    girls_2018 = file_to_list(girls_2018_path)
    boys_1880 = file_to_list(boys_1880_path)
    girls_1880 = file_to_list(girls_1880_path)

    boys_only_2018 = subtract_lists(boys_2018, girls_2018)
    girls_only_2018 = subtract_lists(girls_2018, boys_2018)
    boys_only_1880 = subtract_lists(boys_1880, girls_1880)
    girls_only_1880 = subtract_lists(girls_1880, boys_1880)

    boys_names_2_girls_names = dups(girls_only_2018, boys_only_1880)
    girls_names_2_boys_names = dups(boys_only_2018, girls_only_1880)

    list_to_file(
        Path('../data/girls-names-that-were-boys-names.txt'),
        boys_names_2_girls_names
    )
    list_to_file(
        Path('../data/boys-names-that-were-girls-names.txt'),
        girls_names_2_boys_names
    )

main()