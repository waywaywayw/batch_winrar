# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/24
"""
import os
import re
import numpy as np
import pandas as pd
from atools_python.files import discard_duplicate_folder

if __name__ == "__main__":
    # file_path = os.path.join('D:\\', 'abfc')
    file_path = os.path.join('D:\\', '搜狗高速下载', 'OneDrive_1_2018-10-23')
    discard_duplicate_folder(file_path)