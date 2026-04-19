class reverse():
    def __init__(self,s=""):
        self.s=s

    def stringreverse(self):
        print('The reversed string is: ',self.s[::-1])


string=input('Please enter a string you would like to reverse: ')
strin=reverse(string)

strin.stringreverse()