import json

with open('sinfo.json') as json_file:
    data = json.load(json_file)
print(type(data))

for nodes in data['nodes']:
    print('Node', nodes['name'], 'has', nodes['cpus']-nodes['alloc_cpus'], 'cpus free, \n approximately', \
            nodes['real_memory']-nodes['alloc_memory'], 'MB memory available out of a total of', nodes['real_memory'], 'MB\n', \
            nodes['gres'], 'with', nodes['gres_used'], 'currently used GPUs \n')
 
#    if nodes['alloc_memory']/nodes['real_memory'] >=.8:
#        print(nodes['name'], 'mem more than 80% used at', nodes['alloc_memory']/nodes['real_memory'] )
#        consumed = 'mem'
#    elif nodes['alloc_cpus']/nodes['cpus'] >=.8:
#        print(nodes['name'], 'cpus more than 80% with', nodes['cpus']-nodes['alloc_cpus'], 'remaining')
#
