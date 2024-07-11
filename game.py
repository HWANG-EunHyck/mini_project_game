import pygame

# 1. 게임 초기화
pygame.init()

picture = pygame.image.load('사과.jpg')
picturesize = picture.get_size()
picturesize  = (round(picturesize[0]*0.8),round(picturesize[1]*0.8))
picture = pygame.transform.smoothscale(picture,picturesize)

inum,jnum = 4,4
picturelist = []
for i in range(inum):
  empty_list=[]
  for j in range(jnum):
    w,h = picturesize[0]/inum,picturesize[1]/jnum
    x,y = i*w, j*h
    divpicture = picture.subsurface((x,y,w,h))
    import_dict={
      'listnum':j*jnum+i+1,
      '자른그림':divpicture,
      '위치':(x,y)  
    }
    empty_list.append(import_dict)
  picturelist.append(empty_list)
picturelist[-1][-1]['listnum'] = 0
# print(picturelist[-1][-1])
# print(picturelist[-1][-1]['listnum'])
blackpoint =pygame.Surface((w,h))
blackpoint.fill((0,0,0))
picturelist[-1][-1]['자른그림'] = blackpoint

print(picturelist[0][0]['자른그림'])
# 2 게임창 옵션 설정
size = picturesize
screen = pygame.display.set_mode(size)
title = '퍼즐게임'
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock =pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
diretiondict ={
    "left":(-1,0),'right':(1,0),
    "up":(0,-1),'down':(0,1)
}
exit = True
presskey = False

#4. 메인 이벤트
while exit:
  # 4-1. Fps 설정
  clock.tick(60)
  # 4-2. 각종 입력 감지
  for event in pygame.event.get(): #리스트로 받음
    if event.type == pygame.QUIT:
        exit =False
    if event.type == pygame.KEYDOWN:
        keyname = pygame.key.name(event.key)
        # print(keyname)
        for key in diretiondict.keys():
           if key == keyname:
              presskey = True
           
           


  # 4-3 입력 시간에 따른 변화
  for i in range(inum):
      for j in range(jnum):
         if picturelist[i][j]['listnum'] == 0:
            moo = (i,j)

  if presskey == True:
    i,j = moo
    dir_i,dir_j = diretiondict[keyname]
    movei,movej = i+dir_i, j+dir_j
    if movei>=0 and movei<inum and movej>=0 and movej<jnum:
        picturelist[i][j]['listnum'],picturelist[movei][movej]['listnum'] = picturelist[movei][movej]['listnum'],picturelist[i][j]['listnum']
        picturelist[i][j]['자른그림'],picturelist[movei][movej]['자른그림'] = picturelist[movei][movej]['자른그림'],picturelist[i][j]['자른그림']
  presskey = False


  # 4-4 그리기
  screen.fill(white)
  # 퍼즐 그리기
  for i in range(inum):
    for j in range(jnum):
      image = picturelist[i][j]['자른그림']
      coordinate = picturelist[i][j]['위치']
      screen.blit(image,coordinate)
      x,y =coordinate
      A = (x,y)
      B = (x+w,y)
      C = (x,y+h)
      D = (x+w,y+h)
      pygame.draw.line(screen,black,A,B,3)
      pygame.draw.line(screen,black,A,C,3)
      pygame.draw.line(screen,black,D,B,3)
      pygame.draw.line(screen,black,D,C,3)
    
  # 4-5 업데이트
  pygame.display.flip()
# 5. 게임 종료
pygame.quit()
# 열정과 예산