import os

path_dir = "./Locations/yolo_s"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name ="./Locations/for_get_AP_xy/yolov5s-results/"+file_list[i]
    save=open(save_name,"a")
    lines = f.readlines()

    for line in lines:
        list = line.split(' ')
        name = list[0]
        for i in range(4):
            list[i+2]=str(round(float(list[i+2])))

        save.write(f'{name} {list[1]} {list[3]} {list[2]} {list[5]} {list[4]}\n')