#cartoon.py
#A cartoon face made with the graphics library
#By Ashley Cook

import graphics
from graphics import*
win = graphics.GraphWin()

#Background
bg =Rectangle(Point(0,0),Point(200,200))
bg.setFill('light blue')
bg.draw(win)

#Hair
hair = Polygon(Point(90,50), Point(110,50), Point(140,80), Point(145,145), Point(55,145),Point(60,80), Point(90,50))
hair.setFill('dark red')
hair.draw(win)

#Ears
leftear = Oval(Point(50,90),Point(70,110))
leftear.setFill('tan')
leftear.draw(win)
rightear = Oval(Point(130,90),Point(150,110))
rightear.setFill('tan')
rightear.draw(win)

#Earrings
lefter = Circle(Point(58,108),4)
lefter.setFill('hot pink')
lefter.draw(win)
righter =Circle(Point(142,108),4)
righter.setFill('hot pink')
righter.draw(win)

#Neck
neck =Rectangle(Point(90,130),Point(110,180))
neck.setFill('tan')
neck.draw(win)

#Face
center = Point(100,100)
circ = Circle(center, 40)
circ.setFill ('tan')
circ.draw(win)

#Mouth
line1 = Line(Point(90,120),Point(110,120))
line1.draw(win)
line2 = Line(Point(80,110), Point(90,120))
line2.draw(win)
line3 = Line(Point(110,120), Point(120,110))
line3.draw(win)

#Left eye
eye1 = Circle(Point(85,90), 10)
eye1.setFill ('white')
eye1.draw(win)
pupil1 = Circle(Point(85,90),5)
pupil1.setFill ('black')
pupil1.draw(win)

#Right eye
eye2 = Circle(Point(115,90), 10)
eye2.setFill ('white')
eye2.draw(win)
pupil2 = Circle(Point(115,90),5)
pupil2.setFill ('black')
pupil2.draw(win)

#Nose
nose = Oval(Point(95,105), Point(105,110))
nose.draw(win)

#Hat
hatrim = Rectangle(Point(60,60),Point(140,75))
hatrim.setFill('purple')
hatrim.draw(win)
hattop =Rectangle(Point(75,60),Point(125, 30))
hattop.setFill('purple')
hattop.draw(win)

#Bow
leftbow = Polygon(Point(100,60), Point(80,70),Point(80,50),Point(100,60))
leftbow.setFill('indigo')
leftbow.draw(win)
rightbow =Polygon(Point(100,60), Point(120, 70),Point(120,50),Point(100,60))
rightbow.setFill('indigo')
rightbow.draw(win)
mid= Circle(Point(100, 60), 8)
mid.setFill('indigo')
mid.draw(win)



#Shirt
shirt =Polygon(Point(90,150), Point(100,180),Point(110,150),Point(160,170),Point(160,200),Point(40,200),Point(40,170),Point(90,150))
shirt.setFill('pink')   
shirt.draw(win)



