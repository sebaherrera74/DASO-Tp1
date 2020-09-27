import socket
import json
import os
import sys

#Cliente UDP 

class Main:

    def __init__(self):
        pass

    def main(self):

        port = 10000
        try:
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto")
            exit(1)

        data=[{"id": 1, "value1": 80, "value2": 30, "name": "Dolar"}, {"id": 2,"value1": 65, "value2": 70, "name": "Euro"}]
        coding=json.dumps(data)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytearray(coding,"utf-8"),("localhost",port))
        
        #while True:
            #(data, addr) = s.recvfrom(128*1024)
            #data = Parser.parseData(data)
            #self.model.updateData(data)
            #self.view.show()
            #s.sendto(bytearray("OK","utf-8"),addr)
        
        #finally:
            #
         #   print("Cierro Socketpass") 
          #  s.close()

m = Main()
m.main()