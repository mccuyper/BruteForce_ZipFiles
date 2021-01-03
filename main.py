from zipfile import ZipFile
from os import mkdir


def generator(string):
    for word in string:
        passwd = word.replace('\n', '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield "[FALSE]: " + passwd
        else:
            yield "\n\n[TRUE]: " + passwd
            return


directory = "ExtractedAfterCrack"
try:
    mkdir(directory)
except FileExistsError:
    pass

with open(input("Dictionary to use: "), errors='ignore') as dictionary:
    with ZipFile(input("Archive to Hack: ")) as archive:
        for password in generator(dictionary):
            print(password)
print("---------------END-----------------")
