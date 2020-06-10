parent_types = []
child_types = []
graph = {}
visited = []
cycle = False

def isChild(c_type):
    if (c_type in child_types):
        return True
    else:
        return False

def isParent(p_type):
    if (p_type in parent_types):
        return True
    else:
        return False

def read_command():
    inp = open('input.txt')

    command = inp.readline()
    par_types = command[command.index('(')+1:command.index(')'):1]
    for p_type in par_types.split(','):
        tip = p_type[p_type.index('t'):]
        if (not isParent(tip)):
            parent_types.append(tip)
    
    com_str = inp.readline()
    while (com_str != 'end' and com_str !='end\n'):
        ch_type = com_str[com_str.index('type ')+5:len(com_str)-1:]
        if (not isChild(ch_type)):
            child_types.append(ch_type)
        com_str = inp.readline()
    
    inp.close()
    
def graph_of_creation():
    list_sm=''
    for p_type in parent_types:
        graph.update({p_type:child_types})
    for ch_type in child_types:
        if (not isParent(ch_type)):
            graph.update({ch_type:[]})
    for i in graph.keys():
        list_sm+= i+': '
        for j in graph.get(i):
            list_sm+= j+' '
        list_sm += '\n'
    out.write(list_sm)

   
def dfs(v):
    visited.append(v)
    for t in graph.get(v):
        if (not t in visited):
            dfs(t)
        else:
            return True
    return False
    
def acyclic_graph():
    global cycle
    for i in graph.keys():
        visited.clear()
        cycle += dfs(i)
    if (cycle):
        out.write('Have a cycle\n')
    else:
        out.write('No cycle\n')


read_command()
out = open('output.txt','w')
graph_of_creation()
acyclic_graph()
out.close()

    
