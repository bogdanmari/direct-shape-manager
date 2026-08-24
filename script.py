# -*- coding: utf-8 -*-

__title__ = '''Direct Shapes Manager'''
__doc__ = '''Description'''
__author__ = '''Bogdan Marishchenko'''

from Autodesk.Revit import DB
from UI import UI
from direct_shapes_methods import scope_boxes, create_scope_geometry, direct_shapes, pattern
from options import map_of_color, is_contain

main_form = UI.MainForm()
main_form.ShowDialog()

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

if main_form.state == 1:
    t = DB.Transaction(doc)
    t.Start("SynSys : " + main_form.state_text)
    for scope_box in scope_boxes:
        if "SB" in scope_box.Name:
            ds = create_scope_geometry(scope_box)
            ds.get_Parameter(DB.BuiltInParameter.DOOR_NUMBER).Set(scope_box.Name)
    t.Commit()
elif main_form.state == 2:
    t = DB.Transaction(doc)
    t.Start("SynSys : " + main_form.state_text)
    for direct_shape in direct_shapes:
        name = direct_shape.get_Parameter(DB.BuiltInParameter.DOOR_NUMBER).AsString()
        if map_of_color.get(name) != None:
            color = map_of_color[name]
        else:
            try:
                color = map_of_color[is_contain(name)]
            except:
                continue
        graph = DB.OverrideGraphicSettings()
        graph.SetSurfaceForegroundPatternColor(color)
        graph.SetSurfaceForegroundPatternId(pattern.Id)
        graph.SetSurfaceBackgroundPatternColor(color)
        graph.SetSurfaceBackgroundPatternId(pattern.Id)
        doc.ActiveView.SetElementOverrides(direct_shape.Id, graph)
    t.Commit()
elif main_form.state == 3:
    pass


