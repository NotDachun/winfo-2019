import wx
from functools import partial
import time
import random

LENGTH = 400
WIDTH = 600

class Instructions(wx.Panel):
    def __init__(self, parent):
        super(Instructions, self).__init__(parent)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Word Discrimination: Part 1")
        st1.SetFont(font)
        hbox1.Add(st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)

        vbox.Add((-1, 125))

        st2 = wx.StaticText(self, label="One at a time, 12 random, simple words appear for 1.5 seconds apiece. Then the same 12 words appear again for 1.5 seconds")
        st2.SetFont(font)
        st2.Wrap(275)
        vbox.Add(st2, flag=wx.ALIGN_CENTER | wx.ALL, border=25)

        vbox.Add((-1, 150))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label="I Understand", size=(100, 30))
        btn1.Bind(wx.EVT_BUTTON, partial(parent.switchPanels, panelName="partOne"))
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vbox)

class PartOne(wx.Panel):
    def __init__(self, parent):
        super(PartOne, self).__init__(parent)

        st1 = wx.StaticText(self, label="Hi")

class PartTwo(wx.Panel):
    def __init__(self, parent):
        super(PartTwo, self).__init__(parent)

        st1 = wx.StaticText(self, label="Hi 2")


class WordDiscrimination(wx.Frame):
    def __init__(self, parent, title):
        super(WordDiscrimination, self).__init__(parent, title=title,
                                                 size=(400, 600))
        self.Centre()

        self.panels = {
            "instructions": Instructions(self),
            "partOne": PartOne(self),
            "partTwo": PartTwo(self)
        }

        self.panels.get("partOne").Hide()
        self.panels.get("partTwo").Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        for panel in self.panels.values():
            self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def switchPanels(self, event, panelName):
        for name, panel in self.panels.items():
            if name != panelName:
                panel.Hide()
        self.panels.get(panelName).Show()
        self.Layout()


app = wx.App()
gui = WordDiscrimination(None, title="Concussion Test: Symbol Matching")
gui.Show()
app.MainLoop()
