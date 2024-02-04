import os

def add_zeros_to_filename_dynamic(folder_path, extension):
    files = [f for f in os.listdir(folder_path) if f.endswith(extension)]

    for file_name in files:
        # 获取指定文件夹下每个文件的文件名以及对应的扩展名
        name, ext = os.path.splitext(file_name)

        # 动态计算需要添加的零的个数---这里保证了小数点前面是6位 如果不足的就补上0 当然你可以自定义
        zeros_to_add = max(0, 6 - len(name))
        new_file_name = '0' * zeros_to_add + file_name

        # 构建原始文件路径和新文件路径
        original_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # 重命名文件
        os.rename(original_path, new_path)
        print(f'Renamed: {file_name} -> {new_file_name}')


if __name__ == "__main__":
    folder_path = 'example_sus'  # 替换为实际文件夹的路径---如果是重要文件, 确保文件已备份 因为是在原文件的基础上修改的
    add_zeros_to_filename_dynamic(folder_path, '.json')
    add_zeros_to_filename_dynamic(folder_path, '.pcd')
    add_zeros_to_filename_dynamic(folder_path, '.txt')
    add_zeros_to_filename_dynamic(folder_path, '.npy')

