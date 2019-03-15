Problem Statements

Exercise 1 
Write a Python program that uses uniform(-1,1) from the library
random in order to generate N (x, y) data points, and then count how many
are within the circle of radius 1. It should record its value after N data points.
Then repeat this 100 times (with N data points each time). Find the mean
value, and the uncertainty of the mean. (Reminder: the uncertainty of the mean
is defined as σ/√
M where σ is the standard deviation of your 100 values you
are averaging, and M = 100 is how many values you are averaging.) Plot your
means with your estimated uncertainties of the means as a function of N, using
the values of N = 2i
for i of integer values 8, 9, 10, 11, 12, 13. Your graph
should also include a horizontal line with the exact value (π/4). A semi-log plot
is probably your best bet.

Exercise 2 
Estimate R 1
0
sin2
(1/x) dx. This cannot be solved analytically. Looking at the function, we know the graph lies inside the box defined by 0 ≤ x ≤ 1
and 0 ≤ y ≤ 1. Thus you can use the uniform function to pick random points in
that box, and see if they fall under the curve. That ratio will be the ratio of the
areas (the area of the box is 1). You should do this the same way as in Exercise
1: generate N data points (where N = 2i with i integer values from 8 to 13), do
this 100 times, and find the mean and the uncertainty of the mean. Plot a graph
which is similar to the graph which you produced in Exercise 1. Hint: You can
almost completely reuse your code from Exercise 1, you just have to change a
couple of lines.