Share-it file transfer using socket functionality

Commands to setup:

sudo apt-get install nmap 
sudo apt install python-pip
pip install python-nmap

Can skip the nmap installation and manually add the ip address of server in the code

Commands for quick run

python server.py &
python client.py
pkill -f server.py



To Do:
1) Change functionality from message sharing to file sharing
2) Ensure scalability using memory mapped files
3) Find similar applications and their draw-backs(github issues)
4) Design an user interface
5) Multiple users file sharing
6) Scan nearby devices that are ready to receive


