# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/22
"""
import os
import re
import sys
sys.path.append('..')
# from atools_NLP.files import readlines_from_file





# 下载地址：https://www.7-zip.org/download.html
z7_path = os.path.join('7z.exe')


def readlines_from_file(input_path, encoding='utf8'):
    ret_list = []
    with open(input_path, 'r', encoding=encoding) as fin:
        for line in fin:
            ret_list.append(line.strip())
    return ret_list


def z7_cmd(rar_file, output_path, pwd=None, verbose=True):
    """
    """
    # bse0 表示不显示错误输出；aoa 表示覆盖已有文件；y表示所有选项都点同意
    cmd = '{} x {} -y -o{} -aoa -bse0 '.format(z7_path, rar_file, output_path)

    # 处理密码的情况
    res = None
    if isinstance(pwd, list):
        for p in pwd:
            if p is not None:
                t_cmd = cmd + '-p{} '.format(p)
                res = os.popen(t_cmd)
                print(res.read())
                if res==0 :
                    break
    elif pwd is not None:
        cmd += '-p{} '.format(pwd)
        res = os.system(cmd)
    return res


def file_no_suffix(file_path):
    file_no_suffix = file_path.split('.')[:-1]
    output_path = '.'.join(file_no_suffix)
    return output_path


if __name__ == '__main__':
    input_path = os.path.join('D:\\', 'BaiduNetdiskDownload', '预览图带名字.zip')
    passwd_path = os.path.join('passwd.txt')

    passwd = readlines_from_file(passwd_path)
    ret = z7_cmd(input_path, file_no_suffix(input_path), passwd)
    print('解压命令返回值:', ret)