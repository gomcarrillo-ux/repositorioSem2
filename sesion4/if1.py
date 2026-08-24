#Leer la nota de un estudiante y decir si aprovo o su aprendisaje es inicial.
from colorama import Fore, Style

grade = int(input("Ingrese la nota: "))
if grade >= 70:
    print(Fore.GREEN + "El estudiante aprobó.")
else:
    print(Fore.RED + "Su aprendizaje es inicial.")
print(Style.RESET_ALL)