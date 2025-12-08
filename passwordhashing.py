import hashlib


#makes the md5 hasing of password
def md5hasing(password):
    md5hashing = hashlib.md5(password.encode())
    new = md5hashing.hexdigest()
    # file = open("md5hash.hash", 'w')
    # file.write(new)
    
    return new

#makes the sha hasing of password
def sha(password):
    shahashing = hashlib.sha1(password.encode())
    newhash = shahashing.hexdigest()
    return newhash

#uses sha256 + salting to prove security
def salting(password):
    salt = '4security78'
    newpass = password + salt
    salthashing = hashlib.sha256(newpass.encode())

    salthashings = salthashing.hexdigest()

    return salthashings

def insertTofile(filename, filename2, listofhashes):
    file = open(filename, 'w')
    file2 = open(filename2, 'w')
    for i, x in enumerate(listofhashes):
        if (37 < i < 42):
            file.write(x+'\n')
        elif (i < 60):
            file2.write(x+'\n')
        else:
            pass
    file.close()

def main():
    userpasswords = open("wordlists.txt", 'r')
    u = userpasswords.readlines()
    # print(u)
    listofmd5 = []
    listofsha = []
    listofsha256 = []
    for passwd in u:
        # print(passwd)
        news = passwd.strip(' \n')
        # print(news)
        n = md5hasing(news)
        # print(n)
        listofmd5.append(n)
        # listofmd5.append("test") e10adc3949ba59abbe56e057f20f883e
        # listofmd5.append("test")

        s = sha(news) 
        listofsha.append(s)


        s256 = salting(news)
        listofsha256.append(s256)


    # #inserts the hashes into the file (first file stores 1, second stores all, list of hashes)
    # print(listofmd5)
    insertTofile("md5hash.hash", "totalmd5hash.hash", listofmd5)
    insertTofile("sha1.hash","totalsha1hash.hash", listofsha)
    insertTofile("sha256salt.hash", "totalsha256.hash", listofsha256)

    # passwd = "123456"
    # n = md5hasing(passwd)
    # print(n)
    print("Completed")

main()