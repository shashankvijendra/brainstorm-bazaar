def sort_list_by_order(main_list, values_list,  one_more_list=[]):
    """
    Sorts the main_list based on the values from the values_list.
    """
    sorted_list = [(_,x,y) for _, x,y in sorted(zip(values_list, main_list,one_more_list))]
    return sorted_list

# Example usage:
main_list = ['apple', 'banana', 'orange']
values_list = [3, 1, 2]
one_more_list = [6,2,1]
sorted_result = sort_list_by_order(main_list, values_list,one_more_list)
print("Sorted List based on Values from Another List:", sorted_result)

main_list = [1,2,3]
values_list = [3, 1, 6]
sorted_result = sort_list_by_order(main_list, values_list,one_more_list)
print("Sorted List based on Values from Another List:", sorted_result)