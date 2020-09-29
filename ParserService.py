import csv
import json
import os
import socket
import sys
import time
import traceback
import signal  

#Cliente UDP 

#Clase para acceder a archivo .csv y armar la lista para enviarla por el socket 
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
                elemento={"id":row[0],"name":row[1],"value1":(row[2]),"value2":row[3]}
                #print(elemento)
                lista.append(elemento)
                #print(lista)
            lista.pop(0) #elimino el primer elemento de la lista 
            #print(lista)
            return json.dumps(lista) #retorna la lista ya convertida en string
            



class Main:
    def __init__(self,file_name):
        self.set_file_name(file_name)
    
    def set_file_name(self,file_name):
        self.__file_name=file_name

    def get_file_name(self):
        return self.__file_name

    def get_file_csv(self):
        with open (self.get_file_name(),"r",encoding="utf-8") as f:
            texto=f.read()
        return texto.strip() #Saco espacios en blanco del archivo, solo mando el .csv

    def cerrar_socket(self):
        print("Sale del  programa ")
        s.close()

    def handler(self,sig, frame):  # define the handler  
        print("Signal Number:", sig, " Frame: ", frame)  
        traceback.print_stack(frame)	
        self.cerrar_socket()
        
        
    def main(self):
      
        signal.signal(signal.SIGINT, self.handler)  #requerimiento de signal
     
        port = 10000
        server_address=("localhost",port)
        print('conectado a {}, puerto {}'.format(server_address[0],server_address[1]))
        
        try:
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto") # olocar otro mensaje de exepcion
            exit(1)

        archivo_csv=self.get_file_csv()    #Obtengo el archivo de acuerdo a requerimiento "El programa leerá la ruta del archivo CSV desde un archivo config.txt"
        print(archivo_csv) 
       
        #creo objeto CSV 
        obj_csv=Csv(archivo_csv)
        #print(type(obj_csv))
        #print(obj_csv.get_csv_name())
        
        while True:
            try:
                #Obtengo el dato en formato jason 
                data_json=obj_csv.leer_csv()
                print(data_json)
                
                #creo socket para enviar a PizarraService
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(bytearray(data_json,"utf-8"),server_address)
                
                #espero nuevamente 30 segndos para volver a leer los valores
                time.sleep(10)
                #requerimiento "Se deberá leer el archivo y enviar los datos cada 30 segundos"
            
            except:
                print('cerrando socket..')
                break             
            

        

#print("hola")
m=Main('config.txt') #requerimiento "El programa leerá la ruta del archivo CSV desde un archivo config.txt"
m.main()
