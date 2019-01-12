#!/usr/bin/env python3
import wx
class MainFrame(wx.Frame):
	""" Making a class of a frame """
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(200,100))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

		self.CreateStatusBar() # A Statusbar in the bottom of the window

		# Setting up the menu.
		filemenu = wx.Menu()

		# wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
		filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
		filemenu.AppendSeparator()
		filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

		# Creating the menubar.
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

		self.Show(True) # Show the frame.

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MainFrame(None, 'Hello World') # A Frame is a top-level window. 
app.MainLoop()