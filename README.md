#Files and folders sender

Programs for sending files or folders

## Sending files

Program for sending files is 'fileSender.py'. First of all program log in to server using ssh and given credentials. After sucefully logined in to srever using ssh, program establish sftp conncection. After sucefully establish sftp connection program send file given by you in 'localFile' to server. On srever it saves the file on remote server by 'remoteFile'. You can changed ssh port using 'port' parameter, defult is 22 as normal

### Steup

First of all clone repository to your computer, open 'fileSender.py' and fill in the credentials at th bottom of program. You mabye must 
change name of the program, becaouse of the 'if __name__ == "__main__:', or you can modify the program. And you must to install all libraries.

## Sending Folders

Function for sending folers using ssh and sftp. First the program connect to server using ssh with your credentials. After 
program is sucefully connercted to server, program establish sft conncection a call function for prepare local foleder and
remote folder fro sending. First of all the funkction check if the folder already exist on remote computer. If folder isn't
exist it will create it. After checking, it gets list of all files that are in folder. Then it creates progress bar. And
after all it sends the folder with files to remote computer.

### Setup

First of all you must to clone the repository to you computer and open sendFolders.py and fill in the credentials at the bottoom of page.  You mabye must to change name
 of the program, becaouse of the 'if __name__ == "__main__:', or you can modify the program. And you must to install all libraries.

