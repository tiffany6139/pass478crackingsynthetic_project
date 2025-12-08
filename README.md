Project made by Tiffany Garcia

Project Idea:
Goal is to demonstrate how password cracking is an issue today since constant data breaches leave us at risk. I will also add some mitigations and how to monitor the traffic from attempts trying to login.

Setup:
The project setup is not yet completed. I still need to add the hashcat software, password list data, and other files I might need to simulate my attack using the 2 containers I have built.

User1: Victim to data breach and password hash has been compromised.
Attacker: Has most commonly used passwords list and hash of user1. Will attempt to use that information to gain root access in the container.

Security Solution is to add monitoring and possible limit the attempts of login attempts.

Used smaller library to access wordslist of 1000.

Added an IP address to both containers to be able to monitor the traffic on the network

In the python file I will get a random password hash to be used to allow for the experiment.

Modify the password in the user container to have the correct password that is generated in the ptyhon script

#Final Commands to complete the Project
#Before the running any docker commands- I ran my python file to generate everything that needs to be written into the .hash files!
#First build the docker containers, networks, etc.

    docker compose build 
    docker compose up -d

#Run the attacker container to complete the hashcat brute force and within this terminal run all these commands. This has an interactive shell so commands need to be followed.

    docker exec -it UbuntuAttacker bash
    $ python runcommands.py

#Run the user in Separate terminal (there was no way to run tcpdump without sudo, this is a flaw in my system, password has been set to 'hunter')

    docker exec -it UbuntuUser1 bash
    $sudo tcpdump -v -w newpath.pcap

#In a separate terminal run the follwoing commands and follow interactive shell

    docker exec -it UbuntuUser1 bash
    $python attackerscript.py

#Go back to first user terminal to view all the logs


"""Testing Commands"""

#The following commands are used to be ran in a single bash
Commands to run currently:
docker compose build
docker compose up -d

#Used to get into user container
docker exec -it UbuntuUser1 bash

#By using the following commands you can enter the attacker bash and perform each hashcat command
#Used to get into the attacker container
docker exec -it UbuntuAttacker bash

#command to be used in attacker to fin the password
hashcat -m 0 -a 0 md5hash.hash rockyou.txt
hashcat -m 0 -a 0 totalmd5hash.hash rockyou.txt

#command to do the sha1 will do 1 at a time
hashcat -m 100 -a 0 sha1.hash rockyou.txt
hashcat -m 100 -a 0 totalsha1hash.hash rockyou.txt -O

#command to do the sha256+modified salt will do 1 at a time
hashcat -m 1400 -a 0 sha256salt.hash rockyou.txt
hashcat -m 1400 -a 0 totalsha256.hash rockyou.txt -O

#The following commands build the container images and then using that image create a new container to view interactive shell

docker compose build
docker-compose run --rm attacker

#This command is to view if the commands recieved from the attackers cracking work
docker-compose run --rm user1

#Docker tcpdump
sudo tcpdump -w newpath.pcap

#other terminal
python attackerscript.py


