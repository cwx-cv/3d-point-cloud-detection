import os
import random

def split_train_val(src_path, dst_path, split_ratio=0.8):
    """
    src_path: Label file directory
    dst_path: Output file directory
    split_ratio: Ratio for splitting the data into training and validation sets
    """
    src_list = os.listdir(src_path)
    random.shuffle(src_list)

    split_index = int(len(src_list) * split_ratio)
    train_list = src_list[:split_index]
    val_list = src_list[split_index:]

    with open(os.path.join(dst_path, "train.txt"), 'w') as f:
        for file_name in train_list:
            f.write(file_name.split(".")[0])  # Writing file names without extensions
            f.write('\n')

    with open(os.path.join(dst_path, "val.txt"), 'w') as f:
        for file_name in val_list:
            f.write(file_name.split(".")[0])  # Writing file names without extensions
            f.write('\n')


if __name__ == '__main__':
    src_path = r"custom_person\labels"
    dst_path = r"custom_person\ImageSets"
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    split_ratio = 0.8  # 80% for training, 20% for validation---可以根据自己的需求自定义
    split_train_val(src_path, dst_path, split_ratio)
