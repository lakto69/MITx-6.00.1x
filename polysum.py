# -*- coding: utf-8 -*-
"""
ExercÃ­cios da 2Âª Semana do curso
2nd week exercises of the course
"""
import math

def polysum(n, s):
    """:arg:n = int, number of sides of a regular polygon;
            s = float, side's length;

        out: float (4 decimal places), sum the area and square of the perimeter of the regular polygon."""

    perimetro = n * s
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    return round(area + (perimetro ** 2), 4)

