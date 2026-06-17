"""
Sistema TecnoMarket Bolivia

Este archivo representa una simulación básica del sistema administrativo
utilizado para la actividad de reutilización de software y arquitectura
de componentes.
"""


def obtener_modulos():
    """
    Retorna los módulos principales del sistema.
    """
    return [
        "Inventarios",
        "Ventas",
        "Facturación",
        "Reportes",
    ]


def obtener_componentes_reutilizables():
    """
    Retorna los componentes reutilizables propuestos para el sistema.
    """
    return [
        "Autenticación y roles",
        "Gestión de productos",
        "Control de stock",
        "Registro de ventas",
        "Generador de facturas",
        "Generador de reportes",
        "Exportador PDF/Excel",
    ]


def iniciar_sistema():
    """
    Inicia una simulación básica del sistema TecnoMarket Bolivia.
    """
    print("Sistema TecnoMarket Bolivia iniciado correctamente")
    print("Módulos principales:")

    for modulo in obtener_modulos():
        print(f"- {modulo}")

    print("\nComponentes reutilizables:")

    for componente in obtener_componentes_reutilizables():
        print(f"- {componente}")

    
if __name__ == "__main__":
    iniciar_sistema()