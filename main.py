from presentacion.menu_departamento import MenuDepartamento
from presentacion.menu_principal import MenuPrincipal

def main():
    menu_principal = MenuPrincipal()
    menu_principal.mostrar_opciones()
    menu_principal.seleccionar_opcion()

if __name__ == "__main__":
    main()