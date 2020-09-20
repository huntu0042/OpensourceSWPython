from bangtal import *
import time
import random

solution = random.randint(0,2)
IMG_DIR = "./images/"

scene1 = Scene("룸1",IMG_DIR+"/배경-1.png")
scene2 = Scene("룸2",IMG_DIR+"/배경-2.png")
scene_exit = Scene("EXIT",IMG_DIR+"/exit.jpg")
scene_blood = Scene("EXIT",IMG_DIR+"/blood_ending.png")

door1_0 = Object(IMG_DIR+"/문-오른쪽-닫힘.png")
door1_0_closed = True
door1_0.locate(scene1,600,300)
door1_0.show()


door1_1 = Object(IMG_DIR+"/문-오른쪽-닫힘.png")
door1_1_closed = True
door1_1.locate(scene1,800,270)
door1_1.show()


door1_2 = Object(IMG_DIR+"/문-오른쪽-닫힘.png")
door1_2_closed = True
door1_2.locate(scene1,1000,220)
door1_2.show()


key = Object(IMG_DIR+"/열쇠.png")
key.setScale(0.2)
key.locate(scene1,600,150)
key.show()

flowerpot = Object(IMG_DIR+"화분.png")
flowerpot.moved = False
flowerpot.locate(scene1,550,150)
flowerpot.show()

door2 = Object(IMG_DIR+"문-왼쪽-열림.png")
door2.locate(scene2,320,270)
door2.show()

door3 = Object(IMG_DIR+"/문-오른쪽-닫힘.png")
door3.locate(scene2,800,270)
door3.show()

door4 = Object(IMG_DIR+"/문-오른쪽-닫힘.png")
door4.setScale(0.5)
door4.locate(scene2,1000,270)
door4.show()
door4.closed = True

flowerpot2 = Object(IMG_DIR+"화분.png")
flowerpot2.moved = False
flowerpot2.setScale(1.5)
flowerpot2.locate(scene2,930,220)
flowerpot2.show()



flowerpot3 = Object(IMG_DIR+"화분.png")
flowerpot3.moved = False
flowerpot3.setScale(1.5)
flowerpot3.locate(scene2,630,300)
flowerpot3.show()


saw_doll = Object(IMG_DIR+"saw.png")
saw_doll.moved = False
saw_doll.setScale(0.1)
saw_doll.locate(scene1,100,100)
saw_doll.show()


def click_door1_0(x,y,action):
    global door1_0_closed, door1_1_closed, door1_2_closed
    if door1_0_closed == True:
        if key.inHand():
            door1_0.setImage(IMG_DIR+"/문-오른쪽-열림.png")
            door1_0_closed = False
        else:
            showMessage("문이 단단히 잠겨있다!")
    else:

        if door1_0_closed == False and door1_1_closed == False and door1_2_closed == False:
            scene2.enter()
            showMessage("세가지 문을 다 열어보고 오다니.. 똑똑하군")

        elif solution == 0:
            scene2.enter()
        else:
            scene_blood.enter()
            showMessage("너는 여기에 올 운이 없군. 잘가라.\n [[GAME OVER]]")


def click_door1_1(x,y,action):
    global door1_0_closed, door1_1_closed, door1_2_closed
    if door1_1_closed == True:
        if key.inHand():
            door1_1.setImage(IMG_DIR+"/문-오른쪽-열림.png")
            door1_1_closed = False
        else:
            showMessage("문이 단단히 잠겨있다!")
    else:
        if door1_0_closed == False and door1_1_closed == False and door1_2_closed == False:
            scene2.enter()
            showMessage("세가지 문을 다 확인하고 오다니.. 똑똑하군")
        elif solution == 0:
            scene2.enter()
        else:
            scene_blood.enter()
            showMessage("너는 여기에 올 운이 없군. 잘가라. \n [[GAME OVER]]")



def click_door1_2(x,y,action):
    global door1_0_closed, door1_1_closed, door1_2_closed
    if door1_2_closed == True:
        if key.inHand():
            door1_2.setImage(IMG_DIR+"/문-오른쪽-열림.png")
            door1_2_closed = False
        else:
            showMessage("문이 단단히 잠겨있다!")
    else:
        if door1_0_closed == False and door1_1_closed == False and door1_2_closed == False:
            scene2.enter()
            showMessage("세가지 문을 다 열어보고 오다니.. 똑똑하군")
        elif solution == 0:
            scene2.enter()
        else:
            scene_blood.enter()
            showMessage("너는 여기에 올 운이 없군. 잘가라.\n [[GAME OVER]]")


def door2_onMouseAction(x,y,action):
    scene1.enter()

def door3_onMouseAction(x,y,action):
    showMessage("문이 단단히 잠겨있다!")

def door4_onMouseAction(x,y,action):
    if door4.closed == True:
        door4.setImage(IMG_DIR + "/문-오른쪽-열림.png")
        door4.closed = False
    elif flowerpot2.moved == True:
        scene_exit.enter()
        showMessage("중앙대학교에 올 운과 실력을 갖췄군. 환영해! \n Game Clear")


def key_onMouseAction(x,y,action):
    key.pick()

def flowerpot_onMouseAction(x,y,action):
    if flowerpot.moved == True:
        return 0
    if action == MouseAction.DRAG_LEFT:
        flowerpot.locate(scene1,450,150)
        flowerpot.moved = True
    elif action == MouseAction.DRAG_RIGHT:
        flowerpot.locate(scene1,650,150)
        flowerpot.moved = True

def flowerpot2_onMouseAction(x,y,action):
    if flowerpot2.moved == True:
        return 0
    elif action == MouseAction.DRAG_LEFT:
        flowerpot2.locate(scene2,730,220)
        flowerpot2.moved = True
    elif action == MouseAction.DRAG_RIGHT:
        flowerpot2.locate(scene2,1130,220)
        flowerpot2.moved = True


def flowerpot3_onMouseAction(x,y,action):
    showMessage("바닥에 본드로 붙은 듯 하다.. 안간힘을 써도 움직이지 않는다")


def saw_onMouseAction(x,y,action):
    showMessage("[인형을 누르자 말을 한다] \n 자 게임을 시작하지. 너의 운을 시험해볼까. 3개중 진짜 문은 무작위 하나. 기회도 하나다. (중얼중얼) 똑똑하다면 운은 필요없을지도..")


door1_0.onMouseAction = click_door1_0
door1_1.onMouseAction = click_door1_1
door1_2.onMouseAction = click_door1_2
door3.onMouseAction = door3_onMouseAction
door4.onMouseAction = door4_onMouseAction
key.onMouseAction = key_onMouseAction
flowerpot.onMouseAction = flowerpot_onMouseAction
flowerpot2.onMouseAction = flowerpot2_onMouseAction
flowerpot3.onMouseAction = flowerpot3_onMouseAction

saw_doll.onMouseAction = saw_onMouseAction
startGame(scene1)

