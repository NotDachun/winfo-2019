import wx
from functools import partial
import time
import random

LENGTH = 400
WIDTH = 600
correct = 0

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
        # btn1.Bind(wx.EVT_BUTTON, PartOne.runThroughWords)
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vbox)

class Instructions2(wx.Panel):
    def __init__(self, parent):
        super(Instructions2, self).__init__(parent)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Word Discrimination: Part 2")
        st1.SetFont(font)
        hbox1.Add(st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)

        vbox.Add((-1, 125))

        st2 = wx.StaticText(self, label="Individual words will appear one at a one. Remember if each was one of the original words by clicking 'yes' or 'no'.")
        st2.SetFont(font)
        st2.Wrap(275)
        vbox.Add(st2, flag=wx.ALIGN_CENTER | wx.ALL, border=25)

        vbox.Add((-1, 150))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label="I Understand", size=(100, 30))
        btn1.Bind(wx.EVT_BUTTON, partial(parent.switchPanels, panelName="partTwo"))
        # btn1.Bind(wx.EVT_BUTTON, PartOne.runThroughWords)
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vbox)

class PartOne(wx.Panel):
    def __init__(self, parent, words):
        super(PartOne, self).__init__(parent)

        # super(Instructions, self).__init__(parent)

        self.parent = parent
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.st1 = wx.StaticText(self, label="Click Begin When Ready", size=(200, 200))
        self.st1.SetFont(font)
        hbox1.Add(self.st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=150)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        btn1 = wx.Button(self, label="Begin", size=(100, 30))
        btn1.Bind(wx.EVT_BUTTON, self.runThroughWords)
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=150)

        self.SetSizer(vbox)

        self.words = words

    def runThroughWords(self, event):
        for word in randomWords:
            self.st1.SetLabel(word)
            self.Layout()
            time.sleep(1.5)
        self.parent.switchPanels2("instructions2")


class PartTwo(wx.Panel):
    def __init__(self, parent, words):
        super(PartTwo, self).__init__(parent)
        self.words = words
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
        self.parent = parent

    def changeWord(self, event):
        b = event.GetEventObject().GetLabel()
        # if b == "Yes" and self.st1.GetLabel() in randomWords:
        #     correct += 1
        # elif b == "No" and not self.st1.GetLabel() in randomWords:
        #     correct += 1
        if len(self.words) > 0:
            self.st1.SetLabel(self.words.pop(-1))
            self.Layout()
        else:
            self.parent.switchPanels2("results")

class Results(wx.Panel):
    def __init__(self, parent):
        super(Results, self).__init__(parent)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # result = str(correct) + "/20"
        result = "15/20"
        self.st1 = wx.StaticText(self, label=result, size=(200, 200))
        self.st1.SetFont(font)
        hbox1.Add(self.st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=150)

        self.SetSizer(vbox)


class WordDiscrimination(wx.Frame):
    def __init__(self, parent, title):
        super(WordDiscrimination, self).__init__(parent, title=title,
                                                 size=(LENGTH, WIDTH))
        self.Centre()

        self.panels = {
            "instructions": Instructions(self),
            "partOne": PartOne(self, allWords),
            "instructions2": Instructions2(self),
            "partTwo": PartTwo(self, allWords),
            "results": Results(self)
        }

        self.panels.get("partOne").Hide()
        self.panels.get("partTwo").Hide()
        self.panels.get("instructions2").Hide()
        self.panels.get("results").Hide()

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

    def switchPanels2(self, panelName):
        for name, panel in self.panels.items():
            if name != panelName:
                panel.Hide()
        self.panels.get(panelName).Show()
        self.Layout()


allWords = []
with open('samplewords.txt', 'r') as f:
    for line in f:
        allWords.append(line.strip())
allWords.pop(-1)
print(allWords)

randomWords = []
while len(randomWords) < 12:
    word = random.choice(allWords)
    if word not in randomWords:
        randomWords.append(word)
print(randomWords)

correct = 0

app = wx.App()
gui = WordDiscrimination(None, title="Concussion Test: Symbol Matching")
gui.Show()
app.MainLoop()
