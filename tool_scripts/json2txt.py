import json
import os


def json_to_txt(json_path, txt_path):
    """
    将sustechpoints标注工具标注的.json文件转化成符合OpenPCDet训练的标签文件
    	json_path: .json文件所在目录
    	txt_path: 生成.txt文件目录
    """
    json_list = os.listdir(json_path)
    # print(json_list)

    for json_name in json_list:
        json_file = os.path.join(json_path, json_name)

        with open(json_file, 'r') as f:
            data = json.load(f)
            # print(data)

        label_list = []

        for obj_dict in data:
            label_name = obj_dict["obj_type"]
            pos_xyz = obj_dict["psr"]["position"]
            rot_xyz = obj_dict["psr"]["rotation"]
            scale_xyz = obj_dict["psr"]["scale"]

            temp = ""
            for xyz_dict in [pos_xyz, scale_xyz]:
                for key in ["x", "y", "z"]:
                    
                    # temp += str(xyz_dict[key])
                    # temp += " "
                    temp += "{:.2f} ".format(xyz_dict[key])  # 控制小数点位数---如果有需要的话---用来替换上面两行
                    
            # temp += str(rot_xyz["z"]) + " " + str(label_name) + "\n"
            temp += "{:.2f} {} \n".format(rot_xyz["z"], label_name)  # 控制小数点位数---如果有需要的话---用来替换上面一行
            label_list.append(temp)

        txt_name = json_name.split(".")[0] + ".txt"
        

        with open(os.path.join(txt_path, txt_name), "w") as f:
            for label in label_list:
                f.write(label)


if __name__ == '__main__':
    json_path = r"custom_person\ren_label_final"
    txt_path = r"custom_person\ren_trans_label"
    if not os.path.exists(txt_path):
        os.mkdir(txt_path)
    json_to_txt(json_path, txt_path)
