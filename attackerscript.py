import subprocess

commands = ["sudo apt update"]

#"jennifer", "hunter", "zxcvbnm", "asdfgh"]
userpassword_attempts = []
for x in range(4):
    user_passwords_hashmap = input("Enter the passwords cracked previously:")
    userpassword_attempts.append(user_passwords_hashmap)

for command in commands:
    useradd = input("To intialize the attackers commands press enter:")
    print("Shell Commands: $", command, "Attempt: ", userpassword_attempts)
    proces = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell = True)
    while True:
        if useradd == 'quit':
            break
        
        # output = proces.stdout.read().decode('utf - 8')
        output = ''.join(item.decode('utf-8') for item in proces.stdout.readlines())
        if output:
            print("return:", output)
            break
#unable to do automatic brute-force because sudo protects against that

proces.wait()
print("Success!")