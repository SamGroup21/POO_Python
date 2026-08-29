###################Programmation orienté objet en Pyhthon######################


class Voiture :
    
    couleur = "Voiture de couleur noire"
    
    def Toyota(self) :
        
        vitesse = int(input("etre la vitesse (par km) de votre voiture "))
        marque = {"Toyota" : "100km/h",
                  "lamborghini" : "150km/h",
                  "Lactis" : "120km/h"
                  }
        if vitesse >= 100 :
            for i, value in marque.items() :
               print("Votre voiture est de marque",f"{i} de vitesse : {value}")
               
        else :
            print("aucune voiture ne correspond a votre description")
            
       
car1 = Voiture()
car2 = Voiture()
car1.Toyota()
print(car2.couleur)

    
    
