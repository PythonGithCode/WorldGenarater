
import math


def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points



def get_line_with_ext(x1, y1, x2, y2, origin_x, origin_y, rotation_degrees, pov_degrees, pov_change):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    # Apply rotation transformation
    angle_radians = math.radians(rotation_degrees)
    x1_new = (x1 - origin_x) * math.cos(angle_radians) - (y1 - origin_y) * math.sin(angle_radians) + origin_x
    y1_new = (x1 - origin_x) * math.sin(angle_radians) + (y1 - origin_y) * math.cos(angle_radians) + origin_y
    x2_new = (x2 - origin_x) * math.cos(angle_radians) - (y2 - origin_y) * math.sin(angle_radians) + origin_x
    y2_new = (x2 - origin_x) * math.sin(angle_radians) + (y2 - origin_y) * math.cos(angle_radians) + origin_y
    # Apply POV transformation
    pov_radians = math.radians(pov_degrees)
    x1_new += pov_change * math.cos(pov_radians)
    y1_new += pov_change * math.sin(pov_radians)
    x2_new += pov_change * math.cos(pov_radians)
    y2_new += pov_change * math.sin(pov_radians)
    deltax = x2_new - x1_new
    deltay = abs(y2_new-y1_new)
    error = int(deltax / 2)
    y = y1_new
    ystep = None
    if y1_new < y2_new:
        ystep = 1
    else:
        ystep = -1
    for x in range(int(x1_new), int(x2_new) + 1):
        if issteep:
            points.append((int(y), x))
        else:
            points.append((x, int(y)))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points



