# Python CourseWork
# Showdesh Limbu
# 811334

from graphics import *

#Get the main funtion
def main():
    size, colours = getInput()
    win = GraphWin("CourseWork", size * 100, size * 100)
    drawPatches(win, size, colours)
    
#Draw the patch 
def drawPatches(win, size, colours):
    row = []
    
    yCounter = 0
    for i in range (size):
        row.append(0)
    aCounter = 0
    bCounter = size
    patchInMiddle = False
    middlePatch = (size - 1) / 2
    for j in range(len(row)):
        xCounter = 0
        for k in range (aCounter, bCounter, 1):
            row[k] = 1
        if j == middlePatch:
            patchInMiddle = True
        if patchInMiddle:
            aCounter = aCounter - 1
            bCounter = bCounter + 1
        else:
            aCounter = aCounter + 1
            bCounter = bCounter - 1
        
        for i in row:
            if i == 0:
                if xCounter < middlePatch * 100:
                    drawPatch1(win,xCounter, yCounter, colours[1])
                else:
                    drawPatch1(win,xCounter, yCounter, colours[2])
            else:
                drawPatch2(win, xCounter, yCounter, colours[0])
            xCounter = xCounter + 100
        yCounter = yCounter + 100    
        for l in range(len(row)):
            row[l] = 0

# Draw Patch1            
def drawPatch1(win, xStart, yStart, colour):
    win.setBackground("white")
    for x in range(xStart + 10, xStart + 100, 40):
        for y in range(yStart + 10, yStart + 100, 20):
            drawCircle(win, Point(x, y), colour)
            drawRectangle(win, Point(x, y - 10), Point(x - 10, y + 10), "white")
            drawOutsideCircle(win, Point(x, y), colour)
    for x in range (xStart + 30, xStart + 100, 40):
        for y in range(yStart + 10, yStart + 100, 20):
            drawCircle(win, Point(x, y), colour)
            drawRectangle(win, Point(x - 10, y), Point(x + 10, y + 10), "white")
            drawOutsideCircle(win, Point(x, y), colour)
            
# Draw Patch2            
def drawPatch2(win, xStart, yStart, colour):
    win.setBackground("white")
    for x in range(xStart + 20, xStart + 100, 20):
        drawLine(win, Point(x, yStart), Point(x, yStart + 100), colour)
    for y in range(yStart+20, yStart + 100, 20):
        drawLine(win, Point(xStart, y), Point(xStart + 100, y), colour)
    
    for y in range(yStart + 10, yStart + 100, 20):
        for x in range(xStart + 10, xStart +100, 20):
            printHi(win, Point(x, y), colour)
# Hi!
def printHi(win, point, colour):
    text = Text(point, "hi!")
    text.setFill(colour)
    text.setSize(10)
    text.draw(win)

# Draw Lines
def drawLine(win, p1, p2, colour):
    line = Line(p1, p2)
    line.setFill(colour)
    line.draw(win)
    
# Draw PatchA
def drawCircle(win, centre, colour):
    circle = Circle(centre, 10)
    circle.setFill(colour)
    circle.draw(win)

# Draw Circle
def drawOutsideCircle(win, centre, colour):
    circle = Circle(centre, 10)
    circle.setOutline(colour)
    circle.draw(win)
    
# Draw Rectangle
def drawRectangle(win, p1, p2, colour):
    rect = Rectangle(p1, p2)
    rect.setFill(colour)
    rect.setOutline("")
    rect.draw(win)
    
# Get the input
def getInput():
    patchSize = ["5", "7", "9"]
    validColours = ["red", "green", "blue", "orange", "brown", "pink"]
    inputSize = input("Enter the window size: ")
    colours = []
    while(inputSize not in patchSize):
        print("Invalid Size", inputSize)
        inputSize = input("Enter the window size: ")
    inputSize = int(inputSize)
    for i in range(3):
        inputColour =  (input("Enter a colour: ")).lower()
        while(inputColour not in validColours or inputColour in colours):
            print("Invalid Colour, valid colours: ", validColours)
            inputColour = (input("Enter a colour: ")).lower()
        colours.append(inputColour)
    return inputSize, colours
        
main()
    



    
    