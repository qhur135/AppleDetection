import os

path_dir = "./Locations/for_get_AP_yx/ground-truth/train-gt"
save_dir = "./Locations/for_get_AP_yx/yolo-label/train-gt/gt-normalize"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name =save_dir+'/'+file_list[i]
    save = open(save_name,"w")
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        list = line.split(',')
        name = list[0]
        # for i in range(4):
        #     list[i+1]=str(round(float(list[i+1])))
        #print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        xcenter = (int(list[2])+int(list[4]))/2
        ycenter = (int(list[1])+int(list[3]))/2
        width = int(list[4])-int(list[2])
        height = int(list[3])-int(list[1])
        xcenter = round(xcenter/720,6)
        ycenter = round(ycenter/1280,6)
        width = round(width/720,6)
        height = round(height/1280,6)
        save.write(f'47 {str(xcenter)} {str(ycenter)} {str(width)} {str(height)}\n') # xcenter, ycenter, width, height
