import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='This is the title of my GUI')
        self.Show()
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Press here')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn,0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print('You didn\'t write anything')
        else:
            print(f'{value}? Same for you!')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()