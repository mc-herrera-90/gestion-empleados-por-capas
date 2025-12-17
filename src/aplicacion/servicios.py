from aplicacion.api.mi_indicador import obtener_indicador


def obtener_tasa_desempleo():
    data = obtener_indicador("tasa_desempleo")
    return data["serie"][:10]


def obtener_indicador_diario(indicador):
    data = obtener_indicador()[indicador]
    return data
