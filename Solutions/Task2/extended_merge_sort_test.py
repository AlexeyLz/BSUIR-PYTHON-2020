import unittest
import extended_merge_sort


class ExtendedMergeSort(unittest.TestCase):
    def test_check_amount(self):
        self.assertEqual(extended_merge_sort.check_amount(-3), 3, "Incorrect work")

    def test_merge_sort(self):
        arr = [2, 3, 1]
        extended_merge_sort.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3], "Error merge sort")


if __name__ == "__main__":
    unittest.main()