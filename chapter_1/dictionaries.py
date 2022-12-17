services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
services.keys(['ftp', 'smtp', 'ssh', 'http'])
services.items([('ftp', 21), ('smtp', 25), ('ssh', 22), ('http', 80)])
services.has_key('ftp')
True
services['ftp']
21
print("{<'+'>} Found vuln with FTP on port" + str(services['ftp']))
