import os 
import shutil 
import glob 


src_path = r"custom_person\ren_trans_label"
dest_path = r"custom_person\ren_trans_label_mname"

txt_files = glob.glob(os.path.join(src_path, '*.txt'))
# print(txt_files) ['trans_label\\000950.txt', 'trans_label\\000965.txt', 'trans_label\\000970.txt', 'trans_label\\000975.txt']

os.makedirs(dest_path, exist_ok=True) # 确保dest_path存在, 如果不存在就自动创建

for txt_file in txt_files:
    out_file = os.path.join(dest_path, os.path.basename(txt_file))
    # print(type(out_file)) # trans_cname\000950.txt trans_cname\000965.txt trans_cname\000970.txt trans_cname\000975.txt
    
    shutil.copy2(txt_file, out_file)
    
    with open(out_file, 'r') as file:
        lines = file.readlines()
        
    with open(out_file, 'w') as modifies_file:
        for line in lines:
            data = line.split()
            
            # 根据自己的需求而定
            if data[-1] == 'Pedestrian':
                data[-1] = 'Person'
            elif data[-1] == 'Bus':
                data[-1] = 'DJ'
            elif data[-1] == 'Car':
                data[-1] = 'FZD'
            
            modifies_file.write(' '.join(data) + '\n')
 




