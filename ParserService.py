import csv
import json
import os
import socket
import sys
import time

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

    def get_file_csv(self):
        with open (self.get_file_name(),"r",encoding="utf-8") as f:
            texto=f.read()
        return texto.strip() #Saco espacios en blanco del archivo, solo mando el .csv

    def main(self):
        port = 10000
        server_address=("localhost",port)
        print('conectado a {}, puerto {}'.format(server_address[0],server_address[1]))
        try:
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto")
            exit(1)
        #Hardcodeo para probar 
        #data=[{'id': '1', 'name': 'Dolar', 'value1': '58.63', 'value2': '61.61'}, {'id': '2', 'name': 'Euro', 'value1': '65.12', 'value2': '68.93'}, {'id': '3', 'name': 'Real', 'value1': '13.45', 'value2': '14.23'}]

        #while True:

            #coding=json.dumps(data)
            #print(coding)
            #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #s.sendto(bytearray(coding,"utf-8"),server_address)
            
            #(data, addr) = s.recvfrom(128*1024)    #Veo mensaje recibido desde server
            #print("Mensaje Recibido :"+str(data))       #Imprimo mensaje recibido                         




print("hola")
m=Main('config.txt')
m.main()
