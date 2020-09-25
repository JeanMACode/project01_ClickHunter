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

    menu()

    #Background Text
    clickSquares= Text(Point(300,300), "Click the Squares!")
    clickSquares.setFill("Green")
    clickSquares.draw(win)
    #Gameplay
    Gameplay()
    #Undraws the background text to showcase Final Score
    clickSquares.undraw()

    win.getMouse()
    win.close()

#Start Menu
def menu():
    startLine= Text(Point(300,300), "Click Hunt\nClick to Start!")
    startLine.setFill("Green")
    startLine.draw(win)
    win.getMouse()
    startLine.undraw()


# Gameplay
def Gameplay():
    #Variable to vount the amount of squares clicked
    Sum=0
    #Sets the timer
    Timer=60
    TimerEnd = time.time()+Timer
    BackTime= Text(Point(300,270),f"You have {Timer} seconds")
    BackTime.setFill("Green")
    BackTime.draw(win)

    while time.time() < TimerEnd :
        MpositionX= random.randint(100,300)
        MpositionY= random.randint(300,500)
        Mposition=Rectangle(Point(MpositionX,MpositionY),Point(MpositionY,MpositionX))
        MX=Mposition.getP1()
        MY=Mposition.getP2()
        Mposition.setFill(color_rgb(0,120,0))
        Mposition.draw(win)
    #Booleans that return a true thats gonna be used for the while
        check=win.getMouse()
        CHECKX1=check.getX() >= MX.getX() 
        CHECKX2=check.getX()<=MY.getX()
        CHECKY1=check.getY() >= MX.getY() 
        CHECKY2=check.getY()<=MY.getY()
        CHECKX=CHECKX1 == CHECKX2
        CHECKY=CHECKY1 == CHECKY2
    #Square Spawner
        while (CHECKX!=CHECKY):
            check=win.getMouse()
            CHECKX1=check.getX() >= MX.getX() 
            CHECKX2=check.getX()<=MY.getX()
            CHECKY1=check.getY() >= MX.getY() 
            CHECKY2=check.getY()<=MY.getY()
            CHECKX=CHECKX1 == CHECKX2
            CHECKY=CHECKY1 == CHECKY2
            
               
    #Eliminates the square if touched  
        Mposition.undraw()
    #Counts the squares you touched 
        Sum=Sum+1
    #Deletes the Text in the Background
    BackTime.undraw()
    
#Shows Final Score:
    End= Text(Point(300,300),f"Final Score:{Sum}")
    End.setFill("Green")
    End.draw(win)
    
main()



