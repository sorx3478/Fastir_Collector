from __future__ import unicode_literals
from memory.mem import _Memory


class Windows2008ServerMemory(_Memory):
    def __init__(self, params):
        super(Windows2008ServerMemory, self).__init__(params)

    def csv_all_modules_dll(self):
        super(Windows2008ServerMemory, self)._csv_all_modules_dll()

    def csv_all_modules_opened_files(self):
        super(Windows2008ServerMemory, self)._csv_all_modules_opened_files()

    def json_all_modules_dll(self):
        super(Windows2008ServerMemory, self)._json_all_modules_dll()

    def json_all_modules_opened_files(self):
        super(Windows2008ServerMemory, self)._json_all_modules_opened_files()