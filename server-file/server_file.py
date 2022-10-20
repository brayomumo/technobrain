import csv


def handle_file(file_path):
    '''
        Opens files and parses the data or throws exception if file not found
    '''
    data = []
    with open(file_path, 'r') as csv_file:
        filee = csv.reader(csv_file, delimiter=',')
        for row in filee:
            data.append(row)
    
    return data


def parse_logs(file_path):
    '''
        This creates dictionary of IP addresses and the count in the form
        {
            "ip_addr1": count,
            "ip_addr2": count,
            "ip_addr3": count,
        }
    '''
    data = handle_file(file_path)
 
    ip_addresses = {}
    for log in data:
        ip_addr = log[-1]

        if ip_addr in list(ip_addresses.keys()):
    
            count = ip_addresses[ip_addr]
            ip_addresses[ip_addr] = count +1
            continue

        ip_addresses[ip_addr] = 1
    
    return ip_addresses


if __name__ == '__main__':
    file_path = 'server.log'
    result = parse_logs(file_path)
    print(result)
