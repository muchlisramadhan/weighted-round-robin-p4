from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.enableCli()

# Network definition
net.addP4Switch('s1', cli_input='cmd.txt')
net.setP4SourceAll('weighted_round_robin.p4')

net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addHost('h5')

net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s1', 'h3')
net.addLink('s1', 'h4')
net.addLink('s1', 'h5')
net.mixed()


# Nodes general options
# net.addTaskFile('task.txt')
# net.addTask('h1', 'arp -s 10.0.1.254 00:00:00:00:01:01')
# net.addTask('h2', 'arp -s 10.0.2.254 00:00:00:00:02:02')
# net.addTask('h2', 'ip route del default')
# net.addTask('h3', 'ip route del default')
net.enablePcapDumpAll()
net.enableLogAll()

# Start the network
net.startNetwork()
