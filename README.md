##  Cómo ejecutar y probar el programa

###  Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado:

* Python 3.x
* Librería graphviz

Instalar la librería:

```bash
python -m pip install graphviz
```

Instalar Graphviz (programa):

https://graphviz.org/download/

Importante: Durante la instalación, agregar Graphviz al PATH del sistema.

---

###  Ejecución del programa

1. Clonar el repositorio:

```bash
git clone https://github.com/darevaloz-svg/Tarea-4_Arbol_AVL.git
cd Tarea-4_Arbol_AVL
```

2. Ejecutar el programa:

```bash
python main.py
```

---

###  Uso del menú

Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:

1. Insertar un número en el árbol
2. Buscar un número
3. Eliminar un número
4. Cargar datos desde un archivo CSV
5. Visualizar el árbol (Graphviz)
6. Salir

---

###  Ejemplo de prueba

Puedes probar el programa con los siguientes pasos:

1. Insertar valores:

```
10, 20, 30
```

2. Visualizar el árbol (opción 5)

 El sistema balanceará automáticamente el árbol (AVL)

---

###  Prueba con archivos CSV

El proyecto incluye archivos de prueba:

* data1.csv
* data2.csv
* data3.csv

Para usarlos:

1. Seleccionar la opción 4 (Cargar CSV)
2. Ingresar el nombre del archivo, por ejemplo:

```
data1.csv
```

---

###  Visualización

Al seleccionar la opción 5:

* Se genera un archivo llamado `arbol_avl.pdf` o `.png`
* Se abre automáticamente mostrando el árbol balanceado

---

###  Posibles errores

* Si no se genera la imagen:

  * Verificar que Graphviz esté instalado
  * Ejecutar en terminal:

    ```
    dot -V
    ```

* Si aparece error de módulo:

  ```
  No module named 'graphviz'
  ```

  Ejecutar:

  ```
  python -m pip install graphviz
  ```

---
