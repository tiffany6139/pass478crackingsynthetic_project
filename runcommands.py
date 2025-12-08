import subprocess

"""Used to run entire simulation of Attacks MD5, SHA1, and salt"""
# commands = [ "hashcat -m 0 -a 0 md5hash.hash rockyou.txt",
# "hashcat -m 0 -a 0 totalmd5hash.hash rockyou.txt",
# "hashcat -m 100 -a 0 sha1.hash rockyou.txt",
# "hashcat -m 100 -a 0 totalsha1hash.hash rockyou.txt -O",
# "hashcat -m 1400 -a 0 sha256salt.hash rockyou.txt",
# "hashcat -m 1400 -a 0 totalsha256.hash rockyou.txt -O"
# ]

"""Single command to simulate the attack"""
commands = [ "hashcat -m 0 -a 0 md5hash.hash rockyou.txt"]

for command in commands:
    useradd = input("To intialize the attackers commands press enter:")
    proces = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell = True)
    while True:
        if useradd == 'quit':
            break
        # output = proces.stdout.read().decode('utf - 8')
        output = ''.join(item.decode('utf-8') for item in proces.stdout.readlines())
        if output and (command == commands[0]):
            file = open('passguesses.txt', 'w')
            file.write(output+'\n')
        if output:
            print("hash return:", output)
            break

proces.wait()
print("Passwords Found! Run user container to gain root access!")


"""Tried to use os and try/except but didn't work"""
# try:
#     subprocess.run(['hashcat' ,'-m' ,'0' ,'-a' ,'0' ,'md5hash.hash' ,'rockyou.txt'], shell = True, capture_output = True)

# except subprocess.CalledProcessError:
#     print("error")
# os.system('sudo apt update')

# os.system('hashcat -m 100 -a 0 sha1.hash rockyou.txt')

"""Reference: https://www.digitaldesignjournal.com/python-subprocess-interactive/#:~:text=To%20achieve%20interactive%20communication%20with%20a%20subprocess%2C%20you,Python%20shell%29%20%22python%22%2C%20%23%20Command%20to%20run%20"""