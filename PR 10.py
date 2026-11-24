import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(2, 3, 3)
plt.boxplot(y)
plt.title("Box Plot")

plt.subplot(2, 3, 4)
plt.bar(x, y)
plt.title("Bar Chart")

plt.subplot(2, 3, 5)
plt.pie(y, labels=x)
plt.title("Pie Chart")

plt.tight_layout()
plt.show()