import commands

def GetTarDevice():
    commands.getstatusoutput('ls /bin/ls')


if __name__ == '__main__':
    GetTarDevice()
