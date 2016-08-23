from __future__ import unicode_literals
from registry.reg import _Reg


class Windows2003ServerUserReg(_Reg):
    def __init__(self, params):
        _Reg.__init__(self, params)
        _Reg.init_win_xp(self)

    def csv_open_save_mru(self):
        super(Windows2003ServerUserReg, self)._csv_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU")

    def csv_user_assist(self):
        super(Windows2003ServerUserReg, self)._csv_user_assist(-6, False)

    def json_open_save_mru(self):
        super(Windows2003ServerUserReg, self)._json_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU")

    def json_user_assist(self):
        super(Windows2003ServerUserReg, self)._json_user_assist(-6, False)