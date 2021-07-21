import pygame  # pygame 라이브러리
import sys  #
from time import sleep
import random

BLACK = (0, 0, 0)  # RGB 0 0 0
padWidth = 480  # 게임화면의 가로크기
padHeight = 620  # 게임화면의 세로크기
falling_object = ['','','','','','','','','',''] # 떨어지는 물체 이미지들
power = ['','','','','','','','','',''] # 전기 이미지

def drawObject(obj, x ,y): # 게임에 등장하는 객체를 드로잉
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():  # 게임초기화
    global gamePad, clock ,background, earth, tear, explosion # 글로벌 변수
    pygame.init()  # 파이게임 초기화
    gamePad = pygame.display.set_mode((padWidth, padHeight))  # 게임크기 정의
    pygame.display.set_caption("지구를 지켜라")  # 게임 이름 창의 제목으로 띄워주는 부분
    background = pygame.image.load("e:\\stgame\녹는빙하3.png")
    # 배경그림 위에 게임화면 설정과 픽셀이 같아야 올바른 이미지 출력
    earth = pygame.image.load("e:\\stgame\아픈지구700.png")
    tear = pygame.image.load(("e:\\stgame\눈물1.png"))
    explosion = pygame.image.load(("e:\\stgame\눈물1.png")) # 폭발 그림 그리고 밑에 반짝 그림
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background, earth, tear, explosion # 지구

    #전투기 크기 현제 픽셀은 50*50 픽셀과 관련되있나 확인
    earthSize = earth.get_rect().size  # get_rect() 함수 게임 객체 크기정보 + 좌표정보
    earthWidth = earthSize[0]
    earthHeight = earthSize[1]

    # 전투기 초기 위치(x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    earthX = 0

    tearXY=[] # 무기 좌표 리스트

    #떨어지는 물체 와 전력 랝덤 생성
    obj = pygame.image.load(random.choice(falling_object))
    objSize = obj.get_rect().size  # 물체 크기
    objWidth = objSize[0]
    objHeight = objSize[1]

    # 물체 및 파워 초기 위치 설정
    objX = random.randrange(0, padWidth - objWidth)
    objY = 0
    objSpeed = 2 #속도를 의미 하는 듯? 이것도 랜덤 가능한지 확인

    # 전투기 미사일에 운석이 맞았을 경우 True
    isShot = False
    shotCount = 0
    objPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임종료하는 함수
                pygame.quit()  # 창을 닫거나 하면 파이게임을 종료 or 시스템 종료시키는 이벤트 처리
                sys.exit()
            # 이후 상하좌우로 바꿔야지~
            if event.type in [pygame.KEYDOWN]: # 키보드를 누른 후 뗼떄 발생함.
                if event.key == pygame.K_LEFT: # 지구 왼쪽으로 이동
                    earthX -= 5 # 속도
                elif event.key == pygame.K_RIGHT:# 지구 오른쪽으로 이동
                    earthX += 5
                elif event.key == pygame.K_SPACE: # 미사일 발사~~
                    tearX = x + earthWidth/2
                    tearY = y - earthHeight
                    tearXY.append([tearX, tearY])

            if event.type in [pygame.KEYUP]: #방향키를 뗴면 전투기 멈춤 (KEYUP은 키보드 누를 떄 발생함.)
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    earthX = 0

        # 전투기 위치 재조정
        x += earthX
        if x < 0:
            x = 0
        elif x > padWidth - earthWidth:
            x = padWidth - earthWidth

        drawObject(background, 0, 0)  #녹는 빙하 배경화면 그리기
        drawObject(earth, x, y)

        # 미사일 발사 화면에 그리기   drawObject(earth, x, y) 밑에 !
        if len(tearXY) != 0:
            for i, bxy in enumerate(tearXY):  # 미사일 요소에 대해 반복함  enumerate() 확인 할 것
                bxy[1] -= 10  # 총알의 y 좌표 - 10 (위로 이동?)
                tearXY[i][1] = bxy[1]

                # 미사일이 운석을 맞추었을 경우
                if bxy[1] < objY:
                    if bxy[0] > objX and bxy[0] < objX + objWidth: tearXY.remove(bxy)
                    isShot = True
                    shotCount += 1  #

                if bxy[1] <= 0:  # 미사일이 화면 밖으로 벗어나면
                    try:
                        tearXY.remove(bxy) #미사일 제거
                    except:
                        pass
        # 물체 맞췄을 떄
        if isShot: # 운석 폭발
            drawObject(explosion,objX,objY) # 물체 폭발 이미지

            #새로운 물체 랜덤
            obj = pygame.image.load(random.choice(falling_object))
            objSize = obj.get_rect().size  # 물체 크기
            objWidth = objSize[0]
            objHeight = objSize[1]
            objX = random.randrange(0, padWidth - objWidth)
            objY = 0
            isShot = False

            # 운석 맞추면 속도 증가?
            objSpeed += 0.02
            if objSpeed >= 10:
                objSpeed = 10
        drawObject(falling_object, objX, objY) #물체 그리기 아래 물체그리기랑 중복 확인


        if len(tearXY) != 0: # 미사일 발사 관련
            for bx, by in tearXY:
                drawObject(tear, bx, by)
        writeScore(shotCount) # 뮬체 맞춘 점수 표시
        objY =+ objSpeed # 물체 알래로 움직임

        #물체가 바닥으로 떨어진 경우?
        if objY > padHeight:
            # 새로운 물체 (랜덤)
            obj = pygame.image.load(random.choice(falling_object))
            objSize = obj.get_rect().size  # 물체 크기
            objWidth = objSize[0]
            objHeight = objSize[1]
            objX = random.randrange(0,padWidth-objWidth)
            objY = 0
            objSpeed += 1 # 이거 왜 했는지?
        # drawObject(falling_object, objX, objY) # 물체 그리기 얘 왜 갑자기 코딩이 없어지지?
        if objPassed == 3: # 운석 3개 놓치면 게임 오버
            gameOver()

        writePassed(objPassed)



        # gamePad.fill(BLACK)  # 게임 화면 (검정색색
        pygame.display.update()  # 게임화면을 다시그림
        clock.tick(60)  # 게임화면의 초당 프레임수를 50으로 설정
    pygame.quit()  # pygame 종료

#게임 메시지 출력
def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf',80)
    text = textfont.render(text,True, (255,0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    runGame()

# 지구가 물체과 충돌했을 때 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴 ')

# 게임오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임오버 ')

# 물체를 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20)  # 글자 사이즈
    text = font.render('파괴한 운석 수 :' +str(count),True,(255,255,255)) # 색 True? 이거 확인 할 것
    gamePad.blit(text,(10,0)) # 위치조정
# 물체가 화면 아래로 통과한 개수
def writePassed(count): # 이건 값을 -해주자
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)  # 글자 사이즈
    text = font.render('놓친 운석 :' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (360, 0))

initGame()
runGame()

# import os
# import sys
# import math
# import pygame
# import pygame.mixer
# from pygame.locals import *
#
# black = 0,0,0
# white = 255,255,255
# red = 255,0,0
# green = 0,255,0
# blue = 0,0,255
#
# screen = screen_width, screen_height = 600, 400
#
# clock = pygame.time.Clock()
#
# pygame.display.set_caption("Physics")
#
# fps_cap = 120
# running = True
# while running:
#     clock.tick(fps_cap)
#
#     for event in pygame.event.get(): #error is here
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill(white)
#
#     pygame.display.flip()
#
# pygame.quit()
# sys.exit
# #!/usr/bin/env python