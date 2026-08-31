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
    # pass

#creer les variable de la classe en dehors de la classe (dans ce cas on declare les variable en dehors de la fonction)
# c = Cours()
# c.etudiant = "samuel" 
# c.duree = 120

# print(f"Etudiants : {c.etudiant}")
# print((f"Duree du cours : {c.duree}"))

#print(type(c))


# class Cours :  
#     def __init__(self,titre,etudiant,duree) :
#         self.titre = titre
#         self.etudiant = etudiant
#         self.dure = duree
        
    
    # def afficher_info(self) :
        # print(f"Etudiants : {self.etudiant}")
        # print((f"Duree du cours : {self.dure}"))
        # ou encore
        # print(f"Titre du cours : {self.titre}")
        # print((f"Duree du cours : {self.dure}min"))
        # print("Etudiants : ",self.etudiant)
        
    # def ajouter_etudiant (self) :  #self ou encore this ou s) :
        # self.etudiant = self.etudiant + 1
        
        
# c1 = Cours("Python","samuel",120)
# c2 = Cours("Java","Decor",20)
#  ou encore 
# c1 = Cours("Python","samuel",120)
# c2 = Cours(titre="Java",etudiant = 0,duree =20)

# c1.afficher_info()
# c2.afficher_info()
# c2.ajouter_etudiant()
# c2.afficher_info()


################################## Encapsulation (proteger les données par exemple un mot de passe, ou 
# ou empecher les erreur en evitant qu'un attribut prenne une valeur impossible ou encore
# controller comment les valeur vont etre modifier) #######################
 
class Cours :  
    def __init__(self,titre,etudiant,duree) :
        self.titre = titre
        self.etudiant = etudiant
        self.dure = duree
        self._protege = 10
        self.__prive = 10 #accessible seulement avec ou dans les methode de la classe
    def afficher_info() :
        
        print(f"Titre du cours : {self.titre}")
        print("Etudiants : ",self.etudiant)
        print((f"Duree du cours : {self.dure}min"))
        
        
c2 = Cours()
c2.afficher_info()
  
        
dir(c2)

