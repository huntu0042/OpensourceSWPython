from bangtal import *
import time
import random
import os

IMG_DIR = "./img/"
front_name = "front1"
background_name = "back1"
start_time = 0.0
end_time = 0.0

scene_game1 = Scene("game1",IMG_DIR+background_name+"_crop.jpg")
tile_list = []
start_button = Object(IMG_DIR + "start.png")
showMessage("박보영 퍼즐 입니다.\n 원하는 사진을 골라주세요!")


def click_one(x,y,action):
    global scene_game1
    global tile_list
    global start_button
    global adj_list

    background_name = "back1"
    scene_game1 = Scene("game1",IMG_DIR+background_name+"_crop.jpg")

    front_name = "front1"

    for y in range(0, 4):
        for x in range(0, 4):
            if y == 3 and x == 3:
                break
            i = y * 4 + x
            tile_list.append(Tile(i,front_name))
            tile_list[i].locate_object(x, y, scene_game1)

    adj_list = get_adj_list(3, 3)


    start_button.locate(scene_game1, 600, 400)
    start_button.onMouseAction = click_start
    start_button.show()

    scene_game1.enter()

def click_two(x,y,action):
    global scene_game1
    global tile_list
    global start_button
    global adj_list

    background_name = "back2"
    scene_game1 = Scene("game1", IMG_DIR + background_name + "_crop.jpg")

    front_name = "front2"

    for y in range(0, 4):
        for x in range(0, 4):
            if y == 3 and x == 3:
                break
            i = y * 4 + x
            tile_list.append(Tile(i,front_name))
            tile_list[i].locate_object(x, y, scene_game1)

    adj_list = get_adj_list(3, 3)

    start_button.locate(scene_game1, 600, 400)
    start_button.onMouseAction = click_start
    start_button.show()


    scene_game1.enter()

def click_three(x,y,action):
    global scene_game1
    global tile_list
    global start_button
    global adj_list

    background_name = "back3"
    scene_game1 = Scene("game1", IMG_DIR + background_name + "_crop.jpg")

    front_name = "front3"


    for y in range(0, 4):
        for x in range(0, 4):
            if y == 3 and x == 3:
                break
            i = y * 4 + x
            tile_list.append(Tile(i,front_name))
            tile_list[i].locate_object(x, y, scene_game1)

    adj_list = get_adj_list(3, 3)

    start_button.locate(scene_game1, 600, 400)
    start_button.onMouseAction = click_start
    start_button.show()

    scene_game1.enter()

scene_first = Scene("first",IMG_DIR+"bg.png")
photo_one = Object(IMG_DIR+"/back1.jpg")
photo_one.setScale(0.4)
photo_one.locate(scene_first,150,150)
photo_one.onMouseAction = click_one
photo_one.show()

photo_two = Object(IMG_DIR+"/back2.jpg")
photo_two.setScale(0.4)
photo_two.locate(scene_first,550,150)
photo_two.onMouseAction = click_two
photo_two.show()

photo_three = Object(IMG_DIR+"/back3.jpg")
photo_three.setScale(0.4)
photo_three.locate(scene_first,950,150)
photo_three.onMouseAction = click_three
photo_three.show()



adj_list = [[0 for i in range(4)] for j in range(4)]
scene_game1 = Scene("game1",IMG_DIR+background_name+"_crop.jpg")
# dir_name = IMG_DIR + front_name + "/" + front_name + "_" + str(1).zfill(3) + ".jpg"
# # object = Object(dir_name)
# # object.locate(scene_game1,0,0)

def check_status():
    global tile_list
    global start_time
    count = 0
    for tile in tile_list:
        ori_loc = tile.original_loc
        now_loc = tile.now_y*4 + tile.now_x
        if ori_loc == now_loc:
            count += 1
    if count == 15:
        clear_time = time.time() - start_time
        showMessage("!!!!!!!GAME CLEAR!!!!!!!\n clear time : " + str(round(clear_time,2)))

        if not os.path.isfile(IMG_DIR+background_name+".txt"):
            f = open(IMG_DIR+background_name+".txt","w")
            f.write(str(clear_time))
            showMessage("** NEW HIGH SCORE : " + str(round(clear_time, 2)) + "**")
        else:
            f = open(IMG_DIR + background_name + ".txt", "r")
            text = f.readline()
            f.close()
            t = float(text)
            print(t)
            print(clear_time)
            if t > clear_time:
                showMessage("** NEW HIGH SCORE : " + str(round(clear_time, 2)) + "**\n before :" +str(t))
                f = open(IMG_DIR + background_name + ".txt", "w")
                f.write(str(clear_time))
            else:
                showMessage("EXIST HIGH SCORE : " + str(t) +"\n")


    clear_time = time.time() - start_time
    print(round(clear_time, 2))
    print(count)


class Tile:
    def __init__(self,count,front_name):
        self.original_loc = count
        dir_name = IMG_DIR + front_name + "/" + front_name + "_" + str(count+1).zfill(3) + ".jpg"
        self.object = Object(dir_name)
        self.now_x = -1
        self.now_y = -1

        def click_tile(x, y, action):
            global adj_list
            check = check_adj_list(self.now_x, self.now_y, adj_list)
            x = self.now_x
            y = self.now_y
            if check == 1:
                self.now_y -= 1
            elif check == 2:
                self.now_y += 1
            elif check == 3:
                self.now_x -= 1
            elif check == 4:
                self.now_x += 1
            else:
                showMessage("움직일 수 없어")
                return 0
            self.locate_object(self.now_x, self.now_y, scene_game1)
            adj_list = get_adj_list(x, y)
            check_status()
            return 1

        self.object.onMouseAction = click_tile



    def locate_object(self,x,y,scene):
        self.now_x = x
        self.now_y = y
        loc_x = 439 + x * 100
        loc_y = 535 - y * 125
        self.object.locate(scene, loc_x, loc_y)
        self.object.show()




def check_adj_list(x,y,adjlist):
    check = 0
    if x-1 >= 0:
        if adjlist[x-1][y] == -1:
            check = 3
    if y-1 >= 0:
        if adjlist[x][y-1] == -1:
            check = 1
    if y+1 < 4:
        if adjlist[x][y+1] == -1:
            check = 2
    if x+1 < 4:
        if adjlist[x+1][y] == -1:
            check = 4
    return check  ### 상하좌우 1234


def get_adj_list(x,y):
    arr = [[0 for i in range(4)] for j in range(4)]
    arr[x][y] = -1
    if x-1 >= 0:
        arr[x-1][y] = 1
    if y-1 >= 0:
        arr[x][y-1] = 1
    if y+1 < 4:
        arr[x][y+1] = 1
    if x+1 < 4:
        arr[x+1][y] = 1

    return arr

def print_adj_list(adj_list):
    for i in range(len(adj_list)):
        for j in range(len(adj_list[0])):
            print(str(adj_list[i][j])+" ",end='')
        print('\n')


def click_start(x,y,action):
    global tile_list
    global start_button
    global start_time

    x = [0,1,2,3]
    y = [0,1,2,3]
    random.shuffle(x)
    random.shuffle(y)

    arr = []
    for i in x:
        for j in y:
            if i == 3 and j == 3:
                continue
            arr.append([i,j])
    print(arr)


    for i in range(0, 15):
        tile_list[i].locate_object(arr[i][0],arr[i][1],scene_game1)
    start_button.hide()
    start_time = time.time()






#map_status = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1]



startGame(scene_first)

