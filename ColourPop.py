import cv2
from fastprogress import master_bar, progress_bar
import sys
import os
import imghdr

def createImagePop(f_tmp):
	img = cv2.imread(f_tmp)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	newCol = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
	reverse = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	rCol = newCol.copy()
	gCol = newCol.copy()
	bCol = newCol.copy()
	rgCol = newCol.copy()
	gbCol = newCol.copy()
	rbCol = newCol.copy()
	mb = progress_bar(range(img.shape[0]))
	for i in mb:
		for j in range(img.shape[1]):
		    if img[i][j][2]>img[i][j][1] and img[i][j][2]>img[i][j][0]:
		        rCol[i][j]=img[i][j]
		    if img[i][j][1]>img[i][j][2] and img[i][j][1]>img[i][j][0]:
		        gCol[i][j]=img[i][j]
		    if img[i][j][0]>img[i][j][1] and img[i][j][0]>img[i][j][2]:
		        bCol[i][j]=img[i][j]
		    if img[i][j][2]>img[i][j][0] or img[i][j][1]>img[i][j][0]:
		        rgCol[i][j]=img[i][j]
		    if img[i][j][0]>img[i][j][2] or img[i][j][1]>img[i][j][2]:
		        gbCol[i][j]=img[i][j]
		    if img[i][j][2]>img[i][j][1] or img[i][j][0]>img[i][j][1]:
		        rbCol[i][j]=img[i][j]
	dir_t='.'.join(f_tmp.split('.')[:-1])
	if not os.path.isdir(dir_t):
		os.mkdir(dir_t)
	print('Saving color pop of',f_tmp,'in',dir_t)
	cv2.imwrite(dir_t+'/red.jpg',rCol)
	cv2.imwrite(dir_t+'/green.jpg',gCol)
	cv2.imwrite(dir_t+'/blue.jpg',bCol)
	cv2.imwrite(dir_t+'/redGreen.jpg',rgCol)
	cv2.imwrite(dir_t+'/greenBlue.jpg',gbCol)
	cv2.imwrite(dir_t+'/redBlue.jpg',rbCol)
	cv2.imwrite(dir_t+'/reverse.jpg',reverse)
	print('Saved')

n = len(sys.argv)
files=[]
if n > 1:
	files = sys.argv[1:]
else:
	file_tmp = input('Enter file name(with correct path): ')
	files.append(file_tmp)
	
for f in files:
	if os.path.exists(f):
		if imghdr.what(f):
			createImagePop(f)
		else:
			print(f,'is not image file')
	else:
		print(f, 'doesn\'t exists')


