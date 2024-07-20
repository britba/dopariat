import struct

def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        if i+1 < len(data):
            checksum += (data[i] + (data[i+1] << 8))
    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += (checksum >> 16)
    return ~checksum & 0xffff

def create_packet(data, identifier):
    header = struct.pack('!HH', calculate_checksum(data), identifier)
    packet = header + data
    return packet
