try:
    class Private:
        __PriVar='I\'m Private'

        def __PriMet(self):
            print('I only work inside my class')

        def showPriVar(self):
            print('Private Variable (__PriVar)\'s value: ',Private.__PriVar)


    print()
    RHVBC=Private()
    RHVBC.showPriVar()
    RHVBC.__PriMet()

except AttributeError:
    print('Sorry, but you can\'t access a private method (__PriMet) outside its class\n\n')