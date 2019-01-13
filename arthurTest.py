#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

In this example, we lay out widgets using
absolute positioning.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(400, 600))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour("white")

        self.LoadImages()

        self.logo.SetPosition((20, 20))


    def LoadImages(self):

        self.logo = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("Images/Logo.png", wx.BITMAP_TYPE_ANY))


def main():

    app = wx.App()
    ex = Example(None, title='Concussion Test')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# # moving.py

# import wx


# class MyFrame(wx.Frame):

# 	def __init__(self, parent, title):
# 		super(MyFrame, self).__init__(parent, title=title,
# 		    size=(400, 600))
# 		self.Centre()
		
# class HomePage(wx.Panel):
# 	def __init__(self, parent):



# def  main():
#     app = wx.App()
#     frame = MyFrame(None, title='Concussion Test')
#     panelHome = wx.Panel(frame, wx.ID_ANY)


#     wx.StaticBitmap(panelHome, -1, wx.Bitmap("Images/Logo.png", wx.BITMAP_TYPE_ANY), pos=(0,0))


#     frame.Show()
#     app.MainLoop()




# if __name__ == '__main__':
#     main()


# import os
# import wx


# class MainWindow(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(200,100))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.CreateStatusBar() # A StatusBar in the bottom of the window

#         # Setting up the menu.
#         filemenu= wx.Menu()

#         # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
#         menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
#         menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

#         # Creating the menubar.
#         menuBar = wx.MenuBar()
#         menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
#         self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

#         # Set events.
#         self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
#         self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

#         self.Show(True)

#     def OnAbout(self,e):
#         # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
#         dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
#         dlg.ShowModal() # Show it
#         dlg.Destroy() # finally destroy it when finished.

#     def OnExit(self,e):
#         self.Close(True)  # Close the frame.

# app = wx.App(False)
# frame = MainWindow(None, "Sample editor")
# app.MainLoop()


# # #!/usr/bin/env python3
# # import wx
# # class MainFrame(wx.Frame):
# # 	""" Making a class of a frame """
# # 	def OnAbout(self, event):
# # 		print("About")

# # 	def __init__(self, parent, title):
# # 		wx.Frame.__init__(self, parent, title=title, size=(200,100))
# # 		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

# # 		self.CreateStatusBar() # A Statusbar in the bottom of the window

# # 		# Setting up the menu.
# # 		filemenu = wx.Menu()

# # 		# wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
# # 		menuItem = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
# # 		self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)

# # 		filemenu.AppendSeparator()
# # 		filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

# # 		# Creating the menubar.
# # 		menuBar = wx.MenuBar()
# # 		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
# # 		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

# # 		self.Show(True) # Show the frame.

# # app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
# # frame = MainFrame(None, 'Hello World') # A Frame is a top-level window. 
# # app.MainLoop()