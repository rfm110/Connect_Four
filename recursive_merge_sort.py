"""
This module uses the merge sort function to recursively sort a list
"""
def recursive_merge_sort(mylist):
    sorted_list = mylist

    if len(mylist) > 2:
        # divide input list into two lists
        first_half = mylist[0:len(mylist) / 2]
        second_half = mylist[len(mylist) / 2:]
        print first_half
        print second_half

        # recursively divide divided lists into even smaller lists, stops when len(list) = 1
        # print first_half, second_half


        recursive_merge_sort(first_half)
        print('first half is %s' % first_half)
        recursive_merge_sort(second_half)
        print('second half is %s' % second_half)

        # since there is only one item in each list, all the lists are essentially sorted
        # need only to compare lists with lists not units within lists to other units in the same list
        first_ref = 0
        second_ref = 0
        new_index = 0
        print('len(first_half) is %s' % len(first_half))
        print ('len(second_half) is %s' % len(second_half))
        print ('second_half[second_ref] is %s' % second_half[second_ref])
        print ('first_half[first_ref] is %s ' % first_half[first_ref])
        # recursive_merge_sort(first_half+second_half)
        while len(first_half) > first_ref and len(second_half) > second_ref:
            #need length to be greater than ref numbers for both halves of the list
            if second_half[second_ref] > first_half[first_ref]:
                sorted_list[new_index] = first_half[first_ref]
                print ('sorted_list 1 is %s' % sorted_list)
                first_ref = first_ref + 1



            else:
                sorted_list[new_index] = second_half[second_ref]
                second_ref = second_ref + 1
                print ('sorted_list 2 is %s' % sorted_list)


            new_index = new_index + 1
        while len(first_half) > first_ref:
            sorted_list[new_index] = first_half[first_ref]
            new_index = new_index + 1
            first_ref = first_ref + 1
            if sorted_list[0] > sorted_list[1]:
                zero = sorted_list[0]
                one = sorted_list[1]
                sorted_list[0] = one
                sorted_list[1] = zero
            print ('sorted_list 3 is %s' % sorted_list)


        while len(second_half) > second_ref:
            sorted_list[new_index] = second_half[second_ref]
            second_ref = second_ref + 1
            new_index = new_index + 1
            if sorted_list[0] > sorted_list[1]:
                zero = sorted_list[0]
                one = sorted_list[1]
                sorted_list[0] = one
                sorted_list[1] = zero
            print ('sorted_list 4 is %s' % sorted_list)

        for i in range(len(mylist)-1, 0, -1):
            j = i-1
            higher_index = sorted_list[i]
            lower_index = sorted_list[j]
            # print i
            # print j
            if sorted_list[i] < sorted_list[j]:
                sorted_list[i] = lower_index
                sorted_list[j] = higher_index
        print sorted_list


        return sorted_list

    else:
        return 0















recursive_merge_sort([5, 3, 9, 8, 10, 7, 2, 4, 1, 6])

