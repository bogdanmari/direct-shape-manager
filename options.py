# -*- coding: utf-8 -*-
import Autodesk.Revit.DB.Color as Color
map_of_color = {
"SB B1-1" : Color(250, 128, 114),
"SB B1-2" : Color(250, 128, 114),
"SB B1-3" : Color(250, 128, 114),
"SB B1-4" : Color(250, 128, 114),
"SB B1-5" : Color(250, 128, 114),
"SB B1-6" : Color(250, 128, 114),
"SB B1-7" : Color(250, 128, 114),
"SB B1-8" : Color(250, 128, 114),
"SB B2-1" : Color(50, 205, 50),
"SB B2-2" : Color(50, 205, 50),
"SB C2-1" : Color(255, 20, 147),
"SB C2-2" : Color(255, 20, 147),
"SB D1-1" : Color(128, 128, 0),
"SB D1-2" : Color(128, 128, 0),
"SB D1-3" : Color(128, 128, 0),
"SB D1-4" : Color(128, 128, 0),
"SB D1-5" : Color(128, 128, 0),
"SB D2-1" : Color(102, 205, 170),
"SB D2-2" : Color(102, 205, 170),
"SB D2-3" : Color(102, 205, 170),
"SB D2-4" : Color(102, 205, 170),
"SB D2-5" : Color(102, 205, 170),
"SB A" : Color(255, 0, 0)
}

def is_contain(name):
    for i in map_of_color.keys():
        if i in name:
            return i
    return name