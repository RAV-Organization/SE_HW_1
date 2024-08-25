from myfile import insertionSort

def test_insertion_sort_pass():
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    assert arr == [5, 6, 11, 12, 13]

# def test_insertion_sort_fail():
#     arr = [12, 11, 13, 5, 6]
#     insertionSort(arr)
#     assert arr == [12, 11, 13, 5, 6]