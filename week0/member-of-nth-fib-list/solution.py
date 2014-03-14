def member_of_nth_fib_lists(listA, listB, needle):
    if len(needle) < len(listA):
        return False
    if len(needle) > len(listA):
        return member_of_nth_fib_lists(listB, listA + listB, needle)
    return listA == needle