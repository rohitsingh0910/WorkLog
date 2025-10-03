classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
classes.sort(key=lambda c: c[0] / c[1])
classes[0][0] += extraStudents
classes[0][1] += extraStudents
from functools import reduce
s = reduce(lambda acc, c: acc + (c[0] / c[1]), classes, 0)
print(s/len(classes))