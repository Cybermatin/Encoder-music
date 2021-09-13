#cyber-matin

from eyed3 import load
from stepic import encode
from PIL import Image
from colorama import Fore,init
import colorama
import time

time.sleep(1)
print(colorama.Fore.RED+"""

                     ████╗      ████╗    ██████╗     ████╗   ██╗
                       █████   █████╔╝      ██╔═╝     ██╔██╗  ██║
                       ██╔╝█████╝ ██║       ██║       ██║ ██╗ ██║
                       ██║  ███╝  ██║       ██║       ██║  ██╗██║
                       ██║   █╝   ██║  ██╗  ██║  ██╗  ██║   ████║
                       ╚═╝        ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝   ╚═══
""")

colorama.init() ## initialize the colorama

class colorma:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print(f"""{colorma.CYAN}
    ╔══[Coded by : C Security,{colorma.RED}[Encoder music]{colorma.CYAN}]
    ║
    ╠═Author of tools : MatiN
    ╠═Team name : dark_shell
    ║
    ╠═(~BYE)
    """)
    

init()
data = input(Fore.YELLOW+"::::ENTER YOUR DATA:::: ")

audio = input(Fore.GREEN+"::::Audio:::: ")
img_name = input(Fore.GREEN+"::::Image:::: ")
audio = load(audio) # Opening the audio file

img = Image.open(img_name)
img_steg = encode(img , data.encode()) # Encode data into Image
img_steg.save(img_name) # save encoded image

audio.initTag()
audio.tag.images.set(3 , open(img_name,"rb").read() , "image/png") # set cover to audio file
audio.tag.save() # save changes in audio file

print("ok") # The END :)
input()
