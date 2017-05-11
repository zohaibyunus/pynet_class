import telnetlib
import time
import socket
import sys

TELNET_PORT=23
TELNET_TIMEOUT=6

def connect(ip):
    try:    
        return telnetlib.Telnet(ip,TELNET_PORT,TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed Out")

def login(remote_conn,user,passwd):
    credential = remote_conn.read_until("username:" , TELNET_TIMEOUT)
    remote_conn.write(user+'\n')
    credential+= remote_conn.read_until("password:" , TELNET_TIMEOUT)
    remote_conn.write(passwd+'\n')
    time.sleep(1)
    return credential

def send_command(remote_conn,cmd):
    cmd = cmd.rstrip()
    return remote_conn.write(cmd+'\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    ip="184.105.247.70"
    user="pyclass"
    password="88newclass"
    
    remote_conn = connect(ip)
    time.sleep(1)
    login(remote_conn,user,password)
    output = send_command(remote_conn,'terminal length 0')
    output = send_command(remote_conn,'show ip interface brief')
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()
