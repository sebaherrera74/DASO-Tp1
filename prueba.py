import csv
import time
import json

class Csv:
    def __init__(self,file_csv):
        self.set_csv_name(file_csv)
    
    def set_csv_name(self,file_csv):
        self.__csv_name=file_csv
    
    def get_csv_name(self):
        return self.__csv_name

    def leer_csv(self):
        lista=[]
        with open(self.get_csv_name(),newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                elemento={"id":row[0],"nombre":row[1],"value1":(row[2]),"value2":row[3]}
                #print(elemento)
                lista.append(elemento)
                
            #print(lista)
            lista.pop(0) #elimino el primer elemento de la lista 
            print(lista)
            

            #jsonData = json.dumps(lista)
            #print(jsonData)
           

        

class Main:
    def __init__(self,file_name):
        self.set_file_name(file_name)
    
    def set_file_name(self,file_name):
        self.__file_name=file_name
    
    def get_file_name(self):
        return self.__file_name
    
    def main(self):
        with open (self.get_file_name(),"r",encoding="utf-8") as f:
            texto=f.read()
        return texto.strip() #Saco espacios en blanco del archivo, solo mando el .csv


      

m = Main("config.txt")
prueba=m.main()
print(prueba)

c=Csv(prueba)
print(type(c))
Csv.leer_csv(c)