class Rectangle : 

    def __init__(self, x1, y1, x2, y2) :
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show(self) :
        print('좌측상단꼭지점이({0},{1})이고 우측하단꼭지점이 ({2},{3})인 사각형입니다.'.format(self.x1, self.y1 , self.x2 , self.y2))

    def getWidth(self) :
        
        self.Width = self.x2 - self.x1 # 2
        
        return self.Width

    def getHeight(self) :

        self.Height = self.y1 - self.y2 

        return self.Height
    
    def getArea(self) :

        self.Area = self.Width * self.Height 
        
        return self.Area
    
    def getPerimeter(self) :

        self.Perimeter = self.Width * 2 + self.Height * 2

        return self.Perimeter


r1 = Rectangle(5,10,20,5)
r1.getWidth()
r1.getHeight()

a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')






