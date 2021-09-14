#!/usr/bin/env python
# encoding=utf8         # 开头注释，说明源程序所用编码
import os.path

import pcl
import numpy as np


def bin2pcd(bin_path, save_path, file_name):

    points = np.fromfile(bin_path, dtype="float32").reshape((-1, 4))
    print(points)
    print(points.shape)
    # 载入所有点
    pcd = pcl.PointCloud_PointXYZI()
    pcd.from_array(points)
    # 输出文件的文件名
    pcd_file = os.path.join(save_path, file_name+'.pcd')
    # 保存 .pcd 文件
    pcd._to_pcd_file(pcd_file, False)

