import matplotlib.pyplot as plt
from matplotlib import style
from math import sin, cos, tan, pi

style.use('ggplot')
plt.ion()

funcRange = [-5.2, 5.2]
interval = funcRange[1] - funcRange[0]
steps = 2
miniSteps = 0.001
area = 0.0
colour = 'yellow'
colourRectangle = 'blue'
iteration = 8
function = '(x**2 - 1)*(x**2 - 4)*(x**2 - 9)*(x**2 - 16)*(x**2 - 25)'

X = []
y = []
x = funcRange[0]
while x <= funcRange[1]:
    X.append(x)
    y.append(eval(function))
    x += miniSteps

for i in range(iteration):
    area = 0.0
    plt.clf()
    plt.plot(X, y, color=colour)
    x = funcRange[0]
    jump = interval/steps
    for j in range(steps):
        x += jump
        plt.plot([x, x], [0, eval(function)], color=colourRectangle)
        plt.plot([x, (x-jump)], [eval(function), eval(function)],
                 color=colourRectangle)
        plt.plot([(x-jump), (x-jump)], [eval(function), 0],
                 color=colourRectangle)
        area += (jump * eval(function)) if (jump * eval(function)) >= 0 \
                else -(jump * eval(function))

    steps *= 2
    plt.xlabel('x')
    plt.ylabel('f(x)')
    x = funcRange[1]
    plt.text((x+(interval/32)), (eval(function)+(interval/32)),
             ('Area = '+str(area)))
    x = funcRange[0]
    plt.text((x-(interval/32)), (eval(function)+(interval/32)),
             ('i = '+str(i+1)))
    plt.show()
    plt.pause(0.5)
    
