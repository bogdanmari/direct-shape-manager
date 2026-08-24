# -*- coding: utf-8 -*-
from Autodesk.Revit import DB

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

GENERIC_MODEL_CAT_ID = DB.ElementId(DB.BuiltInCategory.OST_Entourage)
GEOMETRY_OPTIONS = __revit__.ActiveUIDocument.Application.Application.Create.NewGeometryOptions()

def get_bottom_lines(geometry):
    returned_lines = []
    min_Z = 100000
    for line in geometry:
        if not line.Direction.Z == 1 or not line.Direction.Z == -1:
            if line.Origin.Z < min_Z:
                min_Z = line.Origin.Z
    for line in geometry:
        if line.Direction.Z == 1 or line.Direction.Z == -1:
            pass
        else:
            if line.Origin.Z == min_Z:
                returned_lines.append(line)
    return returned_lines

def __is_XYZ_equal(xyz1, xyz2):
    return all([xyz1.X == xyz2.X, xyz1.Y == xyz2.Y, xyz1.Z == xyz2.Z])

def __is_XYZ_in_list(xyz, _list):
    return any([__is_XYZ_equal(xyz, i) for i in _list])

def get_unique_points(lines):
    returned_points = []
    rounded_points = []
    for line in lines:
        for point in line.Tessellate():
            rounded_points.append(DB.XYZ(round(point.X, 3), round(point.Y, 3), round(point.Z, 3)))
    for point in rounded_points:
        if not __is_XYZ_in_list(point, returned_points):
            returned_points.append(point)
    return returned_points

def __get_distance(point1, point2):
    return ((point1.X - point2.X) ** 2 + (point1.Y - point2.Y) ** 2) ** 0.5

# def sorted_points(points):
#     if len(points) < 4:
#         print("Недостаточно точек для построения прямоугольника")
#         print(len(points))
#         return []

#     first_point = points[0]
#     m = 10000000
#     for p in points[1:]:
#         d = __get_distance(first_point, p)
#         if d < m:
#             m = d
#             second_point = p
#     points.remove(first_point)
#     points.remove(second_point)
#     m = 10000000
#     for p in points:
#         d = __get_distance(second_point, p)
#         if d < m:
#             m = d
#             third_point = p
#     points.remove(third_point)
#     last_point = points[0]
#     return (first_point, second_point, third_point, last_point)

def sorted_points(points):
    if len(points) < 4:
        print("Недостаточно точек для построения прямоугольника")
        print(len(points))
        return []

    first_point = points[0]
    third_point = None
    _max_distance = 0
    for point in points[1:]:
        if __get_distance(point, first_point) > _max_distance:
            third_point = point
    points.remove(first_point)
    points.remove(third_point)
    second_point, last_point = points
    return (first_point, second_point, third_point, last_point)

def get_height(geometry):
    for line in geometry:
        if line.Direction.Z == 1 or line.Direction.Z == -1:
            return line.Length

def create_scope_geometry(scope_box):
    scope_box_geometry = scope_box.get_Geometry(GEOMETRY_OPTIONS)
    plane_lines = get_bottom_lines(scope_box_geometry)
    height = get_height(scope_box_geometry)
    unique_points = get_unique_points(plane_lines)
    p = sorted_points(unique_points)

    line1 = DB.Line.CreateBound(p[0], p[1])
    line2 = DB.Line.CreateBound(p[1], p[2])
    line3 = DB.Line.CreateBound(p[2], p[3])
    line4 = DB.Line.CreateBound(p[3], p[0])
    lines = [line1, line2, line3, line4]
    curveloop = DB.CurveLoop.Create(lines)
    solid = DB.GeometryCreationUtilities.CreateExtrusionGeometry([curveloop,], DB.XYZ.BasisZ, height)

    ds = DB.DirectShape.CreateElement(doc, GENERIC_MODEL_CAT_ID)
    ds.SetShape([solid])
    ds.Name = scope_box.Name
    return ds

patterns = DB.FilteredElementCollector(doc).OfClass(DB.FillPatternElement).ToElements()
for pattern in patterns:
    if pattern.Name == "<Сплошная заливка>" or pattern.Name == "<Solid fill>":
        break
pattern = pattern
scope_boxes = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_VolumeOfInterest).ToElements()
direct_shapes = DB.FilteredElementCollector(doc, doc.ActiveView.Id).OfCategoryId(GENERIC_MODEL_CAT_ID).ToElements()

if __name__ == "__main__":
    pass