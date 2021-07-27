import os

path_dir = "./Locations/for_get_AP_yx/ground-truth"
save_dir = "./Locations/for_get_AP_yx/ground-truth2"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name =save_dir+'/'+file_list[i]
    save = open(save_name,"w")
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        list = line.split(' ')
        name = list[0]
        # for i in range(4):
        #     list[i+1]=str(round(float(list[i+1])))
        #print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        save.write(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')