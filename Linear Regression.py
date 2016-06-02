from numpy import loadtxt, array, linspace
from pylab import scatter, show, title, xlabel, ylabel, plot, legend

#Input the data
data = loadtxt('HeightWeightData.txt', delimiter='    ')

#Seperate the x values from the y values
X, Y = data[:, 0], data[:, 1]

#Calculate the mean
def mean(data):
    total = 0
    for datum in data:
        total += datum
    mean = total / data.size
    return mean

meanX, meanY = mean(X), mean(Y)
#print('Mean of X: ' + str(meanX))
#print('Mean of Y: ' + str(meanY))

#Calculate the standard deviation
def standardDeviation(mean, data):
    total = 0
    for datum in data:
        total += ((datum - mean) ** 2)
    variance = total / data.size
    standardDeviation = variance ** 0.5
    return standardDeviation

sdx, sdy = standardDeviation(meanX, X), standardDeviation(meanY, Y)
#print('Standard deviation of X: ' + str(sdx))
#print('Standard deviation of Y: ' + str(sdy))

#Calculate the correlation coefficient
def correlationCoefficient(X, Y, meanX, meanY):
    x, y = [], []
    for i in X:
        x.append(i-meanX)
    for i in Y:
        y.append(i-meanY)
    xyTotal = 0
    for num in range(0, len(x)):
        xyTotal += x[num]*y[num]
    #print('xy: ' + str(xyTotal))
    xSquaredTotal = 0
    for i in x:
        xSquaredTotal += i**2
    #print('xSquaredTotal: ' + str(xSquaredTotal))
    ySquaredTotal = 0
    for i in y:
        ySquaredTotal += i**2
    #print('ySquaredTotal: ' + str(ySquaredTotal))
    correlation = xyTotal / ((ySquaredTotal * xSquaredTotal) ** 0.5)
    #print('Correlation coefficient: ' + str(correlation))
    return correlation

correlation = correlationCoefficient(X, Y, meanX, meanY)

#Generate the equation of the line
b = correlation * (sdy / sdx)
A = meanY - (b * meanX)
if A < 0:
    equation = ('y = ' + str(b) + 'x - ' + str(-1*A))
elif A > 0:
    equation = ('y = ' + str(b) + 'x + ' + str(A))
else:
    equation = ('y = ' + str(b) + 'x')
print('Equation: ' + str(equation))

#Plot the data
firstnum = min(X-0.3)
lastnum = max(X+0.3)
scatter(data[:, 0], data[:, 1], marker='o', c='b', label='Height/weight')
xvalues = linspace(firstnum, lastnum, 2, endpoint=True)
yvalues = linspace(((firstnum*b)+A), ((lastnum*b)+A), 2, endpoint=True)
plot(xvalues, yvalues, label=equation, color='red')
legend(loc='best', fontsize='medium')
title('Height/weight distribution'), xlabel('Height (inches)'), ylabel('Weight (lbs)')
show(block=False)

#Allow user to enter a value and receive a predicted value for the other variable
predict = 'Weight'
while predict.title() not in ('N', 'No'):
    predict = raw_input('\nWould you like to predict a height or a weight? (enter \'H\', \'W\' or \'No\'): ')
    while predict.title() not in ('W', 'Weight', 'H', 'Height', 'N', 'No'):
        print('Please enter a valid answer...')
        predict = raw_input('\nWould you like to predict a height or weight? (enter \'H\', \'W\' or \'No\'): ')
    if predict.title() in ('W', 'Weight'):
        height = float(input('Please enter a height (inches): '))
        weight = (b * height) + A
        print('The predicted weight for a height of ' + str(height) + ' inches is ' + str(weight) + ' lbs')
    elif predict.title() in ('H', 'Height'):
        weight = float(input('Please enter a weight (lbs): '))
        height = (weight - A) / b
        print('The predicted height for a weight of ' + str(weight) + ' lbs is ' + str(height) + ' inches')
    elif predict.title() in ('N', 'No'):
        print('')
