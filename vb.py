import matplotlib.pyplot as plt


x = range(0,10)
y = range(10, 20)


#plotting
plt.figure()

plt.scatter(x, y, c='k')


# opmaak
plt.xlabel("$x$", c='violet')
plt.ylabel("$y$", c='green')
plt.grid()

plt.show()

