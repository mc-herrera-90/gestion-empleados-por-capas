from presentacion.menu_departamento import MenuDepartamento
from presentacion.menu_principal import MenuPrincipal
from persistencia.gestor_db import GestorBD

def main():
    gdb = GestorBD('schema.sql')
    gdb.crear_esquema()
    menu_principal = MenuPrincipal()

if __name__ == "__main__":
    main()