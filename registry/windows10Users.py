from __future__ import unicode_literals
from registry.reg import _Reg
import os
import datetime
from utils.utils import get_json_writer,write_list_to_csv

class Windows10UserReg(_Reg):
    def __init__(self, params):
        _Reg.__init__(self, params)
        _Reg.init_win_vista_and_above(self)


    def csv_open_save_mru(self):
        super(Windows10UserReg, self)._csv_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU")

    def csv_user_assist(self):
        super(Windows10UserReg, self)._csv_user_assist(0, True)

    def csv_networks_list(self):
        super(Windows10UserReg, self)._csv_networks_list(r'Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')

    def csv_shell_forders(self):
        super(Windows10UserReg, self)._csv_shell_forders(
            r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\')

    def json_open_save_mru(self):
        super(Windows10UserReg, self)._json_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU")

    def json_user_assist(self):
        super(Windows10UserReg, self)._json_user_assist(-6, True)

    def json_networks_list(self):
        super(Windows10UserReg,self)._json_networks_list(r'Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')

    def json_shell_forders(self):
        super(Windows10UserReg,self)._json_shell_forders(r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\')
