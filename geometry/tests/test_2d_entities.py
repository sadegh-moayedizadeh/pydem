"""Test cases for all the classes and their methods from
two_dimensional_entities module from geometry sub-packages
"""

import sys
import unittest
import numpy as np
import os
from geometry import two_dimensional_entities as shapes
from geometry import two_dimensional_operations as operations


class TestPoint(unittest.TestCase):
    """Testing the Point class form two_dimensional_entities module

    Parents:
        unittest.TestCase: base class to write unit tests
    """

    def test_from_rtheta(self):
        """testing construction of the Point object from the given
        'r-theta' coordinates"""

        instance = shapes.Point.from_rtheta(1, np.pi / 2)
        self.assertAlmostEqual(0, instance.x)
        self.assertAlmostEqual(1, instance.y)

    def test_get_rtheta(self):
        """testing the 'r' and 'theta' recieved form the get_rtheta
        method"""

        instance = shapes.Point(1, 0)
        self.assertEqual((1, 0), instance.get_rtheta)

    def test_get_rtheta_xzero(self):
        """testing the 'r' and 'theta' recieved from the get_rtheta
        method with the 'x' coordinate provided being zero to see if
        the method is compatible with division by zero"""

        instance = shapes.Point(0, 1)
        self.assertEqual((1, np.pi / 2), instance.get_rtheta)

    def test_equality(self):
        """testing if two points with the same coordinates are equal"""

        instance1 = shapes.Point(0, 0)
        instance2 = shapes.Point(0, 0)
        self.assertEqual(instance1, instance2)


class TestPolygon(unittest.TestCase):
    """Testing the Polygon class from two_dimensional_entities module

    Parents:
        unittest.TestCase: base class to write unit tests
    """

    def test_construction1(self):
        """testing the construction of the object with less than three
        vertices given"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 1)
        self.assertRaises(RuntimeError, shapes.Polygon, p1, p2)

    def test_construction2(self):
        """testing the constuction of the object with the same vetex
        given twice"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(0, 1)
        p3 = shapes.Point(0, 0)
        self.assertRaises(RuntimeError, shapes.Polygon, p1, p2, p3)

    def test_construction3(self):
        """testing the construction of the object with vertices given
        in a way that edges intersect one another"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 1)
        p3 = shapes.Point(1, 0)
        p4 = shapes.Point(0, 1)
        self.assertRaises(RuntimeError, shapes.Polygon, p1, p2, p3, p4)

    def test_as_regular(self):
        """testing 'as_regular' method from Polygon class"""

        instance = shapes.Polygon.as_regular(
            center=shapes.Point(0, 0), diameter=2, number_of_vertices=4
        )
        expected_vertices = (
            shapes.Point(1, 0),
            shapes.Point(0, 1),
            shapes.Point(-1, 0),
            shapes.Point(0, -1),
        )
        for i in range(4):
            self.assertAlmostEqual(instance.vertices[i].x, expected_vertices[i].x)
            self.assertAlmostEqual(instance.vertices[i].y, expected_vertices[i].y)

    def test_number_of_vertices(self):
        """testing the number_of_vertices method from Polygon class"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(1, 1)
        p4 = shapes.Point(0, 1)
        instance = shapes.Polygon(p1, p2, p3, p4)
        self.assertEqual(instance.number_of_vertices, 4)

    def test_edges(self):
        """Testing the 'edges' method from Polygon class"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(1, 1)
        p4 = shapes.Point(0, 1)
        instance = shapes.Polygon(p1, p2, p3, p4)
        expected = (
            shapes.LineSegment(p4, p1),
            shapes.LineSegment(p1, p2),
            shapes.LineSegment(p2, p3),
            shapes.LineSegment(p3, p4),
        )
        self.assertEqual(instance.edges, expected)

    def test_perimeter(self):
        """Testing the 'perimeter' method of Polygon class"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(1, 1)
        p4 = shapes.Point(0, 1)
        instance = shapes.Polygon(p1, p2, p3, p4)
        self.assertEqual(instance.perimeter, 4)

    def test_equality(self):
        """testing if two polygons with the same vertices are equal"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(1, 1)
        p4 = shapes.Point(0, 1)
        instance1 = shapes.Polygon(p1, p2, p3, p4)
        instance2 = shapes.Polygon(p1, p2, p3, p4)
        self.assertEqual(instance1, instance2)

    def test_equality2(self):
        """testing if two polygon with the same vertices but with
        different order of entering those vertices are equal"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(1, 1)
        p4 = shapes.Point(0, 1)
        instance1 = shapes.Polygon(p1, p2, p3, p4)
        instance2 = shapes.Polygon(p4, p3, p2, p1)
        self.assertEqual(instance1, instance2)


class TestRectangle(unittest.TestCase):
    """Testing the Rectangle class and its methods from
    two_dimensional_entities module in geometry sub-package

    Parents:
        unittest.TestCase: the base class to writes unit tests
    """

    def test_construction1(self):
        """testing the construction of Rectangle instance with less
        than four vertices given"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 1)
        p3 = shapes.Point(0, 1)
        self.assertRaises(RuntimeError, shapes.Rectangle, p1, p2, p3)

    def test_construction2(self):
        """testing the construction of Rectangle instance with more
        than four vertices given"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(0, 1)
        p3 = shapes.Point(1, 2)
        p4 = shapes.Point(2, 1)
        p5 = shapes.Point(2, 0)
        self.assertRaises(RuntimeError, shapes.Rectangle, p1, p2, p3, p4, p5)

    def test_construction3(self):
        """testing the construction of Rectangle instance with the
        vertices given in a way that the edges won't be perpendecular"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 0)
        p3 = shapes.Point(2, 1)
        p4 = shapes.Point(1, 0)
        self.assertRaises(RuntimeError, shapes.Rectangle, p1, p2, p3, p4)

    def test_from_midline1(self):
        """testing the 'from_midline' method of Rectangle class with a
        vertical line segment given as the midline
        """

        end1 = shapes.Point(1, 0)
        end2 = shapes.Point(1, 1)
        instance1 = shapes.Rectangle.from_midline(
            midline=shapes.LineSegment(end1, end2), tolerance = 2
        )
        vertex1 = shapes.Point(-1, 0)
        vertex2 = shapes.Point(3, 0)
        vertex3 = shapes.Point(3, 1)
        vertex4 = shapes.Point(-1, 1)
        instance2 = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        self.assertEqual(instance1, instance2)
    
    def test_from_midline2(self):
        """testing the 'from_midline' method of Rectangle class with a
        line with arbitrary inclination segment given as the midline
        """

        end1 = shapes.Point(0, 0)
        end2 = shapes.Point(1, 1)
        instance1 = shapes.Rectangle.from_midline(
            midline=shapes.LineSegment(end1, end2), tolerance = np.sqrt(2)
        )
        vertex1 = shapes.Point(-1, 1)
        vertex2 = shapes.Point(0, 2)
        vertex3 = shapes.Point(2, 0)
        vertex4 = shapes.Point(1, -1)
        instance2 = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        self.assertEqual(instance1, instance2)

    def test_from_diagonal1(self):
        """testing the 'from_diagonal' method of Rectangle class"""

        end1 = shapes.Point(0, 0)
        end2 = shapes.Point(1, 1)
        instance1 = shapes.Rectangle.from_diagonal(diagonal=shapes.LineSegment(end1, end2))
        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 1)
        vertex4 = shapes.Point(0, 1)
        instance2 = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        self.assertEqual(instance1, instance2)

    def test_from_diagonal2(self):
        """testing the 'from_diagonal' method of Rectangle class with
        ends given to the diagonal in an order different from
        test_from_diagonal1 test method"""

        end2 = shapes.Point(0, 0)
        end1 = shapes.Point(1, 1)
        instance1 = shapes.Rectangle.from_diagonal(diagonal=shapes.LineSegment(end1, end2))
        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 1)
        vertex4 = shapes.Point(0, 1)
        instance2 = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        self.assertEqual(instance1, instance2)

    def test_area(self):
        """testing the 'area' method of Rectangle class"""

        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 1)
        vertex4 = shapes.Point(0, 1)
        instance = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        self.assertEqual(instance.area, 1)

    def test_midlines(self):
        """testing the 'midlines' method of Rectangle class"""

        v1 = shapes.Point(0, 0)
        v2 = shapes.Point(1, 0)
        v3 = shapes.Point(1, 2)
        v4 = shapes.Point(0, 2)
        rec = shapes.Rectangle(v1, v2, v3, v4)
        midline1 = shapes.LineSegment(end1 = shapes.Point(0.5, 0), end2 = shapes.Point(0.5, 2))
        midline2 = shapes.LineSegment(end1 = shapes.Point(0, 1), end2 = shapes.Point(1, 1))
        expected = [midline1, midline2]
        res = rec.midlines
        self.assertEqual(set(res), set(expected))

    def test_diagonals(self):
        """testing the 'diagonals' method of Rectangle class"""

        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 1)
        vertex4 = shapes.Point(0, 1)
        instance = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        diagonal1 = shapes.LineSegment(end1=shapes.Point(0, 0), end2=shapes.Point(1, 1))
        diagonal2 = shapes.LineSegment(end1=shapes.Point(1, 0), end2=shapes.Point(0, 1))
        expected = (diagonal1, diagonal2)
        self.assertEqual(instance.diagonals, expected)

    def test_center(self):
        """testing the 'centre' method of Rectangle class"""

        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 1)
        vertex4 = shapes.Point(0, 1)
        instance = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        expected = shapes.Point(0.5, 0.5)
        self.assertEqual(instance.center, expected)

    def test_circumcircle(self):
        """testing the 'circumcircle' method of Rectangle class"""

        vertex1 = shapes.Point(0, 0)
        vertex2 = shapes.Point(1, 0)
        vertex3 = shapes.Point(1, 2)
        vertex4 = shapes.Point(0, 2)
        instance = shapes.Rectangle(vertex1, vertex2, vertex3, vertex4)
        expected = shapes.Circle(shapes.Point(0.5, 1), np.sqrt(5))
        self.assertEqual(instance.circumcircle, expected)
    
    def test_move(self):
        """testing the 'move' method of the Rectangle class
        """

        v1 = shapes.Point(np.sqrt(2), np.sqrt(2))
        v2 = shapes.Point(-1*np.sqrt(2), np.sqrt(2))
        v3 = shapes.Point(-1*np.sqrt(2), -1*np.sqrt(2))
        v4 = shapes.Point(np.sqrt(2), -1*np.sqrt(2))
        rec1 = shapes.Rectangle(v1, v2, v3, v4)
        rec1.move(delta_theta = np.math.pi/4)
        v5 = shapes.Point(2, 0)
        v6 = shapes.Point(0, 2)
        v7 = shapes.Point(-2, 0)
        v8 = shapes.Point(0, -2)
        rec2 = shapes.Rectangle(v5, v6, v7, v8)
        self.assertEqual(rec1, rec2)


class TestCircle(unittest.TestCase):
    """Testing the Circle class from two_dimensional_entitie modules in
    geometry sub-package"""

    def test_construction(self):
        """testing the construction of the Circle object with an
        insvalid entry (negative diameter)"""

        c = shapes.Point(0, 0)
        d = -1
        self.assertRaises(RuntimeError, shapes.Circle, center=c, diameter=d)

    def test_area(self):
        """testing the 'area' method of Circle class"""

        c = shapes.Point(0, 0)
        d = 1
        instance = shapes.Circle(c, d)
        expected = ((np.pi) * (d) ** 2) / 4
        self.assertEqual(instance.area, expected)

    def test_perimeter(self):
        """testing the 'perimeter' method of Circle class"""

        c = shapes.Point(0, 0)
        d = 1
        instance = shapes.Circle(c, d)
        expected = (np.pi) * (d)
        self.assertEqual(instance.perimeter, expected)

    def test_get_point_on_perimeter(self):
        """testing the 'get_point_on_perimeter' method of Circle class"""
        
        c = shapes.Point(0, 0)
        d = 2
        instance = shapes.Circle(c, d)
        angle = (np.pi) / 2
        res = instance.get_point_on_perimeter(angle)
        self.assertAlmostEqual(res.x, 0)
        self.assertAlmostEqual(res.y, 1)

    def test_equality(self):
        """testing the equality condition of Circle class"""

        c = shapes.Point(0, 0)
        d = 1
        instance1 = shapes.Circle(c, d)
        instance2 = shapes.Circle(c, d)
        self.assertEqual(instance1, instance2)

    def test_navigator(self):
        """testing the 'navigator' method of the Circle class"""

        c = shapes.Point(0, 0)
        d = 2
        instance = shapes.Circle(c, d)
        gen = instance.navigator(0, np.pi / 4, 1)
        next(gen)
        expected = shapes.Point((np.sqrt(2) / 2), (np.sqrt(2) / 2))
        p = next(gen)
        self.assertAlmostEqual(p.x, expected.x)
        self.assertAlmostEqual(p.y, expected.y)

    def test_navigator2(self):
        """testing if the 'navigator' method of the Circle class
        terminates after the specified number of rounds"""

        c = shapes.Point(0, 0)
        d = 1
        instance = shapes.Circle(c, d)
        gen = instance.navigator(0, np.pi / 4, 2)
        count = 0
        for _ in gen:
            count += 1
        self.assertEqual(count, 16)

    def test_move(self):
        """testing the 'move' method of the Circle class"""

        c1 = shapes.Point(0, 0)
        c2 = shapes.Point(1, 1)
        d = 1
        instance1 = shapes.Circle(c1, d)
        instance2 = shapes.Circle(c2, d)
        instance1.move(1, 1)
        self.assertEqual(instance1, instance2)


class TestLine(unittest.TestCase):
    """Testing the methods of the Line class from the  two_dimensional_entities
    module in geometry sub-package"""

    def test_from_points(self):
        """testing the construction of the Line object via from_points
        method"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.Line.from_points(point1, point2)
        self.assertEqual(instance.slope, 1)
        self.assertEqual(instance.width, 0)

    def test_from_point_and_inclination(self):
        """testing the construction of the Line object via
        from_point_and_inclination method"""

        point = shapes.Point(0, 0)
        inclination = (np.math.pi) / 4
        instance1 = shapes.Line.from_point_and_inclination(point, inclination)
        instance2 = shapes.Line(1, 0)
        self.assertAlmostEqual(instance1.slope, instance2.slope)
        self.assertAlmostEqual(instance1.width, instance2.width)

    def test_from_ij(self):
        """testing the construction of the Line object via from_ij
        method"""

        i = 1
        j = 1
        instance1 = shapes.Line.from_ij(i, j)
        instance2 = shapes.Line(1, 0)
        self.assertEqual(instance1, instance2)

    def test_inclination(self):
        """testing the 'inclination' method of the Line class"""

        instance = shapes.Line(1, 0)
        expected = (np.pi) / 4
        self.assertEqual(instance.inclination, expected)

    def test_get_x1(self):
        """testing the 'get_x' method of the Line class in a usual
        manner"""

        instance = shapes.Line(1, 0)
        self.assertEqual(instance.get_x(1), 1)

    def test_get_x2(self):
        """testing the 'get_x' method of the Line class with the Line
        object having the slope of infinity"""

        point1 = shapes.Point(1, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.Line.from_points(point1, point2)
        self.assertEqual(instance.get_x(1), 1)

    def test_get_x3(self):
        """testing the 'get_x' method of the Line class with the Line
        object having the slope of zero"""

        instance = shapes.Line(0, 1)
        self.assertRaises(RuntimeError, instance.get_x, 1)

    def test_get_y(self):
        """testing the 'get_y' method of the Line class"""

        instance = shapes.Line(1, 0)
        self.assertEqual(instance.get_y(1), 1)

    def test_equality(self):
        """testing the equality conditoin of the Line class"""

        instance1 = shapes.Line(1, 0)
        instance2 = shapes.Line(1, 0)
        self.assertEqual(instance1, instance2)

    def test_navigator1(self):
        """testing the 'navigator' method of the Line class"""

        instance = shapes.Line(1, 0)
        start = shapes.Point(0, 0)
        end = shapes.Point(1, 1)
        gen = instance.navigator(start, end, 2)
        next(gen)
        expected = shapes.Point(np.sqrt(2), np.sqrt(2))
        res = next(gen)
        self.assertAlmostEqual(res.x, expected.x)
        self.assertAlmostEqual(res.y, expected.y)

    def test_navigator2(self):
        """testing the 'navigator' method of the Line class with an invalid
        start point given, which is not located on the Line"""

        instance = shapes.Line(1, 0)
        start = shapes.Point(0, 1)
        end = shapes.Point(1, 1)
        gen = instance.navigator(start, end, 0)
        self.assertRaises(RuntimeError, next, gen)

    def test_move(self):
        """testing the 'move' method of the Line class"""

        instance1 = shapes.Line(1, 0)
        instance2 = shapes.Line(1, 1)
        instance1.move(0, 1)
        self.assertEqual(instance1, instance2)


class TestLineSegment(unittest.TestCase):
    """Testing the methods of the LineSegment class"""

    def test_construction(self):
        """testing the construction of the LineSegment object"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(0, 0)
        self.assertRaises(RuntimeError, shapes.LineSegment, point1, point2)

    def test_equality(self):
        """testing the equality condition of the LineSegment object"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance1 = shapes.LineSegment(point1, point2)
        instance2 = shapes.LineSegment(point1, point2)
        self.assertEqual(instance1, instance2)

    def test_from_point_and_inclination(self):
        """testing the 'from_point_and_inclination' method of LineSegment
        class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        point3 = shapes.Point(0.5, 0.5)
        inclination = (np.pi) / 4
        size = np.sqrt(2)
        instance1 = shapes.LineSegment(point1, point2)
        instance2 = shapes.LineSegment.from_point_and_inclination(point3, inclination, size)
        self.assertAlmostEqual(instance1.end1.x, instance2.end1.x)
        self.assertAlmostEqual(instance1.end1.y, instance2.end1.y)
        self.assertAlmostEqual(instance1.end2.x, instance2.end2.x)
        self.assertAlmostEqual(instance1.end2.y, instance2.end2.y)

    def test_length(self):
        """testing the 'length' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        expected = np.sqrt(2)
        self.assertEqual(instance.length, expected)

    def test_circumcircle(self):
        """testing the 'circumcircle' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        circle = shapes.Circle(shapes.Point(0.5, 0.5), np.sqrt(2))
        res = instance.circumcircle
        self.assertEqual(res, circle)

    def test_inclination(self):
        """testing the 'inclination' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        expected = (np.pi) / 4
        self.assertEqual(instance.inclination, expected)

    def test_slope(self):
        """testing the 'slope' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        expected = 1
        self.assertEqual(instance.slope, expected)

    def test_slope2(self):
        """testing the 'slope' method of the LineSegment class for a
        vertical LineSegment"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(0, 1)
        instance = shapes.LineSegment(point1, point2)
        expected = np.tan(np.pi / 2)
        self.assertEqual(instance.slope, expected)

    def test_infinite(self):
        """testing the 'infinite' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance1 = shapes.LineSegment(point1, point2)
        instance2 = shapes.Line(1, 0)
        self.assertEqual(instance1.infinite, instance2)

    def test_get_x(self):
        """testing the 'get_x' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        self.assertEqual(instance.get_x(0.5), 0.5)

    def test_get_x2(self):
        """testing the 'get_x' method of the LineSegment class expecting
        an error asking for coordinates that isn't loacated on the
        LineSegment instance"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        self.assertRaises(RuntimeError, instance.get_x, 2)

    def test_get_y(self):
        """testing the 'get_y' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        self.assertEqual(instance.get_x(0.5), 0.5)

    def test_get_y2(self):
        """testing the 'get_y' method of the LineSegment class expecting
        an error asking for coordinates that isn't loacated on the
        LineSegment instance"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(point1, point2)
        self.assertRaises(RuntimeError, instance.get_y, 2)

    def test_midpoint(self):
        """testing the 'midpoint' method of the LineSegment class"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(p1, p2)
        expected = shapes.Point(0.5, 0.5)
        res = instance.midpoint(0.5)
        self.assertAlmostEqual(res.x, expected.x)
        self.assertAlmostEqual(res.y, expected.y)

    def test_midpoint2(self):
        """testing the 'midpoint' method of the LineSegment class given
        an invalid ratio"""

        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(1, 1)
        instance = shapes.LineSegment(p1, p2)
        self.assertRaises(RuntimeError, instance.midpoint, 2)

    def test_navigator(self):
        """testing the navigator method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        line = shapes.LineSegment(point1, point2)
        gen = line.navigator(0.2)
        self.assertEqual(next(gen), shapes.Point(0, 0))
        self.assertEqual(next(gen), shapes.Point(0.2, 0.2))
        self.assertEqual(next(gen), shapes.Point(0.4, 0.4))
        self.assertEqual(next(gen), shapes.Point(0.6, 0.6))
        self.assertEqual(next(gen), shapes.Point(0.8, 0.8))
        self.assertEqual(next(gen), shapes.Point(1, 1))
        self.assertRaises(StopIteration, next, gen)

    def test_move1(self):
        """testing the 'move' method of the LineSegment class"""

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        instance1 = shapes.LineSegment(point1, point2)
        point3 = shapes.Point(1, 1)
        point4 = shapes.Point(2, 2)
        instance2 = shapes.LineSegment(point3, point4)
        instance1.move(1, 1)
        self.assertEqual(instance1, instance2)

    def test_move2(self):
        """testing the 'move' method of the LineSegment class with a
        full rotation
        """

        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        line = shapes.LineSegment(point1, point2)
        line.move(delta_theta = np.math.pi)
        self.assertEqual(line, shapes.LineSegment(point1, point2))
        line.move(delta_theta = np.math.pi*2)
        self.assertEqual(line, shapes.LineSegment(point1, point2))
    
    def test_move3(self):
        """testing the 'move' method of LineSegment class with all
        the coordinates changing
        """

        point1 = shapes.Point(-1*np.sqrt(2), 0)
        point2 = shapes.Point(np.sqrt(2), 0)
        line1 = shapes.LineSegment(point1, point2)
        line1.move(delta_x = 5, delta_y = 5, delta_theta = 3*np.math.pi/4)
        point3 = shapes.Point(4, 6)
        point4 = shapes.Point(6, 4)
        line2 = shapes.LineSegment(point3, point4)
        self.assertEqual(line1, line2)
            

if __name__ == "__main__":
    unittest.main()