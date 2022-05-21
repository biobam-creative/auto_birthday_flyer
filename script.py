from datetime import date, time, timedelta
from PIL import Image, ImageDraw, ImageFont
import csv


class BirthdayWisher:
	
	def __init__(self, dob, name, photo,template):
		self.name = name
		self.dob = dob
		self.today = date.today()
		self.photo = photo
		self.template = template
		
	def age_calc(self):
		age = self.today - self.dob
		return age/365
		
	def generate_card(self,size):
		template = Image.open(self.template)
		otw, oth = template.size
		given_width, given_height = size
		print(size)
		
		new_template = template.resize((given_width,given_height))
		print(new_template.size)
				
		d1 = ImageDraw.Draw(new_template)
				
		photo = Image.open(self.photo)
		
		opw,oph = photo.size
		
		gw = int(0.6*given_width)
		gh = int(0.6*given_height)
				
		resize_ph = photo.resize((gw,gh))
				
		mask_im = Image.new("L", resize_ph.size, 0)
		draw = ImageDraw.Draw(mask_im)
		
		
		
		draw.ellipse((0, 0, gw, gh), fill=255)
		mask_im.save('mask_circle.jpg', quality=95)
		
		
		a = gw*0.5
		b = gh*0.5
				
		pos_x = int(given_width*0.5-a)
		pos_y = int(given_height*0.5-b)
				
		x = int(given_width*0.02)
		y = int(given_height*0.02)	
		
		c = 0.82*given_width
		d = 0.82*given_height
			
		d1.ellipse((pos_x-x,pos_y-y,pos_x+gw+x,pos_y+gh+y),fill=(255,255,255))
		print(c-x,d-y,c+gw+x,d+gw+y,gw,gh)
				
		new_template.paste(resize_ph,(pos_x, pos_y), mask_im)
				
		myfont = ImageFont.truetype('static/Raleway-Black.ttf', int(given_height*0.06))
				
		d1.text((pos_x,pos_y+gh*0.5),self.name, font = myfont, fill=(255,255,255))
				
		new_template.save(self.name+'flyer.jpg', quality=95)
		return 'generated'
				

obj = BirthdayWisher(name='Emmanuel',photo='babayara.jpg',template='template.jpg', dob=date(1990,12,27))

obj.generate_card(size=(10000,10000))

#today = str(date.today())

#with open('B-day.csv','r')as file:
#	reader = csv.reader(file)
#	for index, row in enumerate(reader):
#		if index != 0:
#			name = row[0]
#			bday = row[1]
#			
#			if today[5:] == bday[5:]:
#				print('yes')

				
				
				