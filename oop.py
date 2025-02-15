#object oriented programming
#we use oop to update any object
class MaryamLove:
    def __init__(self,cloths:str,makeup:str,sheosstock:int):
        self.cloths = cloths
        self.makeup = makeup
        self.sheotocks = sheosstock
    def grooming(self):  
        pass 
MaryamLove("Yes","Yes",50)
print(MaryamLove)
MaryamLove.grooming
class Teacher():
    #class variables
    counter:int = 4
    
    def __init__(self, teacher_id: int, teacher_name: str):
        self.name = teacher_name
        self.id = teacher_id
        self.Org_name = "Unknown"
  
    def speak(self, words: str):
        print(f'{self.name} is speaking {words}')
      
    def teaching(self, subject: str):
        print(f'{self.name} is teaching {subject}') 
      
teacher1:Teacher = Teacher(1,"Maryam") 
teacher2:Teacher = Teacher(2,"Safa") 
teacher3:Teacher = Teacher(3,"Huda")  

print(teacher1.name)   
   
teacher1.speak("Truth")
teacher2.teaching("Maths")
print(teacher1.counter)
#Inheritance
#syntex class ChildClass(Parents):pass
class Parents():
     def __init__(self):
        self.eyecolour = "grey" 
        self.haircolour = "hazel" 
        
  
     def speak(self,language:str):
      print(f'Motherside language is {language}')
    
          
     def lands(self,area:str):
      print(f'Inherited land is in {area}')
    
class Child(Parents):
    def teaching(self,subject:str):
        print(f'Child2 is teaching {subject}')
    
child1:Parents = Parents()
print(child1.eyecolour)
print(child1.haircolour)
print(child1.speak("Memoni"))
print(child1.lands("PECHS"))
 
child2 : Child  = Child()
print(child2.eyecolour)
print(child2.haircolour)
child2.speak("Urdu")
child2.lands("Bahadurabad")
child2.teaching("Python")

 

      