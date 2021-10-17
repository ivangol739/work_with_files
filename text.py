
def sort_files():
    text_in_files = {}

    with open('sorted/1.txt', encoding='UTF-8') as t1:
        text1 = t1.readlines()
        text_in_files[len(text1)] = ['1.txt', text1]

    with open('sorted/2.txt', encoding='UTF-8') as t2:
        text2 = t2.readlines()
        text_in_files[len(text2)] = ['2.txt', text2]

    with open('sorted/3.txt', encoding='UTF-8') as t3:
        text3 = t3.readlines()
        text_in_files[len(text3)] = ['3.txt', text3]

    with open('finaltextfile.txt', 'a', encoding='UTF-8') as finaltextfile:
        list_long = list(text_in_files.keys())
        list_long.sort()
        for long in list_long:
            finaltextfile.write(f'{text_in_files[long][0]} \n')
            finaltextfile.write(f'{str(long)} \n')
            finaltextfile.write(f'{"".join(text_in_files[long][1])} \n')
    return

sort_files()