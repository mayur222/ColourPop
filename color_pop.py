import sys
import os
import imghdr
from fastprogress import progress_bar
import cv2

def create_image_pop(f_tmp):
	img = cv2.imread(f_tmp)
	new_col = cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2RGB)
	reverse = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	r_col = new_col.copy()
	g_col = new_col.copy()
	b_col = new_col.copy()
	rg_col = new_col.copy()
	gb_col = new_col.copy()
	rb_col = new_col.copy()
	master_bar1 = progress_bar(range(img.shape[0]))
	for i in master_bar1:
		for j in range(img.shape[1]):
			if img[i][j][2] > img[i][j][1] and img[i][j][2] > img[i][j][0]:
				r_col[i][j] = img[i][j]
			if img[i][j][1] > img[i][j][2] and img[i][j][1] > img[i][j][0]:
				g_col[i][j] = img[i][j]
			if img[i][j][0] > img[i][j][1] and img[i][j][0] > img[i][j][2]:
				b_col[i][j] = img[i][j]
			if img[i][j][2] > img[i][j][0] or img[i][j][1] > img[i][j][0]:
				rg_col[i][j] = img[i][j]
			if img[i][j][0] > img[i][j][2] or img[i][j][1] > img[i][j][2]:
				gb_col[i][j] = img[i][j]
			if img[i][j][2] > img[i][j][1] or img[i][j][0] > img[i][j][1]:
				rb_col[i][j] = img[i][j]
	dir_t = '.'.join(f_tmp.split('.')[:-1])
	if not os.path.isdir(dir_t):
		os.mkdir(dir_t)
	print('Saving color pop of', f_tmp, 'in', dir_t)
	img_name = dir_t.split('/')[-1]
	cv2.imwrite(dir_t + '/red' + img_name + '.jpg', r_col)
	cv2.imwrite(dir_t + '/green' + img_name + '.jpg', g_col)
	cv2.imwrite(dir_t + '/blue' + img_name + '.jpg', b_col)
	cv2.imwrite(dir_t + '/redGreen' + img_name + '.jpg', rg_col)
	cv2.imwrite(dir_t + '/greenBlue' + img_name + '.jpg', gb_col)
	cv2.imwrite(dir_t + '/redBlue' + img_name + '.jpg', rb_col)
	cv2.imwrite(dir_t + '/reverse' + img_name + '.jpg', reverse)
	print('Saved')

files = []
if len(sys.argv) > 1:
	files = sys.argv[1:]
else:
	file_tmp = input('Enter file name(with correct path): ')
	files.append(file_tmp)

for f in files:
	if os.path.exists(f):
		if imghdr.what(f):
			create_image_pop(f)
		else:
			print(f, 'is not image file')
	else:
		print(f, 'doesn\'t exists')
