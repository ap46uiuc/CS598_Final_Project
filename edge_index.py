from pyhealth.medcode import InnerMap

def get_edge_index(graph):
    index = {}
    idx = 0
    child_edge_index = []
    parent_edge_index = []
    for code in graph.graph.nodes:
        index[code]=idx
        idx = idx+1
    for code in graph.graph.nodes:
        children = get_child(code,graph)
        for child in children:
            child_edge_index.append([index[code],index[child]])
        parents = graph.get_ancestors(code)
        for parent in parents:
            parent_edge_index.append([index[code],index[parent]])
    c_row = list(map(lambda x: x[0], child_edge_index))
    c_col = list(map(lambda x: x[1], child_edge_index))
    p_row = list(map(lambda x: x[0], parent_edge_index))
    p_col = list(map(lambda x: x[1], parent_edge_index))
    return index,[c_row,c_col],[p_row,p_col]


def get_child(code, graph):
    level = len(graph.get_ancestors(code))
    full_list_children = graph.get_descendants(code)
    direct_children = []
    for i in full_list_children:
        if len(graph.get_ancestors(i)) == level + 1:
            direct_children.append(i)
        else:
            break
    return direct_children