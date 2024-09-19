import paramiko
import os
from tqdm import tqdm

def run(hostname:str, username:str, password:str, localFolder:str, remoteFolder:str, port:int=22):
    """Function for sending folers using ssh and sftp. First the program connect to server using ssh with your credentials. After 
        program is sucefully connercted to server, program establish sft conncection a call function for prepare local foleder and
        remote folder fro sending. First of all the funkction check if the folder already exist on remote computer. If folder isn't
        exist it will create it. After checking, it gets list of all files that are in folder. Then it creates progress bar. And
        after all it sends the folder with files to remote computer.
        
        Parameters:
        @param hostname Hostname of remote server
        @param username Username to conncet to remote server
        @param password Password to connect to remote server
        @param localFile Directory of folder on local computer
        @param remoteFolder Directory where you want to save the folder on remote computer
        @param port the port of ssh on remote computer"""
    

    def upload_folder(sftp, localFolder, remoteFolder):
        """Function for preparing and sending the folder."""
        if not os.path.exists(remoteFolder):
            sftp.mkdir(remoteFolder)

        # Získání seznamu všech souborů a složek
        all_files = []
        for root, dirs, files in os.walk(localFolder):
            for file in files:
                all_files.append(os.path.join(root, file))

        # Progress bar
        with tqdm(total=len(all_files), desc="Uploading files", unit="file") as pbar:
            for local_path in all_files:
                relative_path = os.path.relpath(local_path, localFolder)
                remote_path = os.path.join(remoteFolder, relative_path)

                # Pokud je složka, vytvoříme ji
                if os.path.isdir(local_path):
                    try:
                        sftp.mkdir(remote_path)
                    except IOError:
                        pass  # Pokud složka již existuje, ignorujeme chybu
                else:
                    # Nahrání souboru
                    sftp.put(local_path, remote_path)
                
                pbar.update(1)



    # Připojení k serveru (IP B)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, port, username, password)
        sftp = ssh.open_sftp()
        try:
            upload_folder(sftp, localFolder, remoteFolder)
        finally:
            sftp.close()
    finally:
        ssh.close()



if __name__ == "__main__":
    run(hostname="yourHostname", username="your username", password="yourPassword", localFolder="directoryOfLocalFolder", remoteFolder="direcotryOfRemoteFolder", port="portOfSsh")