import socket
import threading
from queue import Queue

def scanner(target, port):
    try:
        # Defining the connection
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.settimeout(1)
        conection = sckt.connect((target, port)) # actually making connection
        return True

    except socket.timeout as e: # timeout == FILTERED PORT
        print(f'\nError: {e}\nPort: {port}\nState: FILTERED.')
        return False

    except ConnectionRefusedError as e: # Connectionrefused == CLOSED
        print(f'\nErro: {e}\nPort {port}\nState: CLOSED.')
        return False

def create_queue(list_of_ports):
    for port in list_of_ports:
        queue.put(port)

def worker_queue():
    while not queue.empty(): 
        port = queue.get()
        if scanner(target, port):
            print(f'\nPort: {port}\nState: OPEN')
            print(socket.getservbyport(port))
         
def main():
    global queue
    global list_ports_open
    global target

    queue = Queue()
    list_ports_open = []
    all_threads = []

    target = input('Type here the Ip to scan: ')

    print('If you want to scan only one port type [ 1 ], else type [ 2 ]')
    answer = int(input('Type here: '))
    if answer == 1:
        port = int(input('Type the number of the port: '))
        if scanner(port):
            print(f'Port: {port}')
            print(f'State: OPEN')
        return

    elif answer == 2:
        init = int(input('Type the door to beggin the scan: '))
        final = int(input('Type the door to end the scan: '))
        all_ports = range(init, final + 1)

        speed = int(input('How many ports scan per second: '))

    else:
        print('Invalid answer.')
        return

    create_queue(all_ports)

    for i in range(speed):
        thread = threading.Thread(target=worker_queue)
        all_threads.append(thread)

    for thread in all_threads:
        thread.start()

    for thread in all_threads: # Waiting for all threads to finish
        thread.join()

    print(f'All open ports: {list_ports_open}')

if __name__ == '__main__':
    main()

