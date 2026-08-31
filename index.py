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
 
# class Cours :  
#     def __init__(self,titre,etudiant,duree) :
#         self.titre = titre
#         self.__etudiant = etudiant
#         self.dure = duree
        # self._protege = 15
        # self.__prive = 10 #accessible seulement avec ou dans les methode de la classe
    # def afficher_info(self) :
        
        # print(f"Titre du cours : {self.titre}")
        # print("Etudiants : ",self.__etudiant)
        # print((f"Duree du cours : {self.dure} min"))
        
        
# c2 = Cours(titre = "django",etudiant = 0,duree =20)
# c2.afficher_info()
# "_protege" in print(dir(c2))
# "__prive" in print(dir(c2))

# print(c2._protege)
#print(c2.__prive) # ça ne va pas s'execter car la variable est privé
# print(c2._Cours__prive) # accessible seulement avec ou dans les methode de la classe





############## avoir acces ou modifier aux element protege, prive avec les methode get et set#################

# class Cours :  
#     def __init__(self,titre,etudiant,duree) :
#         self.titre = titre
#         self.dure = duree
#         self.__etudiant = etudiant
        
        
#     def get_etudiant(self) : 
#         return self.__etudiant
    
#     def set_etudiant(self, valeur) :
#         if valeur >= 0 :
#             self.__etudiant = valeur
#         else :
#             print("Erreur :le nombre doit etre superieur ou egal a 0")
        
# c = Cours("100+ exercices en POO",120,120)
# print(c.get_etudiant())
# print((c.set_etudiant(-50)))
# print(c.get_etudiant())

############## avoir acces ou modifier aux element protege, prive avec les methode @property #################





# class Cours :  
#     def __init__(self,titre,etudiant,duree) :
#         self.titre = titre
#         self.dure = duree
#         self.__etudiant = etudiant
        
#     @property   
#     def etudiant(self) : 
#         return self.__etudiant
    
#     @etudiant.setter
#     def etudiant (self, valeur) :
#         if valeur >= 0 :
#             self.__etudiant = valeur
#         else :
#             print("Erreur :le nombre doit etre superieur ou egal a 0")
        
# c = Cours("100+ exercices en POO",20,120)
# print(c.etudiant)
# c.etudiant = 10000
# print(c.etudiant)
# c.etudiant = -120
# print(c.etudiant)
# c.etudiant = -120
# print(c.etudiant)




######### Heritage  ##################

#exemple dans une entreprise

class Employe :
    def __init__(self,name,salary) : #,code_editor,designer) :
        self.name = name
        self.salary = salary
        # self.code_editor = code_editor
        # self.designer = designer
        
#     def partir_en_pause (self) :
#         print(f"{self.name} part en pause")
        
        
#     def coder(self) :
#         print(f"{self.name} se met à coder")
        
#     def designer(self) :
#         print(f"{self.name} se met à designer")
        
        
        
        
# personne = Employe("Samuel",2000)
# print(personne.partir_en_pause())


# Toutes les autres classe vont heriter de la classe Employe
    
class Employe :
    def __init__(self,name,salary) : 
        self.name = name
        self.salary = salary
        
    def partir_en_pause (self) :
        print(f"{self.name} part en pause")   
        
class Developpeur(Employe) :
    def __init__(self,name,salary,code_editor) :
        super().__init__(name,salary) #fait reference les attribut de la la classe parent(employer)
        self.code_editor = code_editor
        
    def coder(self) : 
        print(f"{self.name} se met à coder")

class Designer(Employe) :
    def __init__(self,name,salary,designer) :
        super().__init__(name,salary)
        self.designer = designer
        
    def desining (self) :  
        print(f"{self.name} se met a designer")
       
   
codeur = Developpeur("bob",2000,"Visual studio code")
designeur = Designer("samuel",2000,"Figma")

print(codeur.code_editor)
print(designeur.designer)
print(codeur.coder())
print(designeur.desining())



