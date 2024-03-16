from scapy.all import sniff, IP, UDP, TCP
from collections import defaultdict
import time
import socket
import matplotlib.pyplot as plt

# Dictionary to store packet count for each domain and protocol
# packet_count = defaultdict(lambda: {'TCP': 0, 'UDP': 0})
packet_count = defaultdict(int)
whois = defaultdict(str)
perfGraph = []
plt.ion()

# Function to calculate and display bandwidth per domain
def calculate_bandwidth(pkt):
    global packet_count
    global perfGraph

    minuteSum = 0
    if IP in pkt:
        ipaddr = pkt[IP].dst ### .split('.')[0]  # Extract the domain
        ln = len(pkt)
        minuteSum += ln
        if TCP in pkt:
            # packet_count[domain]['TCP'] += ln
            packet_count[ipaddr] += ln
        elif UDP in pkt:
            packet_count[ipaddr]['UDP'] += ln

    # Update bandwidth every minute
    if time.time() - calculate_bandwidth.last_time >= 60:
        perfGraph.append(minuteSum)
        for ipaddr in packet_count.keys():
            total_bytes = packet_count[ipaddr]
            # total_bytes = counts['TCP'] + counts['UDP']
            bandwidth_MBps = total_bytes / (1024 * 1024)  # Convert to megabytes
            print(f"Domain: {ipaddr}, Bandwidth: {bandwidth_MBps:.2f} MB/s")
            # Reset counts for the domain
            # packet_count[domain] = {'TCP': 0, 'UDP': 0}
        
        calculate_bandwidth.last_time = time.time()
        plot_graph(packet_count)  # Plot the graph

# Initialize last_time
calculate_bandwidth.last_time = time.time()

# Function to plot a monthly graph
def plot_graph(data):
    global perfGraph

    plt.close()
    plt.figure(figsize=(10, 6))
    plt.ion()

    domains = []
    bandwidths = []
    # for domain, counts in data.items():
    #     total_bytes = counts['TCP'] + counts['UDP']
    #     bandwidth_MBps = total_bytes / 1 #(1024 * 1024)  # Convert to megabytes
    #     domains.append(domain)
    #     bandwidths.append(bandwidth_MBps)
    
    for ipaddr in data.keys():
        total_bytes = data[ipaddr]
        data[ipaddr] = 0
        bandwidth_MBps = total_bytes / (1024 * 1024)  # Convert to megabytes

        domain = whois.get(ipaddr,'####')
        if(domain == '####'):
            domain = ipaddr
            try:
                domain = socket.gethostbyaddr(ipaddr)[0]
            except socket.herror:
                remote_host = "Unknown"
            whois[ipaddr] = domain

        domains.append(domain)
        bandwidths.append(bandwidth_MBps)
    
    plt.bar(domains, bandwidths, color='skyblue')
    plt.xlabel('Domain')
    plt.ylabel('Bandwidth (MB/s)')
    plt.title('Minutely Bandwidth Usage per Domain')
    plt.xticks(rotation=90)
    plt.tight_layout()
    #########  plt.savefig('monthly_bandwidth.png')  # Save the plot as an image
    plt.show()
    plt.pause(10)

    plt.close()
    plt.figure(figsize=(10, 6))
    plt.ion()
    plt.plot(perfGraph)
    plt.show()
    plt.pause(10)


# Sniff packets and call calculate_bandwidth function
sniff(prn=calculate_bandwidth, store=0, filter="tcp")