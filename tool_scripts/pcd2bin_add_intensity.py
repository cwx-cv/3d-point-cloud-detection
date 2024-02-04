import os
import numpy as np
from pypcd import pypcd

def convert_pcd_to_bin(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取输入文件夹中的所有.pcd文件
    pcd_files = [f for f in os.listdir(input_folder) if f.endswith('.pcd')]

    for pcd_file in pcd_files:
        pcd_path = os.path.join(input_folder, pcd_file)
        
        # 加载.pcd文件
        pcd_data = pypcd.PointCloud.from_path(pcd_path)

        # 创建NumPy数组, 每个点有4个属性x、y、z以及intensity
        points = np.zeros([pcd_data.width, 4], dtype=np.float32)
        points[:, 0] = pcd_data.pc_data['x'].copy()
        points[:, 1] = pcd_data.pc_data['y'].copy()
        points[:, 2] = pcd_data.pc_data['z'].copy()
        points[:, 3] = 0.0 

        # 构造输出二进制文件的路径
        output_bin_path = os.path.join(output_folder, f"{pcd_file.replace('.pcd', '.bin')}")

        # 将点云数据以二进制形式写入到输出文件
        with open(output_bin_path, 'wb') as f:
            f.write(points.tobytes())

if __name__ == "__main__":
    input_folder = r'custom_person\ren_pcd_final'  # 替换为你实际的输入文件夹路径
    output_folder = r'custom_person\points_bin'  # 替换为你想要存储输出文件的文件夹路径

    convert_pcd_to_bin(input_folder, output_folder)




### bug1 ModuleNotFoundError: No module named 'cStringIO'
#  File "D:\Anaconda3_2021_11\envs\pytorch_gpu\lib\site-packages\pypcd\pypcd.py", line 15, in <module>
#     import cStringIO as sio
#     from _io import StringIO as sio


### bug2 TypeError: startswith first arg must be bytes or a tuple of bytes, not str


