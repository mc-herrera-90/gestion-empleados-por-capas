from presentacion.menu import Menu

class MenuPrincipal(Menu):

  def __init__(self):
    print("1. Ingresar al sistema")
    print("2. Salir")

    if self.pedir_opcion() == 1:
      self.iniciar_sesion()

  def mostrar_opciones(self):
    print("===== ECOTECH SOLUTIONS =====")
    print("Menú Principal ")
    print("1. Menú de Departamento")
    print("2. Menú de Proyectos")
    print("3. Menú de Empleados")
    print("4. Salir del programa")


  def pedir_opcion(self):
    return int(input("Seleccione una opción: "))

  def pedir_credenciales(self):
    print("===== INICIO DE SESIÓN =====")
    u = input("Usuario MySQL: ")
    p = input("Contraseña MySQL: ")
    return u, p

  def iniciar_sesion(self):

    from aplicacion.reglas_login import ReglasLogin
    login = ReglasLogin()
    conexion = login.iniciar(self.pedir_credenciales)
    if conexion.open:
      print("Accediendo al sistema..")
      self.mostrar_opciones()

# class MenuPrincipal(Menu):

#   def __init__(self) -> None:
#     print("Menú Principal ")
#     print("1. Ingresar al sistema")
#     print("2. Salir")   


#   def mostrar_opciones(self):
#     print("===== ECOTECH SOLUTIONS =====")
#     print("Menú Principal ")
#     print("1. Menú de Departamento")
#     print("2. Menú de Proyectos")
#     print("3. Menú de Empleados")
#     print("4. Salir del programa")

#   def pedir_opcion(self):
#     return int(input("Seleccione una opción: "))

#   def pedir_credenciales(self):
#     print("===== INICIO DE SESIÓN =====")
#     u = input("Usuario MySQL: ")
#     p = input("Contraseña MySQL: ")
#     return u, p

#   def seleccionar_opcion(self):
#     opcion = self.pedir_opcion()

#     if opcion == 1:
#       login = ReglasLogin()
#       conexion = login.iniciar(self.pedir_credenciales)
#       if conexion.open:
#         print("Accediendo al sistema")

#     elif opcion == 2:
#         print("Saliendo..")
#         exit()
#     else:
#         print("Opción inválida. Por favor, seleccione una opción válida.")
