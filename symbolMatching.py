import wx

LENGTH = 400
WIDTH = 600

class Instructions(wx.Panel):
    def __init__(self, parent):
        super(Instructions, self).__init__(parent)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Symbol Matching: Part 1")
        st1.SetFont(font)
        hbox1.Add(st1, wx.ALIGN_CENTER)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)

        vbox.Add((-1, 125))

        st2 = wx.StaticText(self, label="Nine boxes have a shape inside, and each is numbered. A single shape appears below, and you have to click the number of the box that matches it.")
        st2.SetFont(font)
        st2.Wrap(275)
        vbox.Add(st2, flag=wx.ALIGN_CENTER | wx.ALL, border=25)

        vbox.Add((-1, 150))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label="I Understand", size=(100, 30))
        hbox2.Add(btn1)
        vbox.Add(hbox2, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vbox)

class PartOne(wx.Panel):
    def __init__(self, parent):
        super(PartOne, self).__init__(parent)

class PartTwo(wx.Panel):
    def __init__(self, parent):
        super(PartTwo, self).__init__(parent)

class SymbolMatching(wx.Frame):
    def __init__(self, parent, title):
        super(SymbolMatching, self).__init__(parent, title=title,
                                             size=(400, 600))
        self.Centre()

        self.panels = {
            "instructions": Instructions(self),
            "partOne": PartOne(self),
            "partTwo": PartTwo(self)
        }

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        for panel in self.panels.values():
            self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def switchPanels(self, event, panelName):
        for name, panel in self.panels.items():
            if name != panelName:
                panel.Hide()
        self.panels.get(panelName).Show()


app = wx.App()
gui = SymbolMatching(None, title="Concussion Test: Symbol Matching")
gui.Show()
app.MainLoop()
