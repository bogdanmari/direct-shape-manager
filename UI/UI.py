# -*- coding: utf-8 -*-
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import *
from System import EventHandler

class MainForm(Form):
    def __init__(self):
        self.state = None
        self.state_text = None

        self.Size = Size(400, 300)
        self.StartPosition = FormStartPosition.CenterParent
        self.Text = "SynSys : Direct Shapes Creator"
        self.FormBorderStyle = FormBorderStyle.FixedSingle
        self.ControlBox = False
        self.BackColor = SystemColors.ControlLightLight
        self.Font = Font("Arial Narrow", 12, FontStyle.Regular)

        self.btn1 = Button()
        self.btn1.Size = Size(345, 50)
        self.btn1.Location = Point(20, 20)
        self.btn1.Text = "Create Direct Shapes based on Scope Boxes"
        self.btn1.Click += EventHandler(self.btn_click)
        self.btn1.FlatStyle = FlatStyle.Flat
        self.Controls.Add(self.btn1)

        self.btn2 = Button()
        self.btn2.Size = Size(345, 50)
        self.btn2.Location = Point(20, 80)
        self.btn2.Text = "Colorize Direct Shapes"
        self.btn2.Click += EventHandler(self.btn_click)
        self.btn2.FlatStyle = FlatStyle.Flat
        self.Controls.Add(self.btn2)

        self.btn3 = Button()
        self.btn3.Size = Size(345, 50)
        self.btn3.Location = Point(20, 140)
        self.btn3.Text = "Create Direct Shapes based on Rooms"
        self.btn3.Click += EventHandler(self.btn_click)
        self.btn3.FlatStyle = FlatStyle.Flat
        self.Controls.Add(self.btn3)  

        self.btn4 = Button()
        self.btn4.Size = Size(70, 25)
        self.btn4.Location = Point(295, 220)
        self.btn4.Text = "Cancel"
        self.btn4.Click += EventHandler(self.btn_cancel)
        self.btn4.FlatStyle = FlatStyle.Flat
        self.Controls.Add(self.btn4)

        self.logo = PictureBox()
        self.logo.ImageLocation = r"Z:\04_Работа\Synergy Systems\00_Плагины pyRevit\bimcoord.extension\bimcoord.tab\For Testing.panel\DirectShapesManager.pushbutton\UI\Logo.png"
        self.logo.Location = Point(10, 210)
        self.logo.SizeMode = PictureBoxSizeMode.AutoSize
        self.Controls.Add(self.logo)

    def btn_click(self, sender, e):
        if sender.Text == "Create Direct Shapes based on Scope Boxes":
            self.state = 1
        elif sender.Text == "Colorize Direct Shapes":
            self.state = 2
        elif sender.Text == "Create Direct Shapes based on Rooms":
            self.state = 3
        self.state_text = sender.Text
        self.Close()

    def btn_cancel(self, sender, e):
        self.Close()


