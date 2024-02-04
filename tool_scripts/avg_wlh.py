# 获取每个类别的3d包围框的平均长、宽以及高, 以此来设置自定义数据集的anchor

import os

if __name__ == "__main__":
    label_path = "data/custom/labels" # 数据集标签的路径
    label_list = os.listdir(label_path)
    # l w h  替换为自己数据集的类别
    P_counts = 0
    Pedestrian = [0.0, 0.0, 0.0]
    B_counts = 0
    BicycleRider = [0.0, 0.0, 0.0]
    C_counts = 0
    Car = [0.0, 0.0, 0.0]

    for label_name in label_list:
        label_file = os.path.join(label_path, label_name)
        with open(label_file, 'r') as f:
            data = f.readlines()
            for line in data:
                temp_list = line.split(" ")
                cls_name = temp_list[-1][:-1]
                if cls_name == "Pedestrian":
                    Pedestrian[0] += float(temp_list[3])
                    Pedestrian[1] += float(temp_list[4])
                    Pedestrian[2] += float(temp_list[5])
                    P_counts += 1
                elif cls_name == "BicycleRider":
                    BicycleRider[0] += float(temp_list[3])
                    BicycleRider[1] += float(temp_list[4])
                    BicycleRider[2] += float(temp_list[5])
                    B_counts += 1
                else:
                    Car[0] += float(temp_list[3])
                    Car[0] += float(temp_list[4])
                    Car[0] += float(temp_list[5])
                    C_counts += 1

    print(f"P l{Pedestrian[0]/P_counts} w{Pedestrian[1]/P_counts} h{Pedestrian[2]/P_counts}")
    print(f"B l{BicycleRider[0]/B_counts} w{BicycleRider[1]/B_counts} h{BicycleRider[2]/B_counts}")
    print(f"C l{Car[0]/C_counts} w{Car[1]/C_counts} h{Car[2]/C_counts}")
    
    
