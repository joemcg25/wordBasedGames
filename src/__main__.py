#TODO Make this package downloable from linux + python import
#TODO Look into if generator functions can enhance any performance here
import os
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()
from arcadeApplication import arcade
if __name__ == '__main__':
    print(f"Welcome to the games zone")
    arcade.arcadeLogic()