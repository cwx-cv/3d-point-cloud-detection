import os 
import open3d as o3d
import numpy as np 

def pcd2npy(pcd_path, npy_path):
    """
    This script is used to convert pcd format point cloud files to .npy format.
    """
    pcd_list = os.listdir(pcd_path)
    
    for pcd_name in pcd_list:
        pcd_file = os.path.join(pcd_path, pcd_name)
        lidar = []
        pcd = o3d.io.read_point_cloud(pcd_file)
        points = np.array(pcd.points)
        
        for linestr in points:
            if len(linestr) == 3:  # only x, y, z 
                linestr_convert = list(map(float, linestr))
                linestr_convert.append(0)
            elif len(linestr) == 4:  # x, y, z, r/i
                linestr_convert = list(map(float, linestr))
            lidar.append(linestr_convert)
        
        lidar = np.array(lidar).astype(np.float32)
        
        if len(lidar) > 0:
            np.save(os.path.join(npy_path, pcd_name[:-4] + ".npy"), lidar)


if __name__ == '__main__':
    pcd_path = "example_pcd"
    npy_path = "example_npy"
    
    if not os.path.exists(npy_path):
        os.mkdir(npy_path)
    
    pcd2npy(pcd_path, npy_path)
