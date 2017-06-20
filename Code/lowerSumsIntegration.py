import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.ion()

funcRange = [-4, 4]
interval = funcRange[1] - funcRange[0]
steps = 2
miniSteps = 0.001
colour = 'red'
graphColour = 'blue'
iteration = 10
function = 'x**3 - 6*x'

X = []
y = []
x = funcRange[0]
while x <= funcRange[1]:
    X.append(x)
    y.append(eval(function))
    x += miniSteps

for i in range(iteration):
    plt.clf()
    plt.plot(X, y, color=graphColour)
    x = funcRange[0]
    jump = interval/steps
    for j in range(steps):
        plt.plot([x, x], [0, eval(function)], color=colour)
        plt.plot([x, (x+jump)], [eval(function), eval(function)],
                 color=colour)
        plt.plot([(x+jump), (x+jump)], [eval(function), 0], color=colour)
        x += jump

    steps *= 2
    plt.xlabel('x')
    plt.ylabel('f(x)')
    x = funcRange[1]
    plt.text(1.1*funcRange[1], eval(function), 'i='+str(i+1))
    plt.show()
    plt.pause(0.5)
    
