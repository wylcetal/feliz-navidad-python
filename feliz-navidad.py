# Importaciones
from colorama import Fore  # Importamos desde colorama los colores
import pyfiglet

# Convertimos el texto a arte ASCII
fuente = pyfiglet.figlet_format("Feliz Navidad")

print(Fore.RED, fuente)  # Imprimimos el texto en color rojo
print(Fore.GREEN, "Les deseo que pasen una hermosa noche con todos los que aman 🎄")
