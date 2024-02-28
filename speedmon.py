from scapy.all import sniff, TCP, UDP
import time

# Dictionary to store packet count for each protocol
packet_count = {'TCP': 0, 'UDP': 0}

# Function to calculate and display traffic speed
def calculate_speed(pkt):
    global packet_count
    if TCP in pkt:
        packet_count['TCP'] += 1
    elif UDP in pkt:
        packet_count['UDP'] += 1

    # Update speed every 5 seconds
    if time.time() - calculate_speed.last_time >= 5:
        print("TCP Speed: {} packets/s".format(packet_count['TCP'] / 5))
        print("UDP Speed: {} packets/s".format(packet_count['UDP'] / 5))
        packet_count = {'TCP': 0, 'UDP': 0}
        calculate_speed.last_time = time.time()

# Initialize last_time
calculate_speed.last_time = time.time()

# Sniff packets and call calculate_speed function
sniff(prn=calculate_speed, store=0, filter="tcp or udp")