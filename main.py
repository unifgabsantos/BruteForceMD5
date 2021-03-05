from hashlib import md5
from os import system
def Crypt(string):
  return (md5(string.encode())).hexdigest()
def Decrypt(stringHash,wordList):
  count=0
  for line in wordList:
    count+=1
    system('clear')
    print("Count: %d"%count)
    if Crypt(line) == stringHash:
      print("String:",line)
      return True
  print("Hash: %s\nString: 404 - Not Found "%stringHash)
file=open("WordList.txt","r")
wordList=[]
for line in file.readlines(): wordList.append(line.strip())
file.close()
Decrypt(input("Crypt: "),wordList)