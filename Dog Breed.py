class Dog:
    
    species = "Dog"
    
    def __init__(self,breed, anger, color):
        self.breed = breed
        self.anger = anger
        self.color = anger
        
        
Chop = Dog("Rottweiler",10,"Black")
Hunter = Dog("Husky",5,"Ash")
Bella = Dog("Bulldog", 3, "White")
Bruno = Dog("German Sheperd", 6 ,"Brown")
Charlie = Dog("Golden Retriever",2,"Dark Golden")

print(f"Chop is a {Dog.species}")
print(f"Hunter is a {Dog.species}")     
print(f"Bella is a {Dog.species}") 
print(f"Bruno is a {Dog.species}")
print(f"Charlie is a {Dog.species}")

print()

print(f"Chop's breed is {Chop.breed}")
print(f"Hunter's breed is {Hunter.breed}")
print(f"Bella's breed is {Bella.breed}")
print(f"Bruno's breed is {Bruno.breed}")
print(f"Charlie's breed is {Charlie.breed}")

print()

print(f"Chop's anger level is {Chop.anger}")
print(f"Hunter's anger level is {Hunter.anger}")
print(f"Bella's anger level is {Bella.anger}")
print(f"Bruno's anger level is {Bruno.anger}")
print(f"Charlie's anger level is {Charlie.anger}")