import paramiko
import time

def new_connection(ip,user,passwd,port):
    remote_conn_pre = paramiko.SSHClient()

    ## Ignore host keys
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip,username=user,password=passwd,port=port,look_for_keys=False,allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    return remote_conn

def disable_paging(remote_conn,cmd='terminal length 0'):

	remote_conn.send(cmd+'\n')
	time.sleep(1)

def send_command(remote_conn,cmd):

    remote_conn.send(cmd+"\n")
    time.sleep(1)
    if remote_conn.recv_ready():
    	output = remote_conn.recv(5000)
    else:
	output = ''

    print output

def main():

    ip = '184.105.247.71'
    user = 'pyclass'
    passwd = '88newclass'
    port = 22
    cmd = 'show version'
    conn = new_connection(ip,user,passwd,port)
    disable_paging(conn)
    send_command(conn,cmd)

if __name__ == '__main__':
    main()


