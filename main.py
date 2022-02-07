import os
import platform

os = platform.system()

if os == "Windows":
    path = "C:\\Program Files\\"
elif os == "Darwin":
    path = "/Applications/"
elif os == "Linux":
    path = "/"
else:
    print("Unsupported OS :(")
    input("Press enter to exit...")
    exit()

#En el caso de Windows pondría chocolatey y en el de macOS homebrew, en linux si no me equivoco con apt-get debería bastar
#Por otro lado git debería de ser una dependencia obligatoria
#NOTE: Revisar que con según que comandos, no se necesiten otras dependencias.
def installDependencies():
    if platform.system == "Darwin":
        os.system("clear")
        os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system('brew install git')
    elif platform.system == "Windows":
        os.system("cls")
    elif platform.system == "Linux":
        os.system("clear")
    else:
        print("Unsupported OS :(")
        input("Press enter to exit...")
        exit()

#NOTE: En esta función básicamente lo que quiero hacer es crear toda la estructura de archivos necesarios.
#NOTE: Probablemente podría añadir que seleccionase los programas de los que quiere hacer backup para crear las estructuras.
#TODO: Acabar de rellenar bien todos los comandos que quedan.
def init(platform, path):
    print("Initializing EasyDots...")
    print("We've detected the following platform: " + platform)
    print("Creating path...")

    if platform == "Windows":
        os.system("mkdir " + path + "EasyDots")
        os.chdir(path + "EasyDots")
    elif os == "Darwin":
        print("Darwin")
        os.system
