lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
cleaned_lst = clean_list(lst)
sorted_lst = sort_list(cleaned_lst)
def clean_list(lst)
    return list(set(lst))

def sort_list(lst):
    lst_int = []
    lst_str = []
    for item in lst:
        if isinstance(item, int):
            lst_int.append(item)
        elif isinstance(item, str):
            lst_str.append(item.lower())
    lst_int.sort()
    lst_str.sort()
   
    return lst_int + lst_str

print(sorted_lst)
