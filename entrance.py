# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/19
"""
import os
import zipfile
import re
import numpy as np
import pandas as pd

need_path = os.path.join('D:\\', 'BaiduNetdiskDownload', 'SFC-PR')
yuhold = 8
rar_suffix = ['rar', '7z', 'zip', 'tar']
filter_name = ['更多福利.zip']


def is_rar(file):
    suffix = file.split('.')[-1]
    for suf in rar_suffix:
        if suffix.find(suf) >= 0:
            return True
    return False


def main():
    # 1.扫描指定路径下所有的压缩文件(rar, 7z, zip等)    [深入每个子目录, 不深入子目录]，获取所有压缩文件路径。

    need_files = []
    for root, dirs, files in os.walk(need_path, topdown=False):
        if root !=need_path and (len(dirs)+len(files))>=yuhold:
            print('路径 {}, 共有文件夹 {} 个， 文件 {} 个。已跳过该文件夹'.format(root, len(dirs), len(files)))
            continue
        for name in files:
            if is_rar(name) and name not in filter_name:
                print('>>>>>>>>>>>>>>>> 发现了压缩文件，路径：{}'.format(os.path.join(root, name)))
                need_files.append(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))

    # 2.将压缩文件就地解压到所在文件夹。（争取显示进度；如果解压错误，给出提示；）
    for file in need_files:
        z = zipfile.ZipFile(file, 'r')
        file_no_suffix = file.split('.')[:-1]
        rar_file = '.'.join(file_no_suffix)
        print('开始解压文件：', file)
        try:
            z.extractall(path=rar_file, pwd=b'sifangclub.net')
            print('解压成功~')
        except Exception as e:
            print('解压失败！错误原因：')
            print(e)
        z.close()

        # 3.验证（解压后的文件夹大小必须大于压缩文件大小！）并报告解压结果。


if __name__ == "__main__":
    main()
