from graphics import *
import random
import time

#Este programa se trata de darle click a los rectangulos con la clase graphics, estos van a aparerecer en la pantalla aleatoriamente 
# y el jugador tiene que darle clicks a todos los cuadros que hayan antes de que se acabe el tiempo.
# Este juego tiene un timer y va a ver al final cuantos pudiste darle click cuando se acabe el timer, el timer se va a implementar con la clase time.

#OJO: Este programa no fue basado en otro codigo(No se uso un programa diferente como referencia)


win=GraphWin("Click Hunt",600,600)
win.setBackground("Black")

def main():

    #Click to start the game
    menu()

    #Background Text
    Background=BackgroundText(win)

    #Gameplay
    Gameplay(win)

    #Undraws the background text to showcase Final Score
    Background.undraw()

    #Click to Exit
    win.getMouse()
    win.close()


#Text that appears during Gameplay
def BackgroundText(win):
    clickCircles= Text(Point(300,300), "Click the Figures!")
    clickCircles.setFill("Green")
    clickCircles.draw(win)
    return clickCircles


#Start Menu
def menu():
    startLine= Text(Point(300,300), "Click Hunt\nClick to Start!")
    startLine.setFill("Green")
    startLine.draw(win)
    win.getMouse()
    startLine.undraw()

#Sets the amount of Time that the while loop will run
def setTimer():
    Timer=60
    TimerEnd = time.time()+Timer
    return Timer,TimerEnd


#sets the center coordinates to appear in
def Spawner():

    radius=random.randint(4,30)

    Mdecision=random.randint(1,80)
    #multiple decisions to assure that the figures appears more randomly
    if (20>Mdecision>10):
        MpositionX= random.randint(10,30)
        MpositionY= random.randint(40,50)
            
    elif (30>Mdecision>20):
        MpositionX= random.randint(100,300)
        MpositionY= random.randint(400,500)
            
    elif (40>Mdecision>30):
        MpositionX= random.randint(20,300)
        MpositionY= random.randint(300,350)
            
    elif (50>Mdecision>40):
        MpositionX= random.randint(500,540)
        MpositionY= random.randint(400,500)
            
    elif (60>Mdecision>50):
        MpositionX= random.randint(100,300)
        MpositionY= random.randint(30,300)
           
    elif (70>Mdecision>60):
        MpositionX= random.randint(50,500)
        MpositionY= random.randint(60,110)
            

    elif (80>Mdecision>70):
        MpositionX= random.randint(20,300)
        MpositionY= random.randint(300,500)
            
    else: 
        MpositionX= random.randint(100,520)
        MpositionY= random.randint(100,550)


    return MpositionX, MpositionY, radius



#Checks if the mouse clicked the figure
def Check(radius,Mposition):
    check=win.getMouse()
    ClickCount=1
    dx=check.getX() - Mposition.getCenter().getX()
    dy=check.getY() - Mposition.getCenter().getY() 
    distance=(dx**2 + dy**2)**(1/2)


    while (distance>=radius):
        check=win.getMouse()
        dx=check.getX() - Mposition.getCenter().getX()
        dy=check.getY() - Mposition.getCenter().getY() 
        distance=(dx**2 + dy**2)**(1/2)
        ClickCount+=1
    return ClickCount

# Gameplay
def Gameplay(win):

    #Variable that counts the amount of clicks
    ClickAmount=0

    #Variable to count the amount of circles clicked
    Sum=0

    #Sets the timer
    Timer,TimerEnd=setTimer()
    
    while time.time() < TimerEnd :

        MpositionX,MpositionY,radius= Spawner()
        Mposition=Circle(Point(MpositionX,MpositionY),radius)
        Mposition.setFill(color_rgb(0,120,0))
        Mposition.draw(win)


        Checking_Clicks=Check(radius,Mposition)
        ClickAmount+=Checking_Clicks
                
    #Eliminates the circle if touched  
        Mposition.undraw()
    #Counts the circles you touched 
        Sum=Sum+1
    
    
#Shows Final Score and amount of clicks:
    TimerUsed=Text(Point(300,260),f"With {Timer} seconds your results are:")
    TimerUsed.setFill("Green")
    FinalScore= Text(Point(300,300),f"Final Score:{Sum}")
    FinalScore.setFill("Green")
    Amount_of_Clicks=Text(Point(300,340),f"Amount of clicks: {ClickAmount}")
    Amount_of_Clicks.setFill("Green")

    TimerUsed.draw(win)
    FinalScore.draw(win)
    Amount_of_Clicks.draw(win)
main()



