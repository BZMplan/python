import wx

app = wx.App()

frame = wx.Frame(None,title = "GUI",pos = (1000,200),size = (500,400))

path_text = wx.TextCtrl (frame,pos = (5,5),size = (350,24))

open_text = wx.Button(frame,label ="打开"，pos = (370))