import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[1,2], []]
        result = lab4.first_element(input)
        expected = [1]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates_1(self):
        input = data.Point(2,6), data.Point(67,4)
        result = lab4.x_coordinates(input)
        expected = [2,67]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = data.Point(0,2), data.Point(1.5,4)
        result = lab4.x_coordinates(input)
        expected = [0,1.5]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(-1,2), data.Point(-2,4)]
        result = lab4.are_in_positive_quadrant(input)
        expected = ([])
        self.assertEqual(expected, result)
    def test_are_in_positve_quadrant_1(self):
        input = [data.Point(1,2), data.Point(1,4)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(1,2),data.Point(1,4)]
        self.assertEqual(expected, result)


    # Part 4
    def test_distance_1(self):
        d1= data.Point(4,6)
        d2=data.Point(7,2)
        result = lab4.distance(d1,d2)
        expected = 5
        self.assertEqual(expected, result)
    def test_distance_2(self):
        d1= data.Point(1,0)
        d2=data.Point(5,0)
        result = lab4.distance(d1,d2)
        expected = 4
        self.assertEqual(expected, result)

    # Part 5
    def test__manhattan_distance_3(self):
        d1= data.Point(1,0)
        d2=data.Point(5,0)
        result = lab4.manhattan_distance(d1,d2)
        expected = 4
        self.assertEqual(expected, result)
    def test_manhattan_distance_4(self):
        d1= data.Point(5,6)
        d2=data.Point(2,3)
        result = lab4.manhattan_distance(d1,d2)
        expected = 6
        self.assertEqual(expected, result)


    # Part 6
    def test_distance_all_1(self):
        input= [data.Point(1,2)]
        result = lab4.distance_all(input)
        expected = [3]
        self.assertEqual(expected, result)
    def test_distance_all_2(self):
        input= [data.Point(2,2)]
        result = lab4.distance_all(input)
        expected = [4]
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
