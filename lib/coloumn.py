import config

class Coloumn:
    name = ""
    datatype = ""
    size = 0
    position = 0
    xCordinate = 0 # will be in respect to table position
    yCordinate = 0 # will be in respect to table position
    width = 0

    def __init(self, name, datatype, size, position):
        self.name = name
        self.datatype = datatype
        self.size = size
        self.position = position
        self.calculateSize()

    def calculateSize(self):
        self.yCordinate = self.position*COLOUMN_BOX_HEIGHT
        self.width = len(self.name)*CHARACTER_LENGTH + MINIMUM_PADDING_LEFT_RIGHT*2 # for both sides

    def draw(self, parentPosition, width, draw):
        x0 = parentPosition[0]
        y0 = parentPosition[1] + self.yCordinate
        x1 = x0 + width
        draw.rectangle([(x0,y0),(x1,y1)])
