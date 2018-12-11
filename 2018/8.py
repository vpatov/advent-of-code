from queue import Queue

with open('8.in') as f:
    nums = [int(i) for i in f.read().split() if len(i.strip()) > 0]

class Node():
    def __init__(self):
        self.children = []
        self.metadata = []

def read_stream(stream,i):

    node = Node()
    children = []
    nchildren = stream[i]
    nmetadata = stream[i+1]
    index = i + 2
    for i in range(nchildren):
        index,child = read_stream(stream,index)
        children.append(child)

    node.children = children
    for i in range(nmetadata):
        node.metadata.append(stream[index])
        index += 1


    return index,node


length, root = read_stream(nums,0)

    
# Part I

def sum_nodes(node):
    sum_metadata = sum(node.metadata)
    queue = Queue()
    for child in node.children:
        queue.put(child)

    while (not queue.empty()):
        cur = queue.get()
        for child in cur.children:
            queue.put(child)
        sum_metadata += sum(cur.metadata)

    return sum_metadata



print(sum_nodes(root))


# Part I
def get_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        value = 0
        for entry in node.metadata:
            try:
                child = node.children[entry-1]
                value += get_value(child)
            except:
                continue
        return value


print(get_value(root))
