import os
import platform
import sys


def mypcdetail():
    """PCDETAIL
    1-To Print plathform Version
    """
    print(platform.version())
    #To print machine
    print(f"Machine Name:{platform.machine()}")

    #To print Python Version
    print(platform.python_version())

    #To print Release Version of platform
    print(f"Os version:{platform.release()}")

    #To print win32 version
    print(f"The window version is:{platform.win32_ver()}")

    #To print which operating system your using
    print(f"To find which os your using:{platform.system()}")

    #working with os module
    print(f"It operating system name:{os.name}")

    #To findout what system palthform are you using
    print(sys.platform)


if __name__=="__main__":
    mypcdetail()