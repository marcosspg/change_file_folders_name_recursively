import os
def listar(ruta):
    if os.path.isdir(ruta):
        for root, _, file in os.walk(ruta):
            root = str(root).replace("\\", "/")+"/"
            for f in file:
                print(str(root+f).replace("E:/servidores/GarrysMod Helix/garrysmod/addons/custompowers/", ""));
            
    else:
        print("El directorio introducido no existe");


listar("E:/servidores/GarrysMod Helix/garrysmod/addons/custompowers/particles");