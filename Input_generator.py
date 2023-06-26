# generate files
import numpy as np
import sys

input_file_name = input("Please enter a name for the input file: ")


nb_vertices = input("Please enter the number of vertices: ")

# checking if the input is a digit
while nb_vertices.isdigit() != True:
    print("Please enter a digit and not a character! ")
    nb_vertices = input("Please enter the number of vertices: ")
    if nb_vertices.isdigit() == True:
        break

percent_edges = input(
    "Please enter the percentage of edges between the vertices (1-100) : ")

while percent_edges.isdigit() != True or int(percent_edges) == 0 or int(percent_edges) > 100:
    print("Wrong input! Please make sure to enter a digit between 1 and 100...")
    percent_edges = input(
        "Please enter the percentage of edges between the vertices (1-100) : ")
    if percent_edges.isdigit() == True and int(percent_edges) > 0 and int(percent_edges) < 100:
        break

max_nb_edges = int(nb_vertices)*(int(nb_vertices)-1)/2

nb_edges = max_nb_edges*(int(percent_edges)/100)
nb_edges = int(nb_edges)

print("number of edges is: " + str(nb_edges))

if nb_edges == 0:
    print("There is no edges for this graph!!! Run the input generator again.")
    sys.exit()

list_vertices = []

for i in range(int(nb_vertices) + 1):
    if i != 0:
        list_vertices.append(i)

print(list_vertices)

with open(input_file_name + ".txt", "w") as f:
    f.write(str(list_vertices) + "\n")
f.close()

list_edges = []


same_element = False
loop_finished = False
while loop_finished == False:
    a = np.random.randint(1, int(nb_vertices) + 1)
    b = np.random.randint(1, int(nb_vertices) + 1)
    for i in list_edges:
        if i == [a, b] or i == [b, a]:
            same_element = True

    if a != b and same_element == False:
        list_edges.append([a, b])
    if len(list_edges) == nb_edges:
        loop_finished = True
        break
    same_element = False
print(list_edges)
# print(len(list_edges))

with open(input_file_name + ".txt", "a") as f:
    f.write(str(list_edges))
f.close()
