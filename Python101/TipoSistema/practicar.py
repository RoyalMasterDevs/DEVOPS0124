# Luis quiere abrir su pizzeria 

# 1. Visualizar que hacer.
# 2. Divide en tareas pequeñas las tareas grandes.
# 3. Aplica logica en todos los pasos.

# Declarar las variables

cliente: str = "Carlos"
basePizza: str = "Delgada"
PizzaTamanio: int = 14
ingredientes: str = "jamon"
extraQueso: bool = True
precio: float = 89.50

# Alternativa 1 - Usando Funciones Con Print

print(f"Se recibe la orden de: {cliente}")
print(f"Pizza base: {basePizza}, tamaño: {PizzaTamanio} pulgadas y de ingredientes: {ingredientes}")
print(f"se requiere con extra queso {extraQueso}")
print(f"La cuenta es de: {precio}")


# Alternativa 2 Strings formateados

detallesOrden: str = f"""
Se recibe orden de: {cliente}
Base Pizza: {basePizza}, tamaño: {PizzaTamanio} pulgadas, ingrediente: {ingredientes}
Con extra queso?: {extraQueso}
El precio va a ser de: ${precio}
"""

# Alternativa 3 - Usando el f string en "print"
print(f""" Se recibe orden de: {cliente}, pizza base: {basePizza}, tamaño:{PizzaTamanio} pulgadas, ingredientes:{ingredientes}, con extra queso?: {extraQueso}, la Cuenta es de: ${precio}""")