import os


## Importante activar para no usar el programa de forma estática
menuActivado = False;




def soloBuscar(ruta, recursivo, caseSensitive, buscar, reemplazar):
    if os.path.isdir(ruta):
        for root, dirs, file in os.walk(ruta):
            root = str(root).replace("\\", "/")+"/"
            for f in file:
                if (caseSensitive and str(f).__contains__(buscar)) or (not caseSensitive and str(f).lower().__contains__(buscar.lower())):
                    print(root+f + " -> "+root+str(f).replace(buscar, reemplazar));
            for d in dirs:
                if (caseSensitive and str(d).__contains__(buscar)) or (not caseSensitive and str(d).lower().__contains__(buscar.lower())):
                    print(root+d + " -> "+root+str(d).replace(buscar, reemplazar));
    else:
        print("El directorio introducido no existe");



def reemplazar(ruta, recursivo, caseSensitive, buscar, reemplazar):
    if os.path.isdir(ruta):
        while True:
            smthfound = False;
            for root, dirs, file in os.walk(ruta):
                root = str(root).replace("\\", "/")+"/"
                for f in file:
                    if (caseSensitive and str(f).__contains__(buscar)) or (not caseSensitive and str(f).lower().__contains__(buscar.lower())):
                        try:
                            smthfound = True;
                            os.rename(root+f, root+str(f).replace(buscar, reemplazar));
                            print(root+f + " -> "+root+str(f).replace(buscar, reemplazar));
                        except Exception as e:
                            print("No se puede reemplazar "+root+f);
                            print(e);
                        break;
                for d in dirs:
                    if (caseSensitive and str(d).__contains__(buscar)) or (not caseSensitive and str(d).lower().__contains__(buscar.lower())):
                        try:
                            smthfound = True;
                            os.rename(root+d, root+str(d).replace(buscar, reemplazar));
                            print(root+d + " -> "+root+str(d).replace(buscar, reemplazar));
                        except Exception as e:
                            print("No se puede reemplazar "+root+d);
                            print(e);
                        break;
                if smthfound:
                    break;
            if not smthfound:
                break;
    else:
        print("El directorio introducido no existe");



while True and menuActivado:
    ##Opciones
    recursivo = False;
    caseSensitive = False;
    ##Opciones

    print("Introduce la ruta al directorio");
    ruta = input(": ").replace("\\", "/");

    print("Pulsa intro para utilizar de forma recursiva (Introduce x para desactivarlo). Si existen carpetas en la ruta introducida, el programa se meterá dentro de ellas para buscar");
    recursivoTXT = input(": ");
    if recursivoTXT.lower() == "":
        recursivo = True;

    print("Pulsa intro para que coincidan las mayúsculas y minúsculas en la búsqueda (Introduce x para desactivarlo)");
    caseSensitiveTXT = input(": ");
    if caseSensitiveTXT.lower() == "":
        caseSensitive = True;


    print("Introduce el texto a buscar");
    buscar = input(":");

    print("Introduce el texto a reemplazar");
    reemplazar = input(": ");
    recursivoTXT = "No";
    if recursivo:
        recursivoTXT = "Sí";

    caseSensitiveTXT = "No";
    if caseSensitive:
        caseSensitiveTXT = "Sí";
    
    print("""
    Ruta: """+ruta+"""
    Recursivo: """+recursivoTXT+"""
    Sensible a mayúsculas y minúsculas: """+caseSensitiveTXT+"""
    Texto a buscar: """+buscar+"""
    Texto a reemplazar: """+reemplazar+"""
    """);
    print("Pulsa intro para empezar a reemplazar (Introduce x para volver a comenzar) ");
    comenzar = input(": ");
    if comenzar == "":
        print("Comienza");
        break;
    else:
        continue;


reemplazar("E:/Servidores/GarrysMod Helix/garrysmod", True, True, "hpwrewrite", "cpowers");
# reemplazar("E:/Servidores/GarrysMod Helix/garrysmod", True, True, "spells", "powers");
# reemplazar("E:/Servidores/GarrysMod Helix/garrysmod", True, True, "Spell", "Power");
# reemplazar("E:/Servidores/GarrysMod Helix/garrysmod", True, True, "spell", "power");