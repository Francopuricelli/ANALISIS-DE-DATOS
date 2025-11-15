# Análisis del Mercado Laboral Argentino (2016-2025)
## Encuesta Permanente de Hogares (EPH) - INDEC

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Descripción del Proyecto

Este proyecto presenta un análisis exhaustivo del mercado laboral argentino para el período 2016-2025, utilizando los microdatos de la **Encuesta Permanente de Hogares (EPH)** del INDEC.

### Objetivos del Análisis

1. **Análisis Univariado**: Evolución histórica de tasas de desocupación, empleo, actividad e ingresos reales
2. **Análisis Multivariado**: Desagregación por nivel educativo, sexo, edad y características del empleo
3. **Modelo de Imputación**: Desarrollo de modelos de regresión para imputar no respuesta en ingresos
4. **Visualización Georreferenciada**: Mapas y análisis geográfico por aglomerado urbano

---

## 🗂️ Estructura del Proyecto

```
ANALISIS-DE-DATOS/
│
├── datos/
│   ├── raw/                    # Datos descargados de EPH (ZIP y TXT)
│   └── processed/              # Datos procesados y consolidados
│
├── notebooks/
│   ├── 01_preparacion_datos.ipynb              # Limpieza y preparación
│   ├── 02_analisis_univariado.ipynb            # Análisis de series temporales
│   ├── 03_analisis_multivariado.ipynb          # Análisis por subgrupos
│   ├── 04_modelo_imputacion.ipynb              # Modelos de regresión
│   └── 05_visualizacion_georreferenciada.ipynb # Mapas y análisis geográfico
│
├── scripts/
│   └── descargar_eph.py        # Script automatizado de descarga de datos
│
├── resultados/
│   ├── graficos/               # Gráficos generados
│   └── tablas/                 # Tablas de resultados
│
├── informe/                    # Informe final (PDF/Word)
│
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

---

## 🚀 Instalación y Configuración

### Prerequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/Francopuricelli/ANALISIS-DE-DATOS.git
cd ANALISIS-DE-DATOS
```

### Paso 2: Crear Entorno Virtual (Recomendado)

```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## 📊 Uso del Proyecto

### 1. Descargar Datos de EPH

```bash
cd scripts
python descargar_eph.py
```

Este script descargará automáticamente todos los microdatos de EPH del período 2016-2025 desde el sitio del INDEC.

### 2. Ejecutar Notebooks

Abrir Jupyter Notebook o JupyterLab:

```bash
jupyter notebook
```

Ejecutar los notebooks en el siguiente orden:

1. **01_preparacion_datos.ipynb**: Carga, limpia y consolida los datos
2. **02_analisis_univariado.ipynb**: Analiza la evolución de indicadores principales
3. **03_analisis_multivariado.ipynb**: Análisis por subgrupos poblacionales
4. **04_modelo_imputacion.ipynb**: Desarrolla modelos de imputación de ingresos
5. **05_visualizacion_georreferenciada.ipynb**: Genera mapas y análisis geográfico

### 3. Resultados

Los resultados se guardarán automáticamente en:
- **Gráficos**: `resultados/graficos/`
- **Tablas**: `resultados/tablas/`

---

## 📈 Indicadores Calculados

### Tasas del Mercado Laboral

- **Tasa de Actividad**: (PEA / PET) × 100
- **Tasa de Empleo**: (Ocupados / PET) × 100
- **Tasa de Desocupación**: (Desocupados / PEA) × 100

Donde:
- **PEA**: Población Económicamente Activa
- **PET**: Población en Edad de Trabajar (10+ años)

### Ingresos

- Ingreso medio y mediano de ocupados
- Ajustados por inflación (IPC)
- Expresados en pesos constantes

### Análisis Multivariado

- Desagregación por:
  - Sexo (Varón/Mujer)
  - Grupos de edad
  - Nivel educativo
  - Rama de actividad económica
  - Categoría ocupacional

---

## 🔬 Metodología

### Fuente de Datos

**INDEC - Encuesta Permanente de Hogares (EPH)**
- URL: https://www.indec.gob.ar/indec/web/Nivel4-Tema-1-39-120
- Período: 2016 (T1) - 2025 (T4)
- Cobertura: 31 aglomerados urbanos de Argentina

### Procesamiento

1. **Descarga**: Obtención automatizada de microdatos
2. **Limpieza**: Tratamiento de valores faltantes y outliers
3. **Ajuste de ingresos**: Deflactación por IPC (base: último trimestre disponible)
4. **Ponderación**: Uso del factor de expansión `PONDERA` para estimaciones poblacionales

### Modelos Estadísticos

- **Regresión Lineal**
- **Ridge Regression (L2)**
- **Lasso Regression (L1)**
- **Random Forest**
- **Gradient Boosting**

Evaluación mediante:
- R² Score
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

---

## 📚 Principales Resultados

> **Nota**: Los resultados específicos se generarán al ejecutar los notebooks con datos reales.

### Hallazgos Esperados:

1. **Evolución Temporal**: Identificación de tendencias y ciclos en el mercado laboral
2. **Brechas de Género**: Análisis de diferencias salariales entre varones y mujeres
3. **Impacto de la Educación**: Relación entre nivel educativo e ingresos
4. **Diferencias Regionales**: Variación de indicadores entre aglomerados
5. **Modelo de Imputación**: Capacidad predictiva del modelo para estimar ingresos

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|-----------|
| **Python 3.9+** | Lenguaje de programación principal |
| **Pandas** | Manipulación y análisis de datos |
| **NumPy** | Operaciones numéricas |
| **Matplotlib** | Visualización de datos |
| **Seaborn** | Visualizaciones estadísticas |
| **Scikit-learn** | Modelos de machine learning |
| **Plotly** | Mapas interactivos (opcional) |
| **Geopandas** | Análisis geoespacial (opcional) |
| **Jupyter** | Notebooks interactivos |

---

## 📝 Requisitos del Trabajo

Este proyecto cumple con los siguientes objetivos académicos:

### ✅ Aprobación No Directa (4-5 puntos)

1. ✅ **Análisis univariado**: Evolución histórica de medidas de tendencia central y posición
2. ✅ **Análisis multivariado**: Desagregación por nivel educativo, características del empleo, sexo y edad
3. ✅ **Visualización de datos**: Gráficos de series temporales, boxplots, barras, etc.

### ✅ Aprobación Directa (6-10 puntos)

4. ✅ **Modelo de imputación**: Desarrollo, evaluación e interpretación de modelos de regresión
5. ✅ **Visualización georreferenciada**: Mapas por aglomerado con indicadores laborales

---

## 👥 Equipo de Trabajo

> **Nota**: Completar con los nombres de los integrantes del grupo

- Integrante 1: [Nombre]
- Integrante 2: [Nombre]
- Integrante 3: [Nombre]
- Integrante 4: [Nombre] (opcional)

**Aglomerados asignados**: [Indicar los dos aglomerados a comparar]

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 📧 Contacto

Para consultas o sugerencias sobre este proyecto:

- **Email**: [correo@ejemplo.com]
- **GitHub**: [Francopuricelli](https://github.com/Francopuricelli)

---

## 🙏 Agradecimientos

- **INDEC** por proporcionar acceso público a los microdatos de la EPH
- **Cátedra de Análisis de Datos** por la guía y orientación del proyecto

---

## 📌 Notas Importantes

1. **Datos del IPC**: Los valores de IPC incluidos son aproximados. Para el análisis final, actualizar con datos oficiales del INDEC.

2. **Geocodificación**: Las coordenadas de aglomerados son aproximaciones. Para análisis precisos, usar shapefiles oficiales.

3. **Recursos Computacionales**: El procesamiento de datos puede requerir recursos significativos (RAM 8GB+ recomendado).

4. **Actualización de Datos**: Los datos de EPH se publican trimestralmente. Verificar disponibilidad de períodos recientes en el sitio del INDEC.

---

**Fecha de última actualización**: Noviembre 2025

**Versión**: 1.0
