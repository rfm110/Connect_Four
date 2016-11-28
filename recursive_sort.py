"""
This module recursively sorts a list of numbers


"""
def sort_recursively(my_list, lower_index, upper_index):




    if lower_index == 0:
        upper_index = len(my_list) -1
        lower_index = 1
        print upper_index

    if upper_index == 0:
        return 0

    if upper_index > 0:
        index_of_max = my_list.index(max(my_list[0:upper_index]))
        print upper_index
        print my_list

        maximum_value = max(my_list[0:upper_index])
        upper_value = my_list[upper_index]


    if my_list[upper_index] < my_list[index_of_max]:

            my_list[index_of_max] = upper_value
            my_list[upper_index] = maximum_value
            print(my_list)
            print upper_index
            upper_index = upper_index - 1
            sort_recursively(my_list, lower_index, upper_index)
    # else:
    #     upper_index = upper_index - 1
    #     sort_recursively(my_list, lower_index, upper_index)






#





if __name__ == "__main__":
    # sort_recursively([10, 5, 6, 3, 2, 9, 7, 4, 8, 1], 0, 0)
    sort_recursively([10, 3, 7, 8, 1, 9, 2, 6, 5, 4], 0, 0)