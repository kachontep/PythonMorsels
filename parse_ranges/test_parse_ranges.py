import unittest

from parse_ranges import parse_ranges, range_from_string, generate_range


class RangeFromStringTests(unittest.TestCase):
    def test_single_range_string(self):
        self.assertEqual(list(range_from_string("1-2")), [(1, 2)])

    def test_multiple_range_strings(self):
        self.assertEqual(list(range_from_string("1-2, 3-3")), [(1, 2), (3, 3)])
        self.assertEqual(list(range_from_string(
            "1-2, 3-3,  4-10")), [(1, 2), (3, 3), (4, 10)])

    def test_optional_end_string(self):
        self.assertEqual(list(range_from_string("1")), [(1, 1)])
        self.assertEqual(list(range_from_string("1-2, 3, 4-5")),
                         [(1, 2), (3, 3), (4, 5)])


class GenerateRangeTests(unittest.TestCase):
    def test_generate_with_length(self):
        self.assertEqual(list(generate_range(1, 10)), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_generate_without_length(self):
        self.assertEqual(list(generate_range(5, 5)), [5])


class ParseRangesTests(unittest.TestCase):

    """Tests for parse_ranges."""

    def test_three_ranges(self):
        self.assertEqual(
            list(parse_ranges('1-2,4-4,8-10')),
            [1, 2, 4, 8, 9, 10],
        )

    def test_with_spaces(self):
        self.assertEqual(
            list(parse_ranges('0-0, 4-8, 20-21, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45],
        )

    # @unittest.expectedFailure
    def test_return_iterator(self):
        numbers = parse_ranges('0-0, 4-8, 20-21, 43-45')
        self.assertEqual(next(numbers), 0)
        self.assertEqual(list(numbers), [4, 5, 6, 7, 8, 20, 21, 43, 44, 45])
        self.assertEqual(list(numbers), [])
        numbers = parse_ranges('100-1000000000000')
        self.assertEqual(next(numbers), 100)

    # @unittest.expectedFailure
    def test_with_individual_numbers(self):
        self.assertEqual(
            list(parse_ranges('0,4-8,20,43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )

    # @unittest.expectedFailure
    def test_ignore_arrows(self):
        self.assertEqual(
            list(parse_ranges('0, 4-8, 20->exit, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
