from unittest import TestCase
from main import add_two_numbers


class AddTwoNumbers(TestCase):

    def test_same_size(self):
        expected = [3, 4, 5]
        add_1 = [1, 1, 1]
        add_2 = [2, 3, 4]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_same_size_with_carry(self):
        expected = [1, 3, 6]
        add_1 = [9, 9, 1]
        add_2 = [2, 3, 4]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_firts_biggest_than_second(self):
        expected = [8, 9, 2]
        add_1 = [9, 9, 1]
        add_2 = [9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_firts_smaller_than_second(self):
        expected = [8, 9, 2]
        add_1 = [9, 9]
        add_2 = [9, 9, 1]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_firts_biggest_than_second_and_carry(self):
        expected = [8, 9, 0, 1]
        add_1 = [9, 9, 9]
        add_2 = [9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_firts_smaller_than_second_and_carry(self):
        expected = [8, 9, 0, 1]
        add_1 = [9, 9, 9]
        add_2 = [9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_firts_bigest(self):
        expected = [8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        add_1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        add_2 = [9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_second_bigest(self):
        expected = [8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        add_1 = [9, 9]
        add_2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_first_empty(self):
        expected = [9, 9]
        add_1 = []
        add_2 = [9, 9]
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_second_empty(self):
        expected = [9, 9]
        add_1 = [9, 9]
        add_2 = []
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")

    def test_diff_size_both_empty(self):
        expected = []
        add_1 = []
        add_2 = []
        output = add_two_numbers(add_1, add_2)
        self.assertEqual(output, expected, f"{add_1}+{add_2}")
