"""test cases for the 'projection' function for two dimensional
entities
"""

import unittest
from geometry import two_dimensional_operations as operations
from geometry import two_dimensional_entities as shapes
import numpy as np


class TestProjection(unittest.TestCase):
    """test cases for the 'projection' function from
    'two_dimensional_operations' module
    """
    
    def test_for_point_and_point(self):
        """testing the projection of a given point on another given
        point
        """
        
        point1 = shapes.Point(0, 0)
        point2 = shapes.Point(1, 1)
        self.assertEqual(operations.projection(point1, point2), point2)
    
    def test_for_point_and_polygon1(self):
        """testing the projection of a given point on a given polygon
        with the point being inside the polygon
        """
        
        point = shapes.Point(0, 0)
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        self.assertEqual(operations.projection(point, pol), None)
    
    def test_for_point_and_polygon2(self):
        """the second test for projection of a given point on a given
        polygon with the point being located on the perimeter of the
        polygon
        """
        
        point = shapes.Point(2, 0)
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        self.assertEqual(operations.projection(point, pol), point)
    
    def test_for_point_and_polygon3(self):
        """the third test for projection of a given point on a given
        polygon with the point being located outside the polygon
        """
        
        point = shapes.Point(0, 3)
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        res = shapes.Point(0, 2)
        self.assertEqual(operations.projection(point, pol), res)
    
    def test_for_point_and_rectangle1(self):
        """the first test for projection of a given point on a given
        rectangle with the point being located inside the rectangle
        """
        
        point = shapes.Point(0, 0)
        v1 = shapes.Point(-1, -1)
        v2 = shapes.Point(1, -1)
        v3 = shapes.Point(1, 1)
        v4 = shapes.Point(-1, 1)
        rec = shapes.Rectangle(v1, v2, v3, v4)
        self.assertEqual(operations.projection(point, rec), None)
    
    def test_for_point_and_rectangle2(self):
        """the second test for projection of a given point on a given
        rectangle with the point being located on the perimeter of the
        rectangle
        """
        
        point = shapes.Point(1, 0)
        v1 = shapes.Point(-1, -1)
        v2 = shapes.Point(1, -1)
        v3 = shapes.Point(1, 1)
        v4 = shapes.Point(-1, 1)
        rec = shapes.Rectangle(v1, v2, v3, v4)
        self.assertEqual(operations.projection(point, rec), point)
    
    def test_for_point_and_rectangle3(self):
        """the third test for projection of a given point on a given
        rectangle with the point being located outside the rectangle
        """
        
        point = shapes.Point(2, 0)
        v1 = shapes.Point(-1, -1)
        v2 = shapes.Point(1, -1)
        v3 = shapes.Point(1, 1)
        v4 = shapes.Point(-1, 1)
        rec = shapes.Rectangle(v1, v2, v3, v4)
        res = shapes.Point(1, 0)
        self.assertEqual(operations.projection(point, rec), res)
    
    def test_for_polygon_and_circle1(self):
        """the first test for projection of a given point on a given
        circle with the point being located inside the circle
        """
        
        point = shapes.Point(0, 0)
        circle = shapes.Circle(shapes.Point(0, 0), 1)
        self.assertEqual(operations.projection(point, circle), None)
    
    def test_for_polygon_and_circle2(self):
        """the second test for projection of a given point on a given
        rectangle with the point being located on the perimeter of the
        rectangle
        """
        
        point = shapes.Point(1, 0)
        circle = shapes.Circle(shapes.Point(0, 0), 1)
        self.assertEqual(operations.projection(point, circle), point)
    
    def test_for_polygon_and_circle3(self):
        """the third test for projection of a given point on a given
        rectangle with the point being located outside the rectangle
        """
        
        point = shapes.Point(2, 0)
        circle = shapes.Circle(shapes.Point(0, 0), 1)
        res = shapes.Point(1, 0)
        self.assertEqual(operations.projection(point, circle), res)
    
    def test_for_point_and_line1(self):    
        """the first test for projection of a given point on a given
        infinite line with the point being located on the line
        """
        
        point = shapes.Point(0, 0)
        line = shapes.Line(0, 0)
        self.assertEqual(operations.projection(point, line), point)
    
    def test_for_point_and_line2(self):
        """the second test for projection of a given point on a given
        infinite line with the point being located outside the line
        """
        
        point = shapes.Point(0, 1)
        line = shapes.Line(0, 0)
        res = shapes.Point(0, 0)
        self.assertEqual(operations.projection(point, line), res)
    
    def test_for_point_and_line3(self):
        """the third test for projection of a given point on a given
        infinite line with the point located outside the line and thee
        line being vertical
        """
        
        point = shapes.Point(1, 0)
        p1 = shapes.Point(0, 0)
        p2 = shapes.Point(0, 1)
        line = shapes.Line.from_points(p1, p2)
        res = shapes.Point(0, 0)
        self.assertEqual(operations.projection(point, line), res)
    
    def test_for_point_and_linesegment1(self):
        """the first test for projection of a given point on a given
        line segment with the point being located on the line
        """
        
        point = shapes.Point(0, 0)
        end1 = shapes.Point(0, -1)
        end2 = shapes.Point(0, 1)
        line = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(point, line), point)
    
    def test_for_point_and_linesegment2(self):
        """the second test for projection of a given point on a given
        line segment with the point being located outside the line and
        in front of it
        """
        
        point = shapes.Point(1, 0)
        end1 = shapes.Point(0, -1)
        end2 = shapes.Point(0, 1)
        line = shapes.LineSegment(end1, end2)
        res = shapes.Point(0, 0)
        self.assertEqual(operations.projection(point, line), res)
    
    def test_for_point_and_linesegment3(self):
        """the third test for projection of a given point on a given
        line segment with the point being located outside the line and
        not in front of it
        """
        
        point = shapes.Point(2, 2)
        end1 = shapes.Point(0, -1)
        end2 = shapes.Point(0, 1)
        line = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(point, line), None)
    
    def test_for_polygon_and_point1(self):
        """the first test for projection of a given polygon on a given
        point with the point being inside the polygon
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        point = shapes.Point(0, 0)
        self.assertEqual(operations.projection(pol, point), point)
    
    def test_for_polygon_and_point2(self):
        """the second test for projection of a given polygon on a given
        point with the point being located outside the polygon
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        point = shapes.Point(5, 5)
        self.assertEqual(operations.projection(pol, point), point)
    
    def test_for_polygon_and_polygon1(self):
        """the first test for projection of a given polygon on another
        given polygon with the second one being inside the first one
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol1 = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(-1, -1)
        v8 = shapes.Point(0, -2)
        v9 = shapes.Point(1, -1)
        v10 = shapes.Point(1, 1)
        v11 = shapes.Point(0, 2)
        v12 = shapes.Point(-1, 1)
        pol2 = shapes.Polygon(v7, v8, v9, v10, v11, v12)
        self.assertEqual(operations.projection(pol1, pol2), pol2)
    
    def test_for_polygon_and_polygon2(self):
        """the second test for projection of a given polygon on another
        polygon with the first one being inside the second one
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol1 = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(-1, -1)
        v8 = shapes.Point(0, -2)
        v9 = shapes.Point(1, -1)
        v10 = shapes.Point(1, 1)
        v11 = shapes.Point(0, 2)
        v12 = shapes.Point(-1, 1)
        pol2 = shapes.Polygon(v7, v8, v9, v10, v11, v12)
        self.assertEqual(operations.projection(pol2, pol1), None)
    
    def test_for_polygon_and_polygon3(self):
        """the third test for projection of a given polygon on another
        given polygon with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol1 = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(1, -1)
        v8 = shapes.Point(2, -2)
        v9 = shapes.Point(3, -1)
        v10 = shapes.Point(3, 1)
        v11 = shapes.Point(2, 2)
        v12 = shapes.Point(1, 1)
        pol2 = shapes.Polygon(v7, v8, v9, v10, v11, v12)
        res = shapes.LineSegment(v3, v4)
        self.assertEqual(operations.projection(pol2, pol1), res)
    
    def test_for_polygon_and_polygon4(self):
        """the fourth test for projection of a given polygon on another
        given polygon with them being apart
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol1 = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(3, -3)
        v8 = shapes.Point(5, -5)
        v9 = shapes.Point(7, -3)
        v10 = shapes.Point(7, 3)
        v11 = shapes.Point(5, 5)
        v12 = shapes.Point(3, 3)
        pol2 = shapes.Polygon(v7, v8, v9, v10, v11, v12)
        res = shapes.LineSegment(v3, v4)
        self.assertEqual(operations.projection(pol2, pol1), res)
    
    def test_for_polygon_and_polygon5(self):
        """the fifth test for projection of a given polygon on another
        given polygon with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol1 = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(1, -1)
        v8 = shapes.Point(2, -2)
        v9 = shapes.Point(3, -1)
        v10 = shapes.Point(3, 1)
        v11 = shapes.Point(2, 2)
        v12 = shapes.Point(1, 1)
        pol2 = shapes.Polygon(v7, v8, v9, v10, v11, v12)
        res = shapes.LineSegment(v3, v4)
        line1 = shapes.LineSegment(v8, v11)
        line2 = shapes.LineSegment(v7, v8)
        line3 = shapes.LineSegment(v7, v12)
        line4 = shapes.LineSegment(v12, v11)
        res = (line1, line2, line3, line4)
        self.assertEqual(operations.projection(pol1, pol2), res)
    
    def test_for_polygon_and_rectangle1(self):
        """the first test for projection of a given polygon on a given
        rectangle with the rectangle being inside the polygon
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(-1, -1)
        v8 = shapes.Point(1, -1)
        v9 = shapes.Point(1, 1)
        v10 = shapes.Point(-1, 1)
        rec = shapes.Rectangle(v7, v8, v9, v10)
        self.assertEqual(operations.projection(pol, rec), rec)
    
    def test_for_polygon_and_rectangle2(self):
        """the second test for projection of a given polygon on a given
        rectangle with the polygon being inside the rectangle
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(-5, -5)
        v8 = shapes.Point(5, -5)
        v9 = shapes.Point(5, 5)
        v10 = shapes.Point(-5, 5)
        rec = shapes.Rectangle(v7, v8, v9, v10)
        self.assertEqual(operations.projection(pol, rec), None)
    
    def test_for_polygon_and_rectangle3(self):
        """the third test for projection of a given polygon on a given
        rectangle with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(1, -2)
        v8 = shapes.Point(3, -2)
        v9 = shapes.Point(3, 2)
        v10 = shapes.Point(1, 2)
        rec = shapes.Rectangle(v7, v8, v9, v10)
        line1 = shapes.LineSegment(v7, v10)
        line2 = shapes.LineSegment(v7, v3)
        line3 = shapes.LineSegment(v10, v4)
        res = (line1, line2, line3)
        self.assertEqual(operations.projection(pol, rec), res)
    
    def test_for_polygon_and_rectangle4(self):
        """the fourth test for projection of a given polygon on a given
        rectangle with them being apart
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        v7 = shapes.Point(3, -1)
        v8 = shapes.Point(6, -1)
        v9 = shapes.Point(6, 1)
        v10 = shapes.Point(3, 1)
        rec = shapes.Rectangle(v7, v8, v9, v10)
        res = shapes.LineSegment(v7, v10)
        self.assertEqual(operations.projection(pol, rec), res)
    
    def test_for_polygon_and_circle1(self):
        """the first test for projection of a given polygon on a given
        circle with the circle being inside the polygon
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        circle = shapes.Circle(shapes.Point(0, 0), 1)
        self.assertEqual(operations.projection(pol, circle), circle)
    
    def test_for_polygon_and_circle2(self):
        """the second test for projection of a given polygon on a given
        circle with the polygon being located inside the circle
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        circle = shapes.Circle(shapes.Point(0, 0), 6)
        self.assertEqual(operations.projection(pol, circle), None)
    
    def test_for_polygon_and_circle3(self):
        """the third test for projection of a given polygon on a given
        circle with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        circle = shapes.Circle(shapes.Point(2, 0), 2)
        res = shapes.Arc(circle, v3, v4)
        self.assertEqual(operations.projection(pol, circle), res)
    
    def test_for_polygon_and_line1(self):
        """the first test for projection of a given polygon on a given
        infinite line with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        line = shapes.Line(0, 0)
        end1 = shapes.Point(-2, 0)
        end2 = shapes.Point(2, 0)
        res = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(pol, line), res)
    
    def test_for_polygon_and_line2(self):
        """the second test for projection of a given polygon on a given
        infinite line with them being apart
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        line = shapes.Line(0, 5)
        end1 = shapes.Point(-2, 5)
        end2 = shapes.Point(2, 5)
        res = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(pol, line), res)
    
    def test_for_polygon_and_linesegment1(self):
        """the first test for projection of a given polygon on a given
        line segment with the line segment being located inside the
        polygon
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        end1 = shapes.Point(0, 0)
        end2 = shapes.Point(1, 1)
        line = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(pol, line), line)
    
    def test_for_polygon_and_linesegment2(self):
        """the second test for projection of a given polyon on a given
        line segment with them intersecting each other
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        end1 = shapes.Point(0, 0)
        end2 = shapes.Point(3, 0)
        line = shapes.LineSegment(end1, end2)
        end3 = shapes.Point(2, 0)
        res = shapes.LineSegment(end1, end3)
        self.assertEqual(operations.projection(pol, line), res)
    
    def test_for_polygon_and_linesegment3(self):
        """the third test for projection of a given polygon on a given
        line segment with them being apart and the polygon being
        located partly in front of the line segment
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        end1 = shapes.Point(0, 5)
        end2 = shapes.Point(5, 5)
        line = shapes.LineSegment(end1, end2)
        end3 = shapes.Point(2, 5)
        res = shapes.LineSegment(end1, end3)
        self.assertEqual(operations.projection(pol, line), res)
    
    def test_for_polygon_and_linesegment4(self):
        """the fourth test for projection of a given polygon on a given
        line segment with them being apart and the polygon not being
        located in front of the line segment
        """
        
        v1 = shapes.Point(-2, -2)
        v2 = shapes.Point(0, -4)
        v3 = shapes.Point(2, -2)
        v4 = shapes.Point(2, 2)
        v5 = shapes.Point(0, 4)
        v6 = shapes.Point(-2, 2)
        pol = shapes.Polygon(v1, v2, v3, v4, v5, v6)
        end1 = shapes.Point(6, 5)
        end2 = shapes.Point(5, 5)
        line = shapes.LineSegment(end1, end2)
        self.assertEqual(operations.projection(pol, line), None)