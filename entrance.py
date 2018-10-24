# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/19
"""
import os
import time
from atools_python.z7.z7 import z7_extract

# need_path = os.path.join('D:\\', 'BaiduNetdiskDownload', 'SFC-PR')
need_path = os.path.join('D:\\', 'BaiduNetdiskDownload', '二次元狂热少女')
yuhold = 8
rar_suffix = ['rar', '7z', 'zip', 'tar']
filter_name = ['更多福利.zip', '更多福利必读']


def is_rar(file):
    suffix = file.split('.')[-1]
    for suf in rar_suffix:
        if suffix.find(suf) >= 0:
            return True
    return False


def folder_size(folder_path):
    floder_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            floder_size += os.path.getsize(os.path.join(root, file))
    return floder_size


def main():
    # 1.扫描指定路径下所有的压缩文件(rar, 7z, zip等)    [深入每个子目录, 不深入子目录]，获取所有压缩文件路径。

    need_files = []
    for root, dirs, files in os.walk(need_path, topdown=False):
        if root !=need_path and (len(dirs)+len(files))>=yuhold:
            # print('路径 {}, 共有文件夹 {} 个， 文件 {} 个。已跳过该文件夹'.format(root, len(dirs), len(files)))
            continue
        for name in files:  # 处理文件
            if is_rar(name) and name not in filter_name:
                print('>>>>>>>>>>>>>>>> 发现了压缩文件，路径：{}'.format(os.path.join(root, name)))
                need_files.append(os.path.join(root, name))
        # for name in dirs:   # 处理文件夹
            # if name == '更多福利必读':
            #     cmd = 'del {}'.format(os.path.join(root, name))
            #     os.system(cmd)
            #     print('删掉目录 ', os.path.join(root, name))
        #     print(os.path.join(root, name))
    print('发现的压缩文件数量：', len(need_files))

    # 2.将压缩文件就地解压到所在文件夹。（争取显示进度；如果解压错误，给出提示；）
    # pwd = 'sifangclub.net'
    pwd = '123'
    for rar_file in need_files:
        file_no_suffix = rar_file.split('.')[:-1]
        output_path = '.'.join(file_no_suffix)
        # 如果已解压过，并且大于1M。那么就不解压了
        if os.path.exists(output_path):
            output_path_size = folder_size(output_path)
            rar_file_size = os.path.getsize(rar_file)*0.9
            if output_path_size >= rar_file_size:    # （可选）
                print('发现文件夹 {}，并且大于压缩文件。不再解压'.format(output_path))
                cmd = 'del {}'.format(rar_file)
                os.system(cmd)
                print('删除原始压缩文件完毕')
                continue
                # break
        try:
            print('开始解压文件：', rar_file)
            start_time = time.time()
            z7_extract(rar_file, output_path, pwd, verbose=True)
            cost_time = time.time() - start_time
            print('解压成功~ 耗时 {} 秒（{} 分钟）'.format(cost_time, cost_time/60))
        except Exception as e:
            print('解压失败！错误原因：')
            print(e)
        # z.close()


if __name__ == "__main__":
    main()
