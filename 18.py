 # This problem could probably be represented as a graph with adjacent nodes linked together
 # something like Bellman-Ford 

 # sum up 2 adjacent node pairs and try to merge them together to get to the final answer
"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

"""
class triangle_node:
    # the triangle has a row and position property, e.g. top = row 1, left = position 1
    def __init__(self, value, row, position, *argv):
        self.value = value
        self.row = row
        self.position = position
        self.path_history = [position] if not argv else argv[0]
        
    def merge_downwards(self, node):
        # create a merged node with new properties
        new_node = triangle_node(
            (self.value + node.value),
            (node.row),
            (node.position),
            (self.path_history + [node.position]))
        return new_node
        
    def merge_upwards(self, node):
        # create a merged node with new properties
        new_node = triangle_node(
            (self.value + node.value),
            (node.row),
            (node.position),
            ([node.position] + self.path_history))
        return new_node

i = triangle_node(3, 1, 1)
j = triangle_node(7, 2, 1)
k = triangle_node(4, 3, 2)
l = triangle_node(9, 4, 3)
print(i.value, i.row, i.position, i.path_history)
y = i.merge_downwards(j).merge_downwards(k).merge_downwards(l)
print(y.value, y.row, y.position, y.path_history)

z = l.merge_upwards(k)
print(z.value, z.row, z.position, z.path_history)
w = i.merge_downwards(j).merge_downwards(z)
print(w.value, w.row, w.position, w.path_history)

# need to convert the data into a giant triangle structure storing nodes
# and write functions to iterate through the giant triangle while operating on nodes
# the triangle after each operation should lose the top row and the bottom row, and the 2nd and 2nd last rows
# should be new nodes with the maximum values and path histories stored together.

