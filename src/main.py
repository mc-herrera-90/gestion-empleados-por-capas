from presentacion.menu_principal import MenuPrincipal
from persistencia.gestor_db import GestorBD

def main():
    gdb = GestorBD('schema.sql')
    gdb.crear_esquema()
    MenuPrincipal()

if __name__ == "__main__":
    main()