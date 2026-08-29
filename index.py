###################Programmation orienté objet en Pyhthon######################


# class Voiture :
    
#     couleur = "Voiture de couleur noire"
    
#     def Toyota(self) :
        
        
#         vitesse = int(input("etre la vitesse (par km) de votre voiture "))
#         marque = {"Toyota" : "100km/h",
#                   "lamborghini" : "150km/h",
#                   "Lactis" : "120km/h"
#                   }
#         if vitesse >= 100 :
#             for i, value in marque.items() :
#                print("Votre voiture est de marque",f"{i} de vitesse : {value}")
               
#         else :
#             print("aucune voiture ne correspond a votre description")
            
       
# car1 = Voiture()
# car2 = Voiture()
# car1.Toyota()
# print(car2.couleur)


#class Cours : #classe qui ne fait rien et qui cause aucun probleme
    pass

#creer les variable de la classe en dehors de la classe (dans ce cas on declare les variable en dehors de la fonction)
# c = Cours()
# c.etudiant = "samuel" 
# c.duree = 120

# print(f"Etudiants : {c.etudiant}")
# print((f"Duree du cours : {c.duree}"))

#print(type(c))


class Cours : 
    def __init__(self,titre,etudiant,duree) :
        self.titre = titre
        self.etudiant = etudiant
        self.dure = duree
        
    
    def afficher_info(self) :
        print(f"Etudiants : {self.etudiant}")
        print((f"Duree du cours : {self.dure}"))
        
        
c = Cours("Python","samuel","tous",120)
c.afficher_info()


    
    
