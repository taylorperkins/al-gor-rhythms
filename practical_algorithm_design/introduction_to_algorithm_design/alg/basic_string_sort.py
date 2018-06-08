from copy import copy


def basic_string_sort(val):
    """String sort!
    Given 'cba', return 'abc'

    Create a copy of the original value, and iterate over every element (i) in the list, starting with 1.
    While that element (j --> j == i) is less than the previous element, swap it with the previous. j is now j-1
    Continue

    :param val: str()
    :return: str()
    """
    val_ = list(copy(val))

    for i in range(1, len(val_)):
        j = i

        while (j > 0) and (val_[j] < val_[j-1]):
            val_[j-1:j+1] = [val_[j], val_[j-1]]

            j = j-1

    return ''.join(val_)
