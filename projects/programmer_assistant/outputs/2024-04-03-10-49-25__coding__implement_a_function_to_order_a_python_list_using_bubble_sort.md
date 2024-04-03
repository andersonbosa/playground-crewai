```python
def bubble_sort(list1):
    """
    Sorts a list using the bubble sort algorithm.

    Parameters:
    list1: The list to be sorted.

    Returns:
    The sorted list.
    """

    # Iterate over the list, comparing each element to its neighbor.
    for i in range(len(list1) - 1):
        # If the current element is greater than its neighbor, swap them.
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]

    # Repeat the process until the list is sorted.
    if not is_sorted(list1):
        return bubble_sort(list1)

    return list1


def is_sorted(list1):
    """
    Checks if a list is sorted.

    Parameters:
    list1: The list to be checked.

    Returns:
    True if the list is sorted, False otherwise.
    """

    for i in range(1, len(list1)):
        if list1[i] < list1[i - 1]:
            return False

    return True
```