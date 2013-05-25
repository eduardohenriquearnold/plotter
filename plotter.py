#python2

#GTK3
from gi.repository import Gtk

#MyPlotClass
import plot

def errorDialog(parent, mainTxt, subTxt):
    d = Gtk.MessageDialog(parent, 0, Gtk.MessageType.ERROR,
        Gtk.ButtonsType.CANCEL, mainTxt)

    d.format_secondary_text(subTxt)

    d.run()
    d.destroy()

def genPlot(button):
    currPage = builder.get_object("notebook1").get_current_page()

    try:
        if currPage == 0:
            f = builder.get_object("t1e").get_text()
            interval = builder.get_object("t1i").get_text()
            squared = builder.get_object("t1s").get_active()

            Plot.fOneVar(f, interval, squared)
        elif currPage == 1:
            x = builder.get_object("t2e1").get_text()
            y = builder.get_object("t2e2").get_text()
            interval = builder.get_object("t2i").get_text()
            squared = builder.get_object("t2s").get_active()

            Plot.f2DParametric(x, y, interval, squared)
        elif currPage == 2:
            f = builder.get_object("t3e").get_text()
            intervalX = builder.get_object("t3i1").get_text()
            intervalY = builder.get_object("t3i2").get_text()

            Plot.fTwoVar(f, intervalX, intervalY)
        elif currPage == 3:
            x = builder.get_object("t4e1").get_text()
            y = builder.get_object("t4e2").get_text()
            z = builder.get_object("t4e3").get_text()
            intervalU = builder.get_object("t4i1").get_text()
            intervalV = builder.get_object("t4i2").get_text()

            Plot.f3DParametric(x, y, z, intervalU, intervalV)
    except Exception as e:
        errorDialog(window, "Error!", str(e))

def changePrec(button):
    prec2D = builder.get_object("p2d").get_text()
    prec3D = builder.get_object("p3d").get_text()

    try:
        prec2D, prec3D = float(prec2D), float(prec3D)
    except:
        errorDialog(window, "Error!", "Invalid precision parameter")

    Plot.prec2D = prec2D
    Plot.prec3D = prec3D

builder = Gtk.Builder()
builder.add_from_file("plotter.glade")

handlers = {"close": Gtk.main_quit, "plot": genPlot, "changePrec": changePrec}
builder.connect_signals(handlers)

Plot = plot.Plot(builder)

window = builder.get_object("window1")
window.show_all()
window.maximize()

Gtk.main()


