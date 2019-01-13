import wx
 
def onButton(event):
    print ("Button pressed.")


frameWidth = 400;
frameHeight = 600;
app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,400, 600)
panel = wx.Panel(frame, wx.ID_ANY)

 
bmp1 = wx.Bitmap("Images/Logo.png", wx.BITMAP_TYPE_ANY)
button1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp1,
                          size=(bmp1.GetWidth()-350, bmp1.GetHeight()-350))

bmp2 = wx.Bitmap("Images/Logo.png", wx.BITMAP_TYPE_ANY)
button2 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp2,
                          size=(bmp2.GetWidth()-350, bmp2.GetHeight()-350))                          

bmp3 = wx.Bitmap("Images/Logo.png", wx.BITMAP_TYPE_ANY)
button3 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp3,
                          size=(bmp3.GetWidth()-350, bmp3.GetHeight()-350))

png = wx.Image("Images/Logo.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
wx.StaticBitmap(panel, -1, png, (frameWidth / 13 + 1.5 * button1.Size.GetWidth(), frameHeight - 300), (png.GetWidth()-350, png.GetHeight()-350))

button1.Bind(wx.EVT_BUTTON, onButton)
button1.SetPosition((frameWidth / 13, frameHeight / 5))

button2.Bind(wx.EVT_BUTTON, onButton)
button2.SetPosition((frameWidth / 13 + 1.5 * button1.Size.GetWidth(), frameHeight / 5))

button3.Bind(wx.EVT_BUTTON, onButton)
button3.SetPosition((frameWidth / 13 + 3 * button1.Size.GetWidth() , frameHeight / 5))



frame.Show()
frame.Centre()
app.MainLoop()