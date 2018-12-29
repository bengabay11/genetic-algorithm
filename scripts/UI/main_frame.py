from wx.core import wx
from original_image_panel import OriginalImagePanel
from new_image_panel import NewImagePanel
from scripts import configuration


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, size=configuration.FRAME_SIZE)

        self.Center()

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(configuration.ICON__PATH))
        self.SetIcon(icon)

        splitter = wx.SplitterWindow(self)
        self.original_image_panel = OriginalImagePanel(splitter)
        self.new_image_panel = NewImagePanel(splitter)
        splitter.SplitVertically(self.original_image_panel, self.new_image_panel)
        splitter.SetSashGravity(configuration.IMAGES_RATIO)
