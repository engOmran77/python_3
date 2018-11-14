import matplotlib.pyplot as plt
%matplotlib inline 

class Circle(object):
    
    def __init__(self,radius=3,color='blue'):
        
        self.radius=radius
        self.color=color 
    
    def add_radius(self,r):
        
        self.radius=self.radius+r
        return(self.radius)
    def drawCircle(self):
        
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

class Rectangle(object):
    
    def __init__(self,width=2,height =3,color='r'):
        self.height=height 
        self.width=width
        self.color=color
    
    def drawRectangle(self):
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
