import os


## Importante activar para no usar el programa de forma estática
menuActivado = False;




def soloBuscar(ruta, caseSensitive, buscar, reemplazar):
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



def reemplazar(ruta, caseSensitive, buscar, reemplazar):
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
                            print("[v] "+root+f + " -> "+root+str(f).replace(buscar, reemplazar));
                        except Exception as e:
                            print("[x] No se puede reemplazar "+root+f);
                            print(e);
                        break;
                for d in dirs:
                    if (caseSensitive and str(d).__contains__(buscar)) or (not caseSensitive and str(d).lower().__contains__(buscar.lower())):
                        try:
                            smthfound = True;
                            os.rename(root+d, root+str(d).replace(buscar, reemplazar));
                            print("[v] "+root+d + " -> "+root+str(d).replace(buscar, reemplazar));
                        except Exception as e:
                            print("[x] No se puede reemplazar "+root+d);
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
    caseSensitive = False;
    ##Opciones

    print("Introduce la ruta al directorio");
    ruta = input(": ").replace("\\", "/");



    print("Pulsa intro para que coincidan las mayúsculas y minúsculas en la búsqueda (Introduce x para desactivarlo)");
    caseSensitiveTXT = input(": ");
    if caseSensitiveTXT.lower() == "":
        caseSensitive = True;


    print("Introduce el texto a buscar");
    buscar = input(":");

    print("Introduce el texto a reemplazar");
    reemplazar = input(": ");

    caseSensitiveTXT = "No";
    if caseSensitive:
        caseSensitiveTXT = "Sí";
    
    print("""
    Ruta: """+ruta+"""
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



########################          ########################
########################          ########################
######################## Ejemplos ########################
########################          ########################
########################          ########################


#reemplazar("C:/testDir", True, "file", "archivo");
#soloBuscar("C:/Windows", True, ".jar", ".zip")

