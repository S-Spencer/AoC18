"""
meta_sum finds the sum of all meta data in input licence
For a given node on the tree, the first number denotes the number of child branches, the second number of meta data entries
Next comes any child branches, including its own children and meta data entries
After all child branches are listed, then the nodes meta data entries are listed
For a given node, meta sum reads the number of child branches (child) and meta data (meta), and initiates a running total of the sum of meta data (total_meta)
If a node has child branches, the function calls itself to find the sum of the meta data on the child branches, which is added to total_meta.
After all child branches have returned their meta_sum - or if a node has no children - its own meta data is added to total_meta
Once a node has returned its meta_sum, it is deleted to collapse the tree down
This is done to make it easier for a node higher up the tree to identify its own meta data (see line 22)
"""
def meta_sum(string,i):
    child = int(string[i])
    meta = int(string[i+1])
    total_meta = 0
    if child > 0:
        j = 1
        while j <= child:
            result = meta_sum(string,i+2)
            total_meta += result
            j += 1
    for k in range(i + 2, i + 2 + meta):
        total_meta += int(string[k])
    del string[i: i + meta + 2]
    return total_meta
"""
node_value finds the value of a root node
If a node has no child nodes, its value is the sum of its meta data
If it has a child node, the meta data acts as indecies for the child nodes. The nodes value is the sum of the indexed child nodes values
If the index is greater than the number of child nodes, it returns 0
child and meta are the same as in meta_sum. node stores the sum of all node values
If a node has no children, it adds the sum of the meta data to node value, then deletes the node to allow higher nodes to read their own meta data
If a node has child nodes, it calls node_value to find the value of the child nodes and stores it in a list (children)
Using the meta data values as specific indecies, node values from children are added to the total.
This is skipped if the idex refers to a child node that does not exsist
"""
def node_value(string,i):
    child = int(string[i])
    meta = int(string[i+1])
    node = 0
    if child == 0:
        for k in range(i+2, i+2+meta):
            node += int(string[k])
        del string[i:i+2+meta]
        return node
    elif child > 0:
        children = []
        j = 1
        while j <= child:
            result = node_value(string,i+2)
            children.append(result)
            j += 1
        for k in range(i + 2, i + 2 + meta):
            position = int(string[k])
            if position > len(children):
                continue
            else:
                node += children[position-1]
        del string[i:i+2+meta]
        return node
    else:
        print("Error: Number of child nodes cannot be negative")

"""
Input line is read in and split into a list (licence).
Due to how meta_sum and node_value are written, two copies are needed as the licence is deleted in the process
licence is operated on by both meta_sum and node_value, with the respective results output
"""
raw = open("day8_input.txt","r")
for line in raw:
    data = line
raw.close()
licence1 = data.split()
licence2 = data.split()
answer1 = meta_sum(licence1,0)
answer2 = node_value(licence2,0)
print("Part 1 answer: " + str(answer1))
print("Part 2 answer: " + str(answer2))
