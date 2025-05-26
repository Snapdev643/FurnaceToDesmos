from filetools import FileTools as ft
from misc import Misc as msc
from settings import Settings as st
from compiler import Compiler as c
from parser import Parser as pr

misc_instance = msc()
cleanup = misc_instance.cleanup
cleanup(False)
settings_instance = st()
compiler_instance = c()
parser_instance = pr()



if ft.get_line(1) == "# Furnace Text Export":
    print("File check successful...")
elif ft.get_line(1) == "":
    print("File is empty or first line missing!")
else:
    print("Not a Furnace file or something went wrong! Try exporting your file again and make sure it's named correctly! (io/input.txt)")




#get pattern length
print(f"Pattern length is {int(ft.find("pattern length")[18:])}")

cleanup(False)
parser_instance.removeMetadata()
compiler_instance.addHardcodedVals()
compiler_instance.createFolders()
cleanup(True)
print("Done! Check io/output.txt for your converted file!")
input("Press enter to exit...")
quit()