lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда'] 
lst_int = [] 
lst_str = [] 
 
def clean_lst(lst): 
    return list(set(lst)) 
cleaned_lst = clean_lst(lst) 
 
def sort_lst(lst): 
    for item in lst: 
        if type(item) == int: 
            lst_int.append(item) 
        if type(item) == str: 
            item = item.lower() 
            lst_str.append(item) 
 
sort_lst(cleaned_lst) 
 
lst_int.sort() 
lst_str.sort() 
 
lst = lst_int + lst_str 
print(lst)
