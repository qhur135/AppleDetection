import os

path_dir = "./Locations/for_get_AP_yx/ground-truth/test-gt"
save_dir = "./Locations/for_get_AP_yx/yolo-label/test-gt/gt-normalize"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name =save_dir+'/'+file_list[i]
    save = open(save_name, "w")
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        List = line.split(' ')
        name = List[0]
        for i in range(1, len(List)):
            List[i] = int(List[i])

        # ymin xmin ymax xmax
        # for _ in range(4):
        #     list[i+1] = str(round(float(list[i+1])))

        # print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        xcenter = (List[4] + List[2]) / 2
        ycenter = (List[3] + List[1]) / 2
        width = (List[4]) - (List[2])
        height = (List[3]) - (List[1])
        xcenter = round(xcenter/1280, 6)
        ycenter = round(ycenter/720, 6)
        width = round(width/1280, 6)
        height = round(height/720, 6)
        # print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        save.write(f'47 {str(ycenter)} {str(xcenter)} {str(height)} {str(width)}\n') # xcenter, ycenter, width, height