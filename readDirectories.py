import os, time
from datetime import datetime
    


class directory:
    def crLstUvz(self, dir):
        vz = os.listdir(dir) #enthält alle Unterverzeichnisse
        print(vz)
        for el in vz:
            uvz = dir + "\\" + el # Baut den Pfad des Unterverzeichnisses zusammen
            #print(x)
            files=os.listdir(uvz) # erstellt eine Liste aus den Filenamen
            cnt=0
            for file in files:
                #print(file)
                unixTimeStamp = os.path.getmtime(uvz + "\\" + file)
                zeitStempel = datetime.fromtimestamp(unixTimeStamp)
                #print(zeitStempel)
                heute = datetime.now().year + datetime.now().month + datetime.now().day
                zeitFile = zeitStempel.year + zeitStempel.month + zeitStempel.day
                #print(heute)
                #print(zeitFile)
                if (heute - 5) > zeitFile:
                    x = uvz + "\\" + file
                    print("Das file kann weg : " + x)
                else:
                    continue
                    


work = directory();
work.crLstUvz("x:\\BO_Berichte")


