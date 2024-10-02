class Student:
    
    #class Variable
    grade = 8
    print("Hello I am a student of grade",grade)
    
    #Constructor Method(Function)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
#Creating Object
zabir = Student("ZHR",25)
radoya = Student("Radoya",14)
tabid = Student("Tabid",15)

print(zabir.name, zabir.age)
print(radoya.name, radoya.age)
print(tabid.name, tabid.age)