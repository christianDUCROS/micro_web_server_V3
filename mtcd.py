def traitement_commandes_dynamiques (commande_split):
    if commande_split[0] == 'btAvancer' and commande_split[1]== '1' :                  
        print ("on avance")
        #action...  
    elif commande_split[0] == 'btStop' and commande_split[1]== '1' :                  
        print ("on s’arrete")
        #action...  

    elif commande_split[0] == 'vitesseT'  :
        print('puissance_moteur=', int(commande_split[1]))	        
        #action...
        
    elif commande_split[0] == 'tourelle' :
        print('Tourelle en position = ',int(commande_split[1]))
        #action


'''
def traitement_commandes_dynamiques (commande): 
    try : 
        commande_split=commande.split('=')
        if commande_split[0] == 'LED' and commande_split[1]== 'ON' :
            print("led on")
            #action...  

        elif commande_split[0] == 'LED' and commande_split[1]== 'OFF' :
            print("led off")
            #action...
        
        elif commande_split[0] == 'pot1' :
            print('potentiometre = ',commande_split[1])
            #action
    except :
        pass
   
'''    