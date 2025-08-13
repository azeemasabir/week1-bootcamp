import unittest
from csv_grading import calculate_average, read_grades

class TestCSVGrading(unittest.TestCase):
    def test_calculate_average(self):
        grades = [("Alice", 80), ("Bob", 100)]
        self.assertEqual(calculate_average(grades), 90)

    def test_read_grades(self):
        test_file = "grades.csv"
        grades = read_grades(test_file)
        self.assertTrue(len(grades) > 0)
        self.assertIsInstance(grades[0][1], float)

if __name__ == "__main__":
    unittest.main()
