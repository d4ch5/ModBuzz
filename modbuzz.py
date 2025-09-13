import sys
import time
from pyModbusTCP.client import ModbusClient

def print_start_screen():
    banner = r"""
 ███▄ ▄███▓ ▒█████  ▓█████▄  ▄▄▄▄    █    ██ ▒███████▒▒███████▒
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▀ ██▌▓█████▄  ██  ▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░
▓██    ▓██░▒██░  ██▒░██   █▌▒██▒ ▄██▓██  ▒██░░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ 
▒██    ▒██ ▒██   ██░░▓█▄   ▌▒██░█▀  ▓▓█  ░██░  ▄▀▒   ░  ▄▀▒   ░
▒██▒   ░██▒░ ████▓▒░░▒████▓ ░▓█  ▀█▓▒▒█████▓ ▒███████▒▒███████▒
░ ▒░   ░  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░▒▓███▀▒░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒
░  ░      ░  ░ ▒ ▒░  ░ ▒  ▒ ▒░▒   ░ ░░▒░ ░ ░ ░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒
░      ░   ░ ░ ░ ▒   ░ ░  ░  ░    ░  ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ░ ░
       ░       ░ ░     ░     ░         ░       ░ ░      ░ ░    
                     ░            ░          ░        ░        
    """
    return banner

def show_menu():
    print(print_start_screen())
    print("\n ModBuzz")
    print('1. Read Register from Target')
    print('2. Write 0 to register')
    print('3. Write 1 to register')
    
def read_register(ip):
            count_reg = int(input("Enter register-count: "))
            counter = int(input("Count of register read: "))
            print("[+] Connected to target")
            for i in range(1, counter):
                client = ModbusClient(host=ip, port=502)
                r = client.read_holding_registers(1, count_reg)
                if r:
                    print(f"Registers: {r}")
                else:
                    print("Failed to read register.")
                time.sleep(1)

def write_register_zero(ip):
            client = ModbusClient(host=ip, port=502, auto_open=True)    
            count_num = int(input("Enter register you want to write 0: "))
            count_write = int(input("Enter amount of write procedures: "))
            print("[+] Connected to target")
            for i in range(1, count_write):
                w = client.write_single_register(count_num, 0)
                if w:
                    print(f'Writing 0 to register {count_num}...')
                else:
                    print(f'Failed to write 0 to register {count_num}...')            
                time.sleep(1)

def write_register_one(ip):
            client = ModbusClient(host=ip, port=502, auto_open=True)    
            count_num = int(input("Enter register you want to write 1: "))
            count_write = int(input("Enter amount of write procedures: "))
            print("[+] Connected to target")
            for i in range(1, count_write):
                w = client.write_single_register(count_num, 1)
                if w:
                    print(f'Writing 1 to register {count_num}...')
                else:
                    print(f'Failed to write 0 to register {count_num}...')            
                time.sleep(1)

if __name__ == "__main__":
    try:
        ip = sys.argv[1].strip()
    except IndexError:
        print(f'[-] Example: python3 {sys.argv[0]} 192.168.2.1')
        sys.exit(-1)

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            read_register(ip)
        
        if choice == "2":
             write_register_zero(ip)
        
        if choice == "3":
             write_register_one(ip)

