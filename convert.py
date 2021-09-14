#!/usr/bin/env python
# encoding=utf8         # 开头注释，说明源程序所用编码

import os
import re
import pcl


def convert(pcd_path, save_path, file_name):

    p = re.compile("DATA (?P<data_type>\w*)")
    data_type = "unknow"
    with open(pcd_path, 'rt') as pcl_src_handle:
        lines = pcl_src_handle.readlines()

        for index in range(12):
            m = p.match(lines[index])
            try:
                data_type = m.group("data_type")
                break
            except Exception as e:
                pass

    print(data_type)

    if data_type == "binary":
        print("Convert binary to ascii")
        B = False
    elif data_type == "ascii":
        print("Convert ascii to binary")
        B = True
    else:
        print("Usage: pyton ./BA.py source.pcd dest.pcd")
        print("Usage: pyton ./BA.py source.pcd ascii.pcd")
        print("Usage: pyton ./BA.py ascii.pcd binary.pcd")

    pcl_file = pcl.PointCloud_PointXYZI()
    pcl_file.from_file(pcd_path)
    pcl_file._to_pcd_file(os.path.join(save_path, file_name+'.pcd'), B)