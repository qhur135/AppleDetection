import os

path_dir = "./input/ground-truth"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name ="./xy_gt/"+file_list[i]
    save=open(save_name,"a")
    lines = f.readlines()

    for line in lines:
        list = line.split(' ')
        name = list[0]
        for i in range(4):
            list[i+1]=str(round(float(list[i+1])))

        save.write(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')