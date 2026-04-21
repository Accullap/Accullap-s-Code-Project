import numpy as np
import matplotlib.pyplot as plt

#def quadratic(x, a):
    #return x**a

#x = np.linspace(-4, 4, 100)
#y = quadratic(x, 4)

#x = np.linspace(-2*np.pi, 2*np.pi, 500)

#for alpha in [1, -2, 3]:
    #y = np.exp(np.sin(x))*np.cos(alpha * x)**3

    #if alpha == 1:
        #color = "blue"
    #elif alpha == -2:
        #color = "red"
    #else:
        #color = "green"

    #plt.plot(x, y, color=color, label=f'alpha = {alpha}', marker = "o")


days = np.array([1, 2, 3, 4, 5, 6, 7])
temp_day =   [22, 25, 19, 30, 28, 24, 21]
temp_night = [12, 14, 10, 18, 16, 13, 11]

plt.plot(days, temp_day, color='red', linestyle='--', 
         marker='o', markersize=6, label='Day temp')

plt.plot(days, temp_night, color='blue', 
         marker='o', markersize=6, label='Night temp')

plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature over one week')
plt.legend()
plt.grid()
plt.show()
