from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from math import *



angle=0
xch=0
forward=True

def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(0.7, 0.7, 0.7, 1)
    glEnable(GL_DEPTH_TEST)

def drawcoor():

    glBegin(GL_LINES)
    glColor3f(1,0,0)

    glVertex(0,0,0)
    glVertex(0,10,0)

    glColor3f(1, 1, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(1, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)

    glEnd()



def drawrect(pnts, rectcol):
        glBegin(GL_POLYGON)
        glColor3f(rectcol[0], rectcol[1], rectcol[2])
        glVertex(pnts[0], pnts[1],pnts[2])
        glVertex(pnts[3], pnts[4],pnts[5])
        glVertex(pnts[6], pnts[7],pnts[8])
        glVertex(pnts[9], pnts[10],pnts[11])

        glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global angle
    global xch
    global forward
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    


    glColor3f(1,0.5,1)
    glTranslate(xch,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glColor3f(1, 0.5, 0.6)
    glTranslate(0,5,0)
    glScale(0.5,1,1)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(xch+2.5,0.7,-0.5)

    glutSolidSphere(0.3,10,10)

    glTranslate(0, 0, 1.4)

    glutSolidSphere(0.3, 10, 10)
#-----------------------------------------------------------------------------------

    glLoadIdentity()
    glColor3f(0,0,0)

    glTranslate(2.5,-0.5*0.25*5,0.5*0.5*5)

    glTranslate(xch,0,0)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glColor3f(0, 0, 0)

    glTranslate(-2.5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)

    glTranslate(xch,0,0)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glColor3f(0, 0, 0)

    glTranslate(2.5, -0.5 * 0.25 * 5,- 0.5 * 0.5 * 5)

    glTranslate(xch,0,0)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glColor3f(0, 0, 0)

    glTranslate(-2.5, -0.5 * 0.25 * 5,- 0.5 * 0.5 * 5)

    glTranslate(xch,0,0)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()

#--------------------------------------------------------------------------------------

    drawrect([10,0,-3,-30,0,-3,-30,1,-3.2,10,1,-3.2],[0,0,0])
    drawrect([10, 0, 3, -30, 0, 3, -30, 0, 4, 10, 0, 4], [0, 0, 0])

    drawrect([10, 4, 1.8, -30, 4, 1.8, -30, 5, -1, 10, 5, 0], [0.1, 0.8, 0.2])
    drawrect([10, 0, 4, -30, 0, 4, -30, 0, 10, 10, 0, 10], [0.1, 0.8, 0.2])

    drawrect([10, 5, 0, -40, 5, 0, -40, 7, -3, 10, 8, -3], [0, 0.9, 0.8])

    drawrect([1,-2,-1,1,-2,-2,-1,-2,-2,-1,-2,-1],[1,1,1])
    glTranslate(3,0,0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glLoadIdentity()
    glTranslate(-3,0,0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])

    glTranslate(-3, 0, 0)
    drawrect([1, -2, -1, 1, -2, -2, -1, -2, -2, -1, -2, -1], [1, 1, 1])


    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(5,7,0)
    glutSolidSphere(1,20,20)








    #--------------------------------------------------------------------------------------
    glutSwapBuffers()

    if forward==True:
      angle+=0.2
      xch+=0.005
      if xch > 5:
          forward=False
    else :
      angle -= 0.2
      xch -= 0.005
      if xch < -5:
        forward = True

#----------------------------------------------------------------------------------------
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow("first program")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

