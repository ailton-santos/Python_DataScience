#2.Crieumprogramaqueirárecebervalores,
# o usuário poderá digitar quantos valores ele quiser 
# até ele digitar 0
# ,mostre em tela os valores digitados e sua média.

# creating an empty list

import numpy as np
import statistics as sttc

list = []

i = -1



while i != 0:
        
        i = int(input("digite um numero:"))

        if i != 0:      
                list.append(i)
                
                print(list)
                


        else:
                print(list)
        
        
        print("A média dos numeros é:")
        print(np.mean(list))

    


