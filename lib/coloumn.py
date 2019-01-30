import config
import box

class Coloumn(box.Box):
	
	position = 0
	def __init__(self, name, datatype, size, position):
		box.Box.__init__(self, name, datatype, size, position)
		self.position = position
		self.calculateSize()

	def calculateSize(self):
		self.yCordinate = self.position*config.COLOUMN_BOX_HEIGHT
		self.width = len(self.name)*config.CHARACTER_LENGTH + config.MINIMUM_PADDING_LEFT_RIGHT*2 # for both sides
		self.height = config.COLOUMN_BOX_HEIGHT

