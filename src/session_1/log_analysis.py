def print_syslog():
    file = open("/var/log/syslog")

    for line in file:
        print(line)
