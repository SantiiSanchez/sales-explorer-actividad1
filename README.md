# Sales Explorer — Actividad 2

Esta aplicación permite analizar ventas mediante filtros, indicadores y gráficas.

El código fue reorganizado en tres partes:

- `app.py`: interfaz principal, filtros y KPIs.
- `data/loaders.py`: carga y limpieza de datos.
- `components/charts.py`: generación de gráficas.

## Comparación con la solución del kit

**Diferencia 1: Carga de datos**

La solución del kit permite cargar datos desde diferentes rutas. En mi versión se utiliza directamente el archivo CSV del proyecto.

Decidimos hacerlo así porque la actividad utiliza un solo archivo y resulta más fácil de entender.

**Diferencia 2: Top 10 de SKUs**

La solución del kit permite modificar la cantidad de SKUs mediante un parámetro. Mi versión siempre muestra los 10 productos con mayores ingresos.

Mantuvimos esta diferencia porque el ejercicio solicita específicamente un top 10 y no es necesario agregar más complejidad.

## Resultado

La aplicación conserva las funciones de la Actividad 1, pero ahora utiliza un código modular y más organizado.
