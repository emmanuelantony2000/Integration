import time
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.ion()

def plotting(func, fr, miniSteps, colour):
    X = []
    y = []
    x = fr[0]
    while x <= fr[1]:
        X.append(x)
        y.append(eval(func))
        x += miniSteps

    plt.plot(X, y, color=colour)

funcRange = [-4, 4]
interval = funcRange[1] - funcRange[0]
steps = 2
colour = 'red'
iteration = 10
function = 'x**3 - 6*x'

for i in range(iteration):
    plt.clf()
    plotting(function, funcRange, 0.001, 'blue')
    x = funcRange[0]
    jump = interval/steps
    for j in range(steps):
        plt.plot([x, x], [0, eval(function)], color='red')
        plt.plot([x, (x+jump)], [eval(function), eval(function)], color='red')
        plt.plot([(x+jump), (x+jump)], [eval(function), 0], color='red')
        x += jump

    steps *= 2
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    plt.pause(0.5)
    #time.sleep(2)
    
