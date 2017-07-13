'''
Author : Atul Kumar

Take excel sheet and extract names from column
then generate certificates for these names using 
provided certificate template in .jpg format.

For www.geeksforgeeks.org

'''


import xlrd
from PIL import Image,ImageFont,ImageDraw,ImageColor
import settings

def parse_xls(xls_path,target_col):
	'''
	parse excel sheet and return the
	target column's data
	'''

	xls = xlrd.open_workbook(xls_path)
	first_sheet = xls.sheet_by_index(0)

	# assumes there is column header
	data = first_sheet.col_values(target_col)[1:]
	return data

def write_image(img, template, font_path,
				font_size,font_color,x,y,
				spacing_px=15,):
	'''
	Write the text templete on the image file
	on x,y coordinates
	'''

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(font_path,font_size)
	font_color = ImageColor.getrgb(font_color)
	draw.multiline_text((x,y),template,fill=font_color,
		font=font,spacing=spacing_px)
	return img


def main():
	'''
	Driver program
	'''
	template = Image.open(settings.IMG_PATH)
	names = parse_xls(settings.XLS_PATH,settings.TARGET_COL)
	for name in names:
		# create a copy of original image template
		tmp_img = template.copy()

		# insert 'name' in text template
		TXT_TEMPLATE = settings.TXT_TEMPLATE.format(name)

		tmp_img = write_image(tmp_img,TXT_TEMPLATE,
					settings.FONT_PATH,settings.FONT_SIZE,
					settings.FONT_COLOR,settings.X, settings.Y,
					settings.SPACING_PX,)

		# save generated image at given target
		tmp_img.save("{}{}.jpg".format(settings.TARGET_PATH, name))

	print("Certificates generated successfully!")


if __name__ == '__main__':
	main()