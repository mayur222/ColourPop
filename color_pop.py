import sys
import os
import imghdr
import cv2

def create_image_pop(f_tmp):
	img = cv2.imread(f_tmp)
	new_col = cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2RGB)
	r_col = new_col.copy()
	g_col = new_col.copy()
	b_col = new_col.copy()
	rg_mask = img[:,:,2] > img[:,:,1]
	rb_mask = img[:,:,2] > img[:,:,0]
	gb_mask = img[:,:,1] > img[:,:,0]
	r_col[rg_mask & rb_mask] = img[rg_mask & rb_mask]
	g_col[gb_mask & ~rg_mask]= img[gb_mask & ~rg_mask]
	b_col[~rb_mask & ~gb_mask] = img[~rb_mask & ~gb_mask]
	dir_t = '.'.join(f_tmp.split('.')[:-1])
	if not os.path.isdir(dir_t):
		os.mkdir(dir_t)
	print('Saving color pop of', f_tmp, 'in', dir_t)
	img_name = dir_t.split('/')[-1]
	if cv2.imwrite(dir_t + '/red' + img_name + '.jpg', r_col):
		print('Saved Red')
	if cv2.imwrite(dir_t + '/green' + img_name + '.jpg', g_col):
		print('Saved Green')
	if cv2.imwrite(dir_t + '/blue' + img_name + '.jpg', b_col):
		print('Saved Blue')

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
