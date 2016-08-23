from __future__ import unicode_literals
from registry.reg import _Reg


class Windows2012ServerR2UserReg(_Reg):
    def __init__(self, params):
        _Reg.__init__(self, params)
        _Reg.init_win_vista_and_above(self)

    def csv_open_save_mru(self):
        super(Windows2012ServerR2UserReg, self)._csv_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU")

    def csv_user_assist(self):
        super(Windows2012ServerR2UserReg, self)._csv_user_assist(0, True)

    def csv_networks_list(self):
        super(Windows2012ServerR2UserReg, self)._csv_networks_list(
            r'Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')

    def json_open_save_mru(self):
        super(Windows2012ServerR2UserReg, self)._json_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU")

    def json_user_assist(self):
        super(Windows2012ServerR2UserReg, self)._json_user_assist(0, True)

    def json_networks_list(self):
        super(Windows2012ServerR2UserReg, self)._json_networks_list(
            r'Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')