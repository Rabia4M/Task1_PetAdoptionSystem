import random
pet_pref={
    'Cat':('fish','meat','milk','scratch pad'),
    'Dog':('bones','walk','playing fetch'),
    'Parrot':('green chillies','some time outside the cage')
}
pet_dict=dict()
class Pet():
  def __init__(self,name,species,age):
    self.name=name
    self.species=species
    self.age=age

  def display_info(self):
    print(f"Name : {self.name}\n")
    print(f"Species : {self.species}\n")
    print(f"Age : {self.age}\n")

class Dog(Pet):
  def __init__(self,name,age,breed,color):
    super().__init__(name,'Dog',age)
    self.breed=breed
    self.color=color

  def display_info(self):
    super().display_info()
    print(f"Breed : {self.breed}\n")
    print(f"Color : {self.color}\n")

class Cat(Pet):
  def __init__(self,name,age,breed,color):
    super().__init__(name,'Cat',age)
    self.breed=breed
    self.color=color

  def display_info(self):
    super().display_info()
    print(f"Breed : {self.breed}\n")
    print(f"Color : {self.color}\n")


def adopt_pet(pet_dict):
    adopt_id = input("Enter the pet id of the pet you want to adopt:")
    if adopt_id in pet_dict:
      pet=pet_dict[adopt_id]
      pet.display_info()
      confirm=input("Confirm adoption by entering 'y'").strip().lower()
      if confirm=='y':
        print(f"Thank You for adopting!")
        del pet_dict[adopt_id]
      else:
        print("Adoption cancelled try again")
    else:
      print("Invalid pet id please re-check the pet id!")
def add_pet(pet_dict):
  print("\nEnter the details:\n")
  while True:
    type=int(input("Choose type of pet:\n1.Cat\n2.Dog\n3.Other\nEnter your choice"))
    new_name=input("Enter the name of the pet:")
    new_age=input("Enter age of the pet:")
    new_id=generate_id(pet_dict,length=6)
    if type==1 or type==2:
      new_breed=input("Enter breed of the pet:")
      new_color=input("Enter color of the pet:")

    if type==1:
      new_cat=Cat(new_name,new_age,new_breed,new_color)
      pet_dict[new_id]=new_cat
      print("Successful addition")
      return

    elif type==2:
      new_dog=Dog(new_name,new_age,new_breed,new_color)
      pet_dict[new_id]=new_dog
      print("Successful addition")
      return

    elif type==3:
      new_species=input("Enter species of the pet:")
      new_pet=Pet(new_name,new_species,new_age)
      pet_dict[new_id]=new_pet
      print("Successful addition")
      return

    else:
      print("Invalid type of pet")

def generate_id(pet_dict,length=6):
  while True:
    id= ''.join(random.choice('0123456789') for _ in range(length))
    if id not in pet_dict:
      return id

def menu(pet_dict):
    while True:
      print("\nOptions:\n1.View available pets\n2.Adopt a pet\n3.Add a pet\n4.View Pet preferences\n5.Exit\n")
      try:
        num = int(input("Choose an option (1-5): "))
      except ValueError:
        print("Please enter a valid number!")
        continue


      if num == 1:
        if not pet_dict:
          print("There are no available pets!!")
        else:
          for id,obj in pet_dict.items():
            print(f"Pet id : {id}")
            obj.display_info()
            print()

      elif num == 2:
        adopt_pet(pet_dict)

      elif num==3:
        add_pet(pet_dict)

      elif num==4:
        for p,pref in pet_pref.items():
          print(f"{p} has {pref} care preferences")

      elif num==5:
        exit()

      else:
        print("Invalid choice!")
menu(pet_dict)
