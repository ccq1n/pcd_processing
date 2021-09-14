#!/usr/bin/env python
# encoding=utf8         # 开头注释，说明源程序所用编码

import numpy as np
import os
import pypcd


def pcd2bin(pcd_path, save_path, file_name):

    if not (os.path.isdir(save_path)):
        os.makedirs(os.path.join(save_path))

    pc = pypcd.PointCloud.from_path(pcd_path)

    ## Generate bin file name
    bin_file_name = "{}.bin".format(file_name)
    bin_file_path = os.path.join(save_path, bin_file_name)

    ## Get data from pcd (x, y, z, intensity, ring, time)
    np_x = (np.array(pc.pc_data['x'], dtype=np.float32)).astype(np.float32)
    np_y = (np.array(pc.pc_data['y'], dtype=np.float32)).astype(np.float32)
    np_z = (np.array(pc.pc_data['z'], dtype=np.float32)).astype(np.float32)
    np_i = (np.array(pc.pc_data['intensity'], dtype=np.float32)).astype(np.float32) # / 256
    # np_r = (np.array(pc.pc_data['ring'], dtype=np.float32)).astype(np.float32)
    # np_t = (np.array(pc.pc_data['time'], dtype=np.float32)).astype(np.float32)

    ## Stack all data
    points_32 = np.transpose(np.vstack((np_x, np_y, np_z, np_i)))

    ## Save bin file
    points_32.tofile(bin_file_path)