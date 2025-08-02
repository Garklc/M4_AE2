# main.py

from persona import Persona
from tamagotchi import Tamagotchi

def main():
    # Crear un Tamagotchi
    mi_tamagotchi = Tamagotchi(nombre="Pichu", color="Amarillo")

    # Crear una Persona y asignarle el Tamagotchi
    persona = Persona(nombre="Juan", apellido="Pérez", tamagotchi=mi_tamagotchi)

    # Interactuar con el Tamagotchi
    print("Estado inicial del Tamagotchi:")
    print(f"Salud: {mi_tamagotchi.salud}, Felicidad: {mi_tamagotchi.felicidad}")

    # La persona le da comida al Tamagotchi
    persona.darle_comida()

    # La persona juega con el Tamagotchi
    persona.jugar_con_tamagotchi()

    # La persona cura al Tamagotchi
    persona.curarlo()

    # Estado final del Tamagotchi
    print("\nEstado final del Tamagotchi:")
    print(f"Salud: {mi_tamagotchi.salud}, Felicidad: {mi_tamagotchi.felicidad}")

if __name__ == "__main__":
    main()