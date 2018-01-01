# coding:utf-8
__author__ = "dfk"
__date__ = "2018/1/1 11:29"

import wx
import os

import shutil
import io


class MainWindow(wx.Frame):
    """
    记事本
    """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # 创建位于窗口的底部的状态栏
        # self.icon = wx.Icon('one.ico', wx.BITMAP_TYPE_ICO)
        # self.SetIcon(self.icon)

        # 设置菜单
        filemenu = wx.Menu()
        # wx.ID_ABOUT 和 wx.ID_EXIT 是wxWidets提供的标准id
        menufile = filemenu.Append(wx.ID_OPEN, '文件', '选择文件')
        menuSave = filemenu.Append(wx.ID_SAVE, '保存', '保存文件')
        menuNew = filemenu.Append(wx.ID_NEW, '新建', '新建文件')
        menuAbout = filemenu.Append(wx.ID_ABOUT, '关于', '关于程序的信息')
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, '退出', '终止应用程序')

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '文件')  # 在菜单栏添加菜单
        self.SetMenuBar(menuBar)  # 在frame中添加菜单栏

        # 设置events
        self.Bind(wx.EVT_MENU, self.OnOpen, menufile)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self, e):
        # 创建一个带“ok”按钮的对话框，wx.ok是wxWidgets提供的标准id
        dlg = wx.MessageDialog(self, "一个小的文本编辑器.",
                               "关于编辑器", wx.OK)  # 语法是（self,内容，标题，id） #这里加不加wx.ok都是一样的效果
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()  # 当结束之后关闭对话框

    def OnExit(self, e):
        self.Close(True)  # 关闭整个frame

    def OnOpen(self, e):
        """打开一个文件"""
        self.dirname = ""
        dlg = wx.FileDialog(self, "选择一个文件", self.dirname, "", "*.*", wx.FD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnNew(self, e):
        dlg = wx.TextEntryDialog(self, '输入文件名', '新建文件')
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetValue() + '.txt'
            file = open(self.filename, 'w+')
            file.write(self.control.GetValue())
            file.close()

    def OnSave(self, e):
        """保存一个文件"""
        try:
            file = open(self.filename, 'w')
            file.write(self.control.GetValue())
            file.close()
        except:
            dlg = wx.TextEntryDialog(self, '输入文件名', '新建文件')
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetValue() + '.txt'
                file = open(filename, 'w+')
                file.write(self.control.GetValue())
                file.close()


app = wx.App(False)
frame = MainWindow(None, "记事本")
app.MainLoop()
"""
在这个例子中，我们生成一个wx.Frame 的子类，并重写它的__init__ 方法。
我们用wx.TextCtrl 来声明一个简单的文本编辑器。
注意，因为在MyFrame.__init__ 中已经运行了self.Show() ，
所以在创建MyFrame的实例之后，就不用再调用frame.Show() 了。
"""
# 添加一个菜单栏Menubar
'''
TIP: wx.ID_ABOUT 和wx.ID_EXIT 是wxWidgets提供的标准ID(查看全部标准ID)。
如果有一个现成的标准ID，最好还是使用它，而不要自定义。
因为这样可以让wxWidgets知道，在不同的平台怎样去显示这个组件，
使它看起来更美观。
'''

'''
wx.EVT_MENU 指代“选择菜单中的项目”这个事件。
wxWidgets 提供了很多的事件，可以点这里查看不完整的列表，
也可以使用下面的代码打印完整的列表。
所有的事件都是wx.Event 的子类。
import wx

for x in dir(wx):
    if x.startswith('EVT_'):
        print x
'''

'''
Note1: 上述代码的菜单项目名称”&About”, “E&xit”, “&File” 中的 “&”是做什么用的？ “&” 的位置也不一样，
分别意味着什么？如果直接print "&About" ，会把 “&” 打印出来。但是在上面的应用程序菜单中看不到 “&”。
而且我试过把 “&”去掉，没有任何变化。谁能帮我解答一下？
'''
