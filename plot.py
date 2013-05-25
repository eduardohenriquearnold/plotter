#Matplotlib
import matplotlib
matplotlib.use('GTK3Agg')

#from matplotlib.figure import Figure
from matplotlib.pyplot import figure as Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

from numpy import *

class Plot:
    
    def __init__(self, builder):
        self. builder = builder

        #Precision between points
        self.prec2D = 0.10
        self.prec3D = 0.25

    def update_canvas(self, canvas):
        sw = self.builder.get_object("graphArea")

        if sw.get_child() is not None:
            sw.get_child().destroy()

        sw.add_with_viewport(canvas)
        self.builder.get_object("window1").show_all()
    

    def showPlot2D(self, x, y, squared):
        if squared:
            asp = 'equal'
        else:
            asp = 'auto'

        fig = Figure(dpi=100, frameon=False)
        a = fig.add_subplot(111, aspect=asp)

        a.plot(x,y)

        canvas = FigureCanvas(fig)
        self.update_canvas(canvas)

    def showPlot3D(self,x,y,z):
        fig = Figure(dpi=100, frameon=False)
        a = fig.add_subplot(111, projection='3d')

        a.plot_surface(x,y,z, rstride=4, cstride=4,  linewidth=0, color='b')

        canvas = FigureCanvas(fig)

        #Makes possible to rotate the plot
        a.mouse_init()

        self.update_canvas(canvas)

    def f2DParametric(self, x, y, interval, squared):
        minT, maxT = self.convertInterval(interval)
        t = arange(minT, maxT, self.prec2D)

        try:
            x = eval(x)
            y = eval(y)
        except:
            raise Exception("Couldn't resolve the equation")

        self.showPlot2D(x,y, squared)

    def fOneVar(self, f, interval, squared):
        f = f.replace('x', 't')

        self.f2DParametric('t', f, interval, squared)

    def f3DParametric(self, x, y, z, intervalU, intervalV):
        minU, maxU = self.convertInterval(intervalU)
        minV, maxV = self.convertInterval(intervalV)

        u = arange(minU, maxU, self.prec3D)
        v = arange(minV, maxV, self.prec3D)
        u, v = meshgrid(u, v)

        try:
            x = eval(x)
            y = eval(y)
            z = eval(z)
        except:
            raise Exception("Couldn't resolve the equation")

        self.showPlot3D(x,y,z)

    def fTwoVar(self, f, intervalX, intervalY):
        f = f.replace('x', 'u')
        f = f.replace('y', 'v')

        self.f3DParametric('u', 'v', f, intervalX, intervalY)

    def convertInterval(self, intervalStr):
        interval = intervalStr.split(':')

        try:
            min, max = interval[0], interval[1]
            min, max = eval(min), eval(max)
        except:
            raise Exception("Couldn't resolve the interval")

        return min, max
        

