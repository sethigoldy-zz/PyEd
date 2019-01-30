from PIL import ImageFont

class Box:
	name = "" # in terms of db
	datatype = "" # in terms of db varchar,string,int
	size = 0 # in terms of db
	xCordinate = 0 # will be in respect to table position
	yCordinate = 0 # will be in respect to table position
	width = 0
	height = 0
	
	def __init__(self, name, datatype, size, position):
		self.name = name
		self.datatype = datatype
		self.size = size
		self.position = position

	def draw(self, parentPosition, width, draw):
		#fnt = ImageFont.load_default()
		fnt = ImageFont.truetype("Sarabun-Light.ttf",15)
		textSize = fnt.getsize(self.name)
		
		x0 = parentPosition[0]
		y0 = parentPosition[1] + self.yCordinate
		x1 = x0 + self.width
		y1 = y0 + self.height
		draw.rectangle([(x0,y0),(x1,y1)],outline='black')
		tx = self.width - textSize[0]
		tx = tx/2
		ty = (self.height - textSize[1])/2
		tx = x0 + tx
		ty = y0 + ty 
		draw.text((tx,ty),self.name,  font=fnt, fill='black')
