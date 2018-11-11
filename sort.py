import os
import shutil

for f in os.listdir("."):
    letter = f[-6]
    
    if(not os.path.isdir("./"+letter)):
        os.mkdir("./"+letter)
    shutil.move(f, "./"+letter)