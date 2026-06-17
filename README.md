# TecnoMarket Bolivia - Reutilización de Software

Este repositorio corresponde a la actividad de Ingeniería de Software II sobre análisis arquitectónico, reutilización de componentes, refactorización y pipeline CI/CD.

## Caso de estudio

El caso seleccionado es el sistema administrativo de la empresa TecnoMarket Bolivia, dedicada a la venta de accesorios tecnológicos.

## Módulos principales

- Inventarios
- Ventas
- Facturación
- Reportes

## Componentes reutilizables

- Autenticación y roles
- Gestión de productos
- Control de stock
- Registro de ventas
- Generador de facturas
- Generador de reportes
- Exportador PDF/Excel

## Pipeline CI/CD

El repositorio incluye un workflow de GitHub Actions ubicado en:

```text
.github/workflows/ci.yml