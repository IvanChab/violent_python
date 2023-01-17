def check_vulns(banner):
    f = open("vuln_banners.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("{+} Serveris vulnerable: " + banner.strip('\n'))
