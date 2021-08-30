import os

path_dir = "./datasets/real/test/images"
save_dir = "./real-results"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r",encoding='utf-16')

    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        list = line.split(',')
        name = list[0]
        save_name = save_dir + '/' + name+".txt"
        save = open(save_name, "w")
        # for i in range(4):
        #     list[i+1]=str(round(float(list[i+1])))
        #print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        save.write(f'{name} {list[1]} {list[2]} {list[3]} {list[4]} {list[5]}\n')