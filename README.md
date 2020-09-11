# network-simulation
- It is a simple network simulation environment written in python.And it's the assignment of my course "Computer Communication Network (H)".  
- **The idea of this project is proposed by my teacher Mao Yuming and the core code is also programed by him.** I just did some simple work.
- You can use Pycharm to open it with python 3.8.
## project structure  
*The files of floder channel and core are coded by my teacher,the others are coded by myself.*  
- .idea  
- channel
    - There are two kinds of communication channel:bus and link
- core  
- device  
    - host,switch and router. Every device is composed of multiple modules.Switches are divided into two types, VLAN enabled and non VLAN enabled.
- module  
    - *I design most modules based on OSI.*  
    - alohaApp is specially designed for aloha simulation.
- workspace
    -Experiments and network topology.
