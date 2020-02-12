print("Codigo listas")
bicycles=["trek","cannondale","redline","specialized"]
print(bicycles)
"""Al ejecutar el progrma lo que me manda es la lista de las bicicletas"""
print("\n")




print("Ingresar a los elementos")
"""1.1 INGRESANDO A LOS ELEMENTOS DE LISTA"""
bicycles=["trek","cannondale","redline","specialized"]
print(bicycles[1])
"""Me imprime el elemento de la lista que se encuentra en la posicion deseada"""
bicycles=["trek","cannondale","redline","specialized"]
print(bicycles[0].title())
"""Me imprime el elmento de la lista de la posicion deseada en este caso al 
   inicio de la marca coloca la mayuscula de manera predeterminada"""
print("\n")




print("TAREA")
print("\n")
""" Nombres:Realiza una lista con algunos nombres de tus amigos en una lista 
llamada names. Imprime en la pantalla el nombre de cada persona ingresando 
elemento por elemento. 
• Mensaje: En la lista creada anteriormente, adem´as de imprimir el nombre de
 cada persona imprime un mensaje personalizado para cada persona.
 • Tu propia lista: Piensa en una lista deseos, la lista debe de tener por lo 
 menos 15 elementos. Imprime algunos de los deseos. Ejemplo Me gustar´ıa tener 
 una moto Honda”."""
 
names=["jose","fabricio","danilo","andres"]
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print("\n")
nombres=["daniela","juan","tony","adrian","beto","diana","graciela","monse","cris"]
print("\n".join(nombres))
print("\n")


print("hola " +  names[0] + " meda gusto verte" )
print("hola " +  names[1] + ",me gustaria verte hoy" )
print("hola " +  names[2] + ",¿que es lo que haras hoy de comer?" )
print("hola " +  names[3] + ",espero llegar pronto a casa" )
print("\n")

print("LISTA DEDESEOS")
deseos=["un celular","dinero","una empresa","pasaporte","razonamiento","la capacidad de enteder todo a la primera","mas fuerza","caracter","mas oportunidades laborales","ma confianza","seguridad","facilidad  de palabra","un carro","una novia","una mascota"]
for c, value in enumerate (deseos,1):
    print(c, value)
    print("me gustaria tener " + value)
print("\n")


 
"""FUNCIONES"""
def greet_user():
    print ("hello")
greet_user()
"""Esta funcion lo unico que hace es imprimir un simple saluo ya que no se le 
   estan pasando parametros para que relize otra cosa"""
print("\n")


def greet_user(username):
    print("hello," + username.title() + "!")
greet_user("samanta")
"""aqui en esta segunda funcion lo que isimios fue mandarle o meterle el 
   parametro de nombre de usuario que de manera como tol ya hay una variable 
   con el nombre que nos arrojara al momento de iprimir"""
print("\n")


def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + "." )
    print("my " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("hamster","harry")
describe_pet("dog","willie")
"""en esta funcion ya cuenta con parametros que viene siendo el tipo de animal
   y el nombre, asi que lo que le pasaremos son esos dos datos para que 
   esta funcion imprima tantas veces le mande parametros en este caso solo 
   fueron  2 cosas en especifico que fue el hamster y el perro """
print("\n")


print("\n")
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')
"""Como se observa en este los parametros  se enviaron de forma desordenada asi
    que al imprimir el mensaje no tendra sentido"""
print("\n")

print("KEWORD ARGUMENTS")
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
"""Este  parte lo que hace es que no  importa el orden pues el usuario le asigno
    los valore  a cada  parametro de la funcion,no es recomendable cuando son
    demasiados argumentos pues si se te olvida no puede que  no lo pongas y no
    lo imprima"""
print("\n")


print("DEFAULT VALUES")
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
"""En esta funcion desde el princnipio el usuario le designo un valor al parametro
    esto se realisa cuando de ciertamanera hablaremos de lo mismo en una funcion
    en este caso el tipo de animal sera perro,pero de igual manera podemos modi-
    ficar el typo de animal pasando el parametro con el tipo de animal que desea
    y  este parametro borrara el  valor  predeterminado y colocara el nuevo valor"""
print("DEFAULT VALUES")
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie', animal_type="gato")
print("\n")

print("TAREA")
def make_shirt (tamano_play, tex_imprest):
    print("El tamaño de la playera es  de " + tamano_play + "." )
    print("El texto es " + tex_imprest + "." )
make_shirt("grande","Te amo mama")
print("\n")

print("2parte")
def make_shirt (tamano_play="Grande", tex_imprest="I <3 Python"):
    print("El tamaño de la playera es " + tamano_play + "." )
    print("El texto es " + tex_imprest + "." )
make_shirt()
make_shirt("mediana")
make_shirt("pequeña","Yikes")
print("\n")


print("3ra parte")
def describe_city (ciudad , pais="Cuba"):
    print(ciudad + " esta en " + pais)
describe_city("Havana")
describe_city("Havana")
describe_city("L.A","Estados Unidos")
print("\n")


print("Clases")
class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        print(self.name.title() + " ha dado  una vuelta")

my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.name
my_dog.sit()
my_dog.roll_over()
print("\n")


class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_res(self):
        print("El restaurante " + self.restaurant_name.title() + " trabaja comida " + self.cuisine_type.title())
    def open_restaurant(self):
        print( self.restaurant_name.title()  +" abre de lunes a sabado de 9:30am a 23:00hrs")

my_restaurant=restaurant("dys", "italiana")
my_restaurant.describe_res()
my_restaurant.open_restaurant()
print("\n")


print"TRES RETAURANES"
class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_res(self):
        print("El restaurante " + self.restaurant_name.title() + " trabaja comida " + self.cuisine_type.title())
    def open_restaurant(self):
        print( self.restaurant_name.title()  +" abre de lunes a sabado de 9:30am a 23:00hrs")

my_restaurant=restaurant("the cruw", "americana")
my_restaurant.describe_res()
my_restaurant.open_restaurant()
print("\n")

my_restaurant2=restaurant("La aguja", " cortes de carnes")
my_restaurant2.describe_res()
my_restaurant2.open_restaurant()
print("\n")

my_restaurant3=restaurant("La hoya", "Poblana")
my_restaurant3.describe_res()
my_restaurant3.open_restaurant()
print("\n")

print("USERNAMAE")
class user():
    def __init__(self, frist_name, last_name, date_nac, age, pasword):
        self.frist_name=frist_name
        self.last_name=last_name
        self.date_nac=date_nac
        self.age=age
        self.pasword=pasword
    def describe_user(self):
        print("Usuaerio: "+self.frist_name+"Fecha de nacimiento: "+self.date_nac+"Edad: "+self.age+"Su contraseña es: "+self.pasword)
    def greet_user(self):
        print("Hola " + self.frist_name + self.last_name + " bienvenido al ipn.")

my_user=user("Jose Daniel ", "Tecchi Perez", "13/dic/2000", "19", "2020302278")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Rosendo ", "Peralta", "12/agos/2000", "19", "2026402269")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Monse ", "Tecchi Perez", "25/agos/2001", "18", "2030264270")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Fidel ", "Gamez Flores", "23/mar/2004", "16", "2030222271")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Rosario ", "Vazquez Pacheco", "16/juli/2002", "17", "2030235272")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Gabriel ", "Ordoñez Mendoza", "10/nov/2004", "16", "20295628278")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Oscar ", "Ortega Sandoval ", "13/dic/2000", "19", "2020563278")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Britany ", "Garmendia Soliz", "03/Agos/2000", "19", "20203868284")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Xochitl ", "Perez Lopez", "07/abril/2000", "19", "202175498138")
my_user.describe_user()
my_user.greet_user()
print("\n")
my_user=user("Pedro ", "Yeso Rodriguez", "05/may/2000", "19", "887874832278")
my_user.describe_user()
my_user.greet_user()        
        