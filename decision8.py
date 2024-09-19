''''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
''''
a = int(input())
b = int(input())
c = int(input())
allocated_lab = input()
available_labs = []
if allocated_lab != "L1":
    available_labs.append(a)
if allocated_lab != "L2":
    available_labs.append(b)
if allocated_lab != "L3":
    available_labs.append(c)
if min(available_labs) == a:
    print("L1")
elif min(available_labs) == b:
    print("L2")
else:
    print("L3")
