port_list = [21, 80, 443, 25]
print(port_list)

port_list.sort()
print(port_list)

pos = port_list.index(80)
print("{<'+'>} There are " + str(pos) + " ports to scan before 80.")

port_list.remove(25)
print(port_list)

cnt = len(port_list)
print("{<'+'>} Scanning " + str(cnt) + " Total Ports.")
