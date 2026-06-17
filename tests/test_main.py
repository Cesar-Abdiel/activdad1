from main import obtener_componentes_reutilizables, obtener_modulos


def test_obtener_modulos():
    modulos = obtener_modulos()

    assert "Inventarios" in modulos
    assert "Ventas" in modulos
    assert "Facturación" in modulos
    assert "Reportes" in modulos
    assert len(modulos) == 4


def test_obtener_componentes_reutilizables():
    componentes = obtener_componentes_reutilizables()

    assert "Autenticación y roles" in componentes
    assert "Gestión de productos" in componentes
    assert "Control de stock" in componentes
    assert "Generador de facturas" in componentes
    assert len(componentes) >= 5