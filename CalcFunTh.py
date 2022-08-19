
from sympy import *
import numpy as np 
 
import matplotlib.pyplot as plt 
 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_aspect(1 ) 
 
def DrawXY(xFrom,xTo,steps,expr,color,label,plt):
    yarr = []
    xarr = np.linspace(xFrom ,xTo, steps) 
    for xval in xarr:
        yval = expr.subs(x,xval)
        yarr.append(yval)
    y_nparr = np.array(yarr) 
    plt.plot(xarr, y_nparr, c=color, label=label)    
 
def DrawRects(xFrom,xTo,steps,expr,color,plt):
    width = (xTo - xFrom)/steps
    xarrRect = []
    yarrRect = []
    area = 0
    xprev = xFrom
    for step in range(steps):
        yval = expr.subs(x,xprev + width)
        xarrRect.append(xprev)
        xarrRect.append(xprev)
        xarrRect.append(xprev + width)
        xarrRect.append(xprev + width)
        xarrRect.append(xprev)
        yarrRect.append(0)
        yarrRect.append(yval)
        yarrRect.append(yval)
        yarrRect.append(0)
        yarrRect.append(0)
        area += width * yval
        plt.plot(xarrRect, yarrRect, c=color)    
        xprev= xprev + width
    print('width =', width)
    print('area=',area)
    areaFinal = (integrate(expr, (x,xFrom,xTo)))
    print ('area final=',areaFinal)
 
def TangentLine(exprY,x0Val,xVal):
    diffExpr = diff(exprY)
    x1,y1,xo,yo = symbols('x1 y1 xo yo')
    expr = (y1-yo)/(x1-xo) - diffExpr.subs(x,x0Val)
    eq = expr.subs(xo,x0Val).subs(x1,xVal).subs(yo,exprY.subs(x,x0Val))
    eq1 = Eq(eq,0)
    solveY = solve(eq1)
    return xVal,solveY
 
def DrawTangentLine(exprY, x0Val,xVal1, xVal2, clr, txt):
    x1,y1 = TangentLine(exprY, x0Val, xVal1)
    x2,y2 = TangentLine(exprY, x0Val, xVal2)
    plt.plot([x1,x2],[y1,y2], color = clr, label=txt)
    
def Newton(expr, x0):
    ret = x0 - expr.subs(x, x0)/ expr.diff().subs(x,x0)
    return ret
 
x = symbols('x')
expr = sin(x)

###################################################### 
    # xFrom,xTo,steps,expr,color,label,plt
DrawXY( 0, np.pi, 100,expr,'blue', '',plt)
DrawRects(0,np.pi,100,expr,'green',plt)

#plt.legend(loc='lower right')
plt.show()