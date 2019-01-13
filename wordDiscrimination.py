import wx
from functools import partial
import time
import random

LENGTH = 400
WIDTH = 600

class Instructions(wx.Panel):
    def __init__(self, parent, directions):
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

        st2 = wx.StaticText(self, label=directions)
        st2.SetFont(font)
        st2.Wrap(275)
        vbox.Add(st2, flag=wx.ALIGN_CENTER | wx.ALL, border=25)

        vbox.Add((-1, 150))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label="I Understand", size=(100, 30))
        btn1.Bind(wx.EVT_BUTTON, partial(parent.switchPanels, panelName="partTwo"))
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vbox)

class PartOne(wx.Panel):
    def __init__(self, parent, words):
        super(PartOne, self).__init__(parent)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Hi")
        st1.SetFont(font)
        hbox1.Add(st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=50)

        self.SetSizer(vbox)

class PartTwo(wx.Panel):

    def __init__(self, parent, words):
        super(PartTwo, self).__init__(parent)
        self.words = words
        print(words)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st1 = wx.StaticText(self, label=self.words.pop(-1))
        self.st1.SetFont(font)
        hbox2.Add(self.st1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=150)

        vbox.Add((-1, 300))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label="Yes", size=(150, 70))
        btn1.Bind(wx.EVT_BUTTON, self.changeWord)
        hbox1.Add(btn1)
        btn2 = wx.Button(self, label="No", size=(150, 70))
        btn2.Bind(wx.EVT_BUTTON, self.changeWord)
        hbox1.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=10)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_BOTTOM)

        self.SetSizer(vbox)

    def changeWord(self, event):
        self.st1.SetLabel(self.words.pop(-1))
        self.Layout()


class WordDiscrimination(wx.Frame):
    def __init__(self, parent, title):
        super(WordDiscrimination, self).__init__(parent, title=title,
                                                 size=(400, 600))
        self.Centre()

        self.panels = {
            "instructions": Instructions(self, "One at a time, 12 random, simple words appear for 1.5 seconds apiece. Then the same 12 words appear again for 1.5 seconds"),
            "partOne": PartOne(self, allWords),
            "instructions2": Instructions(self, "Individual words will appear one at a one. Remember if each was one of the original words by clicking 'yes' or 'no'."),
            "partTwo": PartTwo(self, allWords)
        }

        self.panels.get("partOne").Hide()
        self.panels.get("partTwo").Hide()
        self.panels.get("instructions2").Hide()

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


allWords = []
with open('samplewords.txt', 'r') as f:
    for line in f:
        allWords.append(line.strip())
print(allWords.pop())

app = wx.App()
gui = WordDiscrimination(None, title="Concussion Test: Symbol Matching")
gui.Show()
app.MainLoop()
