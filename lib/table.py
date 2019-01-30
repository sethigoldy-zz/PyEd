import config
import box

class Table(box.Box):
	cols = []
    
	def __init__(self,name):
		box.Box.__init__(self, name, datatype, size, position)
		self.name = name

	def addCols(col):
		self.cols.append(col)

	def calculateSize(self):
		self.yCordinate = self.position*config.COLOUMN_BOX_HEIGHT
		self.width = len(self.name)*config.CHARACTER_LENGTH + config.MINIMUM_PADDING_LEFT_RIGHT*2 # for both sides
		self.height = config.COLOUMN_BOX_HEIGHT
