import csv
from avl import AVL
from visualizer import graficar_arbol

def cargar_csv(ruta, arbol):
    try:
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    arbol.raiz = arbol.insertar(arbol.raiz, int(valor))
        print("Datos cargados correctamente.")
    except Exception as e:
        print("Error:", e)

def menu():
    arbol = AVL()

    while True:
        print("\n--- MENÚ AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Visualizar (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            valor = int(input("Ingrese número: "))
            arbol.raiz = arbol.insertar(arbol.raiz, valor)

        elif opcion == "2":
            valor = int(input("Buscar: "))
            resultado = arbol.buscar(arbol.raiz, valor)
            print("Encontrado" if resultado else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar: "))
            arbol.raiz = arbol.eliminar(arbol.raiz, valor)

        elif opcion == "4":
            ruta = input("Ruta CSV: ")
            cargar_csv(ruta, arbol)

        elif opcion == "5":
            graficar_arbol(arbol.raiz)

        elif opcion == "6":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
