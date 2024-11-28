import matplotlib.pyplot as plt
# Data for the first graph
x1 = [2, 4, 6, 7]
y1 = [4, 3, 5, 1]

    # Data for the second graph
x2 = [1, 2, 3, 4]
y2 = [4, 2, 3, 1]

    # Plotting the first graph
plt.plot(x1, y1, label='Graph 1', color='b')

    # Plotting the second graph
plt.plot(x2, y2, label='Graph 2', color='r')

    # Adding title and labels
plt.title("Multiple Graphs in One Axes")
plt.xlabel("X axis")
plt.ylabel("Y axis")

    # Adding legend
plt.legend()

    # Display the plot
plt.show()