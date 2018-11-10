import networkx as nx
import matplotlib.pyplot as plt
import json,sys
import seaborn
import datetime

def maketree(json_file):
    G = nx.DiGraph()
    G.size = {}
    G.num = {}
    #G.add_node("ROOT")
    json_data = open(json_file).read()
    data = json.loads(json_data)
    label = {}
    for node in data:
        if not G.has_node(node['id']):
            G.add_node(node['id'] )
            G.size[node['id']] = 0.002*node['info']['chars_total'] if node['info']['chars_total']>0 else 1
            G.num[node['id']] = len(node['children'])
            attributes ={node['id'] :node}
            label[node['id']] = node['id']
            nx.set_node_attributes(G, attributes)
    for node in data:
        for child in node['children']:
            if not G.has_node(child):
                G.add_node(child)
                if child not in G.num:
                    G.num[child] = 0
                G.size[child] = 1
            if not G.has_edge(node['id'], child):
                G.add_edge(child,node['id'])
    return (G,label)


def plot(filename):
    G, label = maketree(filename)

    # write dot file to use with graphviz
    # run "dot -Tpng test.dot >test.png"
    # nx.write_gexf(G,'test.gexf')

    # same layout using matplotlib with no labels
    plt.title('Shell layout of Coversation threads')
    # pos=nx.graphviz_layout(G, prog='dot')
    colors = range(len(G.edges))
    # nx.draw(G, labels = label, node_size=[1000*G.size[node] for node in G],pos = nx.spring_layout(G,k=0.6,iterations=20), edge_color=colors,node_color='#A0CBE2')
    first = []
    second = []
    third = []
    fourth = []

    for k, v in G.num.items():
        if v < 1:
            first.append(k)
        elif v >= 1 and v < 3:
            second.append(k)
        elif v >= 3 and v < 4:
            third.append(k)
        else:
            fourth.append(k)

    shells = [first,second, third, fourth]
    pos = nx.shell_layout(G, shells)
    nx.draw(G, node_size=[10 * G.size[node] for node in G], pos=nx.shell_layout(G, shells),
            node_color='#A0CBE2')
    for p in pos:
        yOffSet = 0
        xOffSet = 0
        pos[p] = (pos[p][0] + xOffSet, pos[p][1] + yOffSet)
    #plt.legend()
    plt.show()

if __name__=="__main__":
    plot('2017-5-5.json')