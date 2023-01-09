services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}

print(services.keys())

print(services.items())

print('ftp' in services)

print(services['ftp'])

print("{<'+'>} Found vuln with FTP on port " + str(services['ftp']))

for key in services.keys():
    print(key)
