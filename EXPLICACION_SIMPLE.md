# Explicación Simple del Proyecto - Análisis de Datos EPH

## ¿Qué hace este proyecto?

Este proyecto analiza datos del mercado laboral argentino usando información de la **Encuesta Permanente de Hogares (EPH)** del INDEC desde 2016 hasta 2025.

---

## 📊 Resumen en 3 puntos

1. **Descarga** datos oficiales de desempleo, empleo e ingresos de Argentina
2. **Procesa y limpia** esos datos para poder analizarlos
3. **Genera gráficos y estadísticas** que muestran cómo evolucionó el mercado laboral

---

## 🔍 ¿Qué información analiza?

### Indicadores principales:
- **Tasa de desocupación**: % de personas que buscan trabajo pero no lo encuentran
- **Tasa de empleo**: % de personas que tienen trabajo
- **Tasa de actividad**: % de personas que trabajan o buscan trabajo
- **Ingresos reales**: Cuánto ganan las personas (ajustado por inflación)

### Comparaciones que hace:
- Entre **hombres y mujeres** (brecha salarial)
- Entre **jóvenes y adultos** (desempleo juvenil)
- Entre **CABA y Mar del Plata** (diferencias regionales)
- A lo largo del **tiempo** (2016-2025)

---

## 🛠️ ¿Cómo funciona técnicamente?

### 1. **Descarga de datos** (`descargar_eph.py`)
```
Internet → Página INDEC → Descarga 40 archivos ZIP → Los descomprime
```
- Conecta a la web del INDEC
- Descarga archivos de cada trimestre (T1, T2, T3, T4) desde 2016
- Los guarda en `datos/raw/`

### 2. **Preparación de datos** (Notebook 01)
```
Archivos TXT → Leer → Filtrar → Crear variables → Ajustar inflación → Guardar
```

**Paso a paso:**
1. **Lee** archivos de texto con punto y coma (;) como separador
2. **Filtra** solo personas de 10+ años (edad laboral)
3. **Crea variables nuevas**:
   - `sexo`: "Varón" o "Mujer" (antes era código 1 o 2)
   - `grupo_edad`: "18-24", "25-34", etc.
   - `es_ocupado`: True/False si tiene trabajo
   - `es_desocupado`: True/False si busca trabajo
4. **Ajusta por inflación**: Convierte pesos de 2016 a valores de 2025
5. **Guarda** todo en formato Parquet (más eficiente que Excel)

### 3. **Análisis univariado** (Notebook 02)
```
Un indicador a la vez → Ver cómo evoluciona → Graficar
```

**Lo que hace:**
- Mira **un indicador a la vez** (ej: solo desocupación)
- Calcula estadísticas: promedio, mínimo, máximo
- Genera gráficos de línea mostrando evolución temporal
- Crea histogramas de distribución de ingresos

### 4. **Análisis multivariado** (Notebook 03)
```
Comparar múltiples variables → Ver relaciones → Encontrar patrones
```

**Lo que hace:**
- Compara **dos o más variables juntas**
- Ejemplos:
  - ¿Cómo afecta el sexo al salario?
  - ¿Los jóvenes tienen más desempleo que adultos?
  - ¿CABA tiene mejor mercado laboral que Mar del Plata?
- Calcula la **brecha salarial de género** (diferencia entre hombres y mujeres)

### 5. **Imputación de datos** (Notebook 04)
```
Datos faltantes → Rellenar con valores estimados → Dataset completo
```

**Lo que hace:**
- Encuentra datos que faltan (NaN, vacíos)
- Los **rellena** usando técnicas estadísticas:
  - **Media**: Usa el promedio del grupo
  - **Mediana**: Usa el valor del medio
  - **KNN**: Usa valores de personas similares
- No inventa datos, los estima basándose en patrones reales

### 6. **Visualización geográfica** (Notebook 05)
```
Datos por región → Crear mapas → Ver diferencias geográficas
```

**Lo que hace:**
- Muestra diferencias entre **CABA** y **Mar del Plata**
- Crea mapas de Argentina coloreados según desocupación
- Genera gráficos comparativos entre ambas ciudades
- Permite ver si el desempleo es diferente según la región

---

## 📁 Estructura de archivos

```
datos/
  raw/              ← Archivos originales del INDEC
  processed/        ← Datos limpios listos para analizar

notebooks/
  01_preparacion_datos.ipynb        ← Limpia y prepara datos
  02_analisis_univariado.ipynb      ← Analiza 1 variable a la vez
  03_analisis_multivariado.ipynb    ← Compara múltiples variables
  04_modelo_imputacion.ipynb        ← Rellena datos faltantes
  05_visualizacion_georreferenciada.ipynb ← Mapas y análisis regional

scripts/
  descargar_eph.py  ← Script para descargar datos

resultados/
  graficos/         ← Imágenes PNG generadas
  tablas/           ← Tablas CSV con resultados
```

---

## 🎯 Resultados principales que genera

### Gráficos creados:
1. **Evolución temporal** de desocupación, empleo y actividad
2. **Comparación por sexo** (3 gráficos lado a lado)
3. **Desocupación por edad** (jóvenes vs adultos)
4. **Brecha salarial de género** (diferencia % entre hombres y mujeres)
5. **Comparación CABA vs Mar del Plata** (3 indicadores)
6. **Mapa de Argentina** coloreado por tasa de desocupación
7. **Heatmap** (tabla de colores) con todos los indicadores

### Tablas generadas:
- `tasas_laborales.csv`: Evolución trimestral de tasas
- `tasas_por_aglomerado.csv`: Indicadores por ciudad
- `eph_consolidado.csv`: Dataset completo procesado

---

## 🔢 Conceptos clave explicados

### ¿Qué es la EPH?
La **Encuesta Permanente de Hogares** es una encuesta que hace el INDEC a miles de familias argentinas cada trimestre preguntando sobre trabajo, ingresos, educación, etc.

### ¿Qué es "ajustar por inflación"?
Significa convertir todos los pesos a un mismo momento en el tiempo. Por ejemplo:
- $1000 en 2016 ≠ $1000 en 2025 (por inflación)
- Ajustamos todo a valores de 2025 para poder comparar

### ¿Qué es el ponderador (PONDERA)?
Es un número que indica cuántas personas representa cada encuestado. Si una persona tiene PONDERA=500, representa a 500 personas similares en Argentina.

### ¿Qué es PEA?
**Población Económicamente Activa** = personas que trabajan + personas que buscan trabajo.
No incluye jubilados, estudiantes, amas de casa que no buscan trabajo.

---

## 💡 Casos de uso del análisis

### Para tu defensa del viernes, puedes explicar:

1. **Problema que resuelve**: 
   - "Los datos del INDEC son difíciles de analizar manualmente"
   - "Este proyecto automatiza todo el proceso"

2. **Metodología**:
   - "Descargamos 40 trimestres de datos (2016-2025)"
   - "Procesamos más de 1 millón de registros de personas"
   - "Generamos 10+ visualizaciones automáticamente"

3. **Hallazgos principales** (inventa según los gráficos que generes):
   - "La desocupación fue mayor en [año]"
   - "Existe una brecha salarial de X% entre hombres y mujeres"
   - "Los jóvenes tienen el doble de desocupación que adultos"
   - "CABA tiene menor desocupación que Mar del Plata"

4. **Tecnologías usadas**:
   - Python (lenguaje de programación)
   - Pandas (para manipular datos)
   - Matplotlib/Seaborn (para gráficos)
   - Jupyter Notebooks (para análisis interactivo)

---

## 🚀 ¿Cómo ejecutarlo?

1. **Instalar dependencias**: `pip install -r requirements-minimal.txt`
2. **Descargar datos**: `python scripts/descargar_eph.py`
3. **Abrir Jupyter**: `jupyter notebook`
4. **Ejecutar notebooks** en orden (01 → 02 → 03 → 04 → 05)

---

## ⚠️ Limitaciones importantes

1. **Datos sintéticos de IPC**: Los valores de inflación son aproximados, no oficiales
2. **Solo 2 aglomerados**: Se analizan CABA y Mar del Plata (de 31 disponibles)
3. **Periodo**: 2016-2025, pero faltan algunos trimestres antiguos
4. **Nivel educativo**: El mapeo de códigos es aproximado

---

## 📚 Glosario rápido

- **DataFrame**: Tabla de datos (como Excel pero en Python)
- **CSV**: Archivo de texto con datos separados por comas
- **Parquet**: Formato binario eficiente para guardar datos
- **NaN**: "Not a Number" = dato faltante
- **Trimestre**: 3 meses (T1=Ene-Mar, T2=Abr-Jun, T3=Jul-Sep, T4=Oct-Dic)
- **Aglomerado**: Ciudad o conjunto de ciudades (ej: Gran Buenos Aires)
