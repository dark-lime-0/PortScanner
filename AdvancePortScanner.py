import socket
import optparse
from threading import Thread

l='''
            _       _                                       
           / \   __| |_   ____ _ _ __   ___ ___             
          / _ \ / _` \ \ / / _` | '_ \ / __/ _ \            
         / ___ \ (_| |\ V / (_| | | | | (_|  __/            
 ____   /_/   \_\__,_|_\_/ \__,_|_| |_|\___\___|            
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ___ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__| 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | |  __/ |    
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_|\___|_|    
v0.0.1 by Youssef | dark-lime-0
'''
print(l)

def portScanner(host, port):        # check if the port status
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        print(f"[+] Port {port} on {host} is open")
    except (socket.timeout, socket.error):
        # print(f"[-] Port {port} on {host} is closed")
        pass
    finally:
        sock.close()

def scanPorts(targetHost, targetPorts):    # scan multiple ports simultaneously to improving the overall performance.
    for port in targetPorts:
        Thread(target=portScanner, args=(targetHost, port)).start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
    parser.add_option('-p', dest='targetPorts', type='string', help='specify target ports range (e.g. 20-100)')
    (options, args) = parser.parse_args()

    targetHost = options.targetHost
    targetPorts = options.targetPorts

    if not (targetHost and targetPorts):
        print(parser.usage)
        exit(0)

    try:                                                    # parse port range
        start, end = map(int, targetPorts.split('-'))
        targetPorts = range(start, end + 1)                 # specifying port range
    except ValueError:
        print("Invalid port range format, Use format like '20-100' ")
        exit(0)

    scanPorts(targetHost, targetPorts)                      # scan specified host & port

if __name__ == "__main__":
    main()


