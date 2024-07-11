import pygame

# 1. 게임 초기화
pygame.init()

puzzleimage = pygame.image.load('사과.jpg')
puzzlesize = puzzleimage.get_size()
puzzlesize  = (round(puzzlesize[0]*0.5),round(puzzlesize[1]*0.5))
puzzleimage = pygame.transform.smoothscale(puzzleimage,puzzlesize)

inum,jnum = 4,4
puzzlelist = []
#puzzlelist create
for i in range(inum):
  templist=[]
  for j in range(jnum):
    templist.append(j*jnum +i+1)
  puzzlelist.append(templist)
puzzlelist[-1][-1] = 0

#puzzleimagelist create
puzzleimagelist = []
for i in range(inum):
  templist=[]
  for j in range(jnum):
    w,h = puzzlesize[0]/inum,puzzlesize[1]/jnum
    x,y = i*w, j*h
    partimage = puzzleimage.subsurface((x,y,w,h))

    templist.append(partimage)
  puzzleimagelist.append(templist)
bs =pygame.Surface((w,h))
bs.fill((0,0,0))
puzzleimagelist[-1][-1] = bs

# 2 게임창 옵션 설정
size = puzzlesize
screen = pygame.display.set_mode(size)
title = 'puzzle'
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock =pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
exit = False
#4. 메인 이벤트
while not exit:
  # 4-1. Fps 설정
  clock.tick(60)
  # 4-2. 각종 입력 감지
  for event in pygame.event.get(): #리스트로 받음
    if event.type == pygame.QUIT:
        exit =True
  # 4-3 입력 시간에 따른 변화
  # 4-4 그리기
  screen.fill(white)
  # 퍼즐 그리기
#   for i in range(inum):
#     for j in range(jnum):
#       img = puzzlelist[i][j]['image']
#       pos = puzzlelist[i][j]['pos']
#       screen.blit(img,pos)
    
  # 4-5 업데이트
  pygame.display.flip()
# 5. 게임 종료
pygame.quit()