import paramiko
def run(hostname:str, username:str, password:str, localFile:str, remoteFile:str, port:int):
    """Function for sending files using ssh and sftp. First of all function establish ssh connection with given credentials. After suscefully 
    connected to server with ssh, it establish sftp connection and finally send the file. After seding file function close sftp and ssh 
    connection.
    
    Parmeters:
    @param hostanme hostname or remote server
    @param username username for connecting to ssh 
    @param password password for connecting to ssh
    @param localFile direcotry of local file
    @param remoteFile director of remote file where you want to save the file
    @param port port for connecting over ssh to remote server"""

    # Soubor, který chcete odeslat
    local_file = "./Command database"
    remote_file = "/"

    # Připojení k serveru (IP B)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    # Spuštění SFTP
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)

    # Uzavření spojení
    sftp.close()
    ssh.close()


if __name__ == "__main__":
    run(hostname="hostnameOfRemoteServer", username="usernameForSsh", password="passwordForSsh", localFile="direcotryOfLocalFile", remoteFile="direcotryOfRemoteFile", port="portForSsh")
