from random import randint

def GNA():
    print("\n--- GRAMÁTICA NO AMBIGUA ---\n")
    print(" B->(RB|e R->)|(RR")
    mod = input("\n1)MODO MANUAL 2)MODO AUTOMÁTICO \n")
    gna = open("GNA.txt", "w")

    if mod == "1":
        print("\nINGRESE LA CADENA ()")
        cadena = input() 
        print("Longitud de la cadena:", len(cadena)) 
        gna.write("\n"+"Longitud de la cadena: "+ str(len(cadena)))
        gna.write("\n"+cadena)

    else:
        print("\nMODO AUTOMÁTICO")
        gna.write("\n"+"MODO AUTOMATICO")
        cadena=""
        largo=randint(1,1000)
        for i in range(0,largo):
            rand1=randint(0,1)
            if(rand1==1):
                cadena=cadena+')'
            else:
                cadena=cadena+'('
        print("Longitud de la cadena:", len(cadena)) 
        gna.write("\n"+"Longitud de la cadena:"+str(len(cadena))) 
        print(cadena)
        gna.write("\n"+cadena)

    final = "B" 
    resultado = ""
    print("")
    gna.write("\n"+"")

    longitud = len(cadena)
    print("B")
    gna.write("\n"+"B")

    for i in range(0,longitud):
        if(final[0] == "B"):

            if (cadena[i] == "("):
                final = "R"+final
                resultado = resultado + "("
                print (resultado+final)
                gna.write("\n"+resultado+final)
                continue

            if(cadena[i] == ")"):
                print("ERROR: LA CADENA NO SIGUE LAS REGLAS DE DERIVACIÓN")
                gna.write("\n"+"ERROR: LA CADENA NO SIGUE LAS REGLAS DE DERIVACION")
                final =final+"X"
                break

        if(final[0] == "R"):

            if(cadena[i]=="("):
                final = "R"+final
                resultado = resultado +"("
                print (resultado+final)
                gna.write("\n"+resultado+final)
                continue

            if(cadena[i]==")"):
                final = final[1:len(final)]
                resultado = resultado + ")"
                print (resultado+final)
                gna.write("\n"+resultado+final)
                continue

    if(final=="B"):
        print("\n"+resultado)
        print("\nCADENA ACEPTADA")
        gna.write("\n"+"\n"+resultado)
        gna.write("\n"+"\nCADENA ACEPTADA")

    if(final!="B"):
        print("\nCADENA NO ACEPTADA")
        gna.write("\n"+"\nCADENA NO ACEPTADA")
        
while True:
    GNA()
    opcion = input("¿DESEA EJECUTAR NUEVAMENTE?(s/n): ").lower()
    if opcion != "s":
        break	