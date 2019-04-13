import random
import csv
import copy

def ccw(pointA, pointB, pointC):
	return (int((pointB[0]-pointA[0]))*int((pointC[1]-pointA[1]))-int((pointB[1]-pointA[1]))*int((pointC[0]-pointA[0])))

def get_leftmost(arr):
	leftmost = arr[0]
	for i in arr:
		if(i[0] < leftmost[0]):
			leftmost = i
	return leftmost

shiftX = 0
shiftY = 0	
	
def make_leftmost_origin(arr):
	global shiftX
	global shiftY
	leftmost = get_leftmost(arr)
	shiftX = -leftmost[0]
	shiftY = -leftmost[1]
	for i in arr:
		i[0] += shiftX
		i[1] += shiftY
		
def verify_hull_integrity(hull):
	curlen = len(hull)-1
	if(curlen == 2):
		return
	if(ccw(hull[curlen-2], hull[curlen-1], hull[curlen])) < 0:
		del hull[curlen-1]
		verify_hull_integrity(hull)
	
delta = int(input("Enter range (-X to X): "))
Npoints = int(input("Enter number of points to create: "))
hull = []
sortedPoints = []
originalpoints = []
points = []
angles = {}
path = r"D:\Python\Custom\testfile.csv"			# Change to a valid path you can write to 

originalpoints = [[random.randint(-delta,delta), random.randint(-delta,delta)] for i in range(0,Npoints)]
print("\n")
print(originalpoints)

points = copy.deepcopy(originalpoints)
make_leftmost_origin(points)

for i in points:
	if i[0] == 0:
		origin = i
		hull.append(origin)
		continue
	angles[float(i[1])/float(i[0])] = i
	
for key in sorted(angles.keys(),reverse = True):
	 sortedPoints.append(angles[key])

while(len(sortedPoints) > 0):
	hull.append(sortedPoints.pop())
	curlen = len(hull)-1
	if(ccw(hull[curlen-2], hull[curlen-1], hull[curlen])) < 0:
		del hull[curlen-1]
		verify_hull_integrity(hull)
		
for i in hull:
	i[0] -= shiftX
	i[1] -= shiftY
hull.append(hull[0])
print("\nWith the original added to the end to wrap back around, the convex hull is:")
print(hull)

# Optional code to export to Excel for visual aid

xs = []
opxs = []
ys = []
opys = []

for i in hull:
	xs.append(i[0])
	ys.append(i[1])
	
for i in originalpoints:
	opxs.append(i[0])
	opys.append(i[1])
	
with open(path, 'w', encoding="utf-8") as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(opxs)
	wr.writerow(opys)
	wr.writerow(xs)
	wr.writerow(ys)