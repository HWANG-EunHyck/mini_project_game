inum,jnum = 4,4

picturelist = []

#[[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
for i in range(inum):
  numlist=[]
  for j in range(jnum):
    #i = 0 ,j = 0 ,result =1
    #i = 0 ,j = 1 ,result = 5
    #i = 1 ,j = 1 ,result = 6
    numlist.append(j*jnum +i+1)
  picturelist.append(numlist)
picturelist[-1][-1] = 0

# print(puzzlelist)
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

def listshow():
  emt_str = ''
  for j in range(jnum):
    for i in range(inum):
      emt_str += str(picturelist[i][j]) + '\t'
    emt_str += '\n'
  print(emt_str)

# 까만 부분 찾기
for i in range(inum):
  for j in range(jnum):
      if picturelist[i][j] == 0:
        moo = (i,j)
# print(moo)

diretiondict ={
    "left":(-1,0),'right':(1,0),
    "up":(0,-1),'down':(0,1)
}
i,j = moo
dir_i,dir_j = diretiondict['right']
movei,movej = i+dir_i, j+dir_j
#0<=movei<3 / 0<=movej<3
if movei>=0 and movei<inum and movej>=0 and movej<jnum:
  picturelist[i][j],picturelist[movei][movej] = picturelist[movei][movej],picturelist[i][j]
listshow()

dir_i,dir_j = diretiondict['up']
movei,movej = i+dir_i, j+dir_j
picturelist[i][j],picturelist[movei][movej] = picturelist[movei][movej],picturelist[i][j]
listshow()