# Guía Rápida de Inicio - Análisis EPH

## 🚀 Inicio Rápido (5 minutos)

### 1. Preparar el Entorno

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Descargar Datos

```powershell
cd scripts
python descargar_eph.py
cd ..
```

⏱️ Tiempo estimado: 10-30 minutos (según velocidad de Internet)

### 3. Ejecutar Análisis

```powershell
# Iniciar Jupyter
jupyter notebook
```

Ejecutar notebooks en orden:
1. `01_preparacion_datos.ipynb` ⏱️ ~5-10 min
2. `02_analisis_univariado.ipynb` ⏱️ ~5 min
3. `03_analisis_multivariado.ipynb` ⏱️ ~5 min
4. `04_modelo_imputacion.ipynb` ⏱️ ~10-15 min
5. `05_visualizacion_georreferenciada.ipynb` ⏱️ ~5 min

---

## 📊 Estructura de los Notebooks

### Notebook 1: Preparación de Datos
- ✅ Carga de datos EPH de todos los trimestres
- ✅ Limpieza y consolidación
- ✅ Creación de variables derivadas
- ✅ Ajuste de ingresos por inflación
- 📤 Output: `eph_consolidado.parquet`, `tasas_laborales.csv`

### Notebook 2: Análisis Univariado
- ✅ Evolución de tasas (desocupación, empleo, actividad)
- ✅ Estadísticas descriptivas
- ✅ Gráficos de series temporales
- ✅ Análisis de ingresos reales
- 📤 Output: 6 gráficos + 1 tabla resumen

### Notebook 3: Análisis Multivariado
- ✅ Tasas por sexo
- ✅ Tasas por grupo de edad
- ✅ Brecha salarial de género
- ✅ Ingresos por nivel educativo
- 📤 Output: 5 gráficos + 3 tablas

### Notebook 4: Modelo de Imputación
- ✅ Análisis de no respuesta
- ✅ 5 modelos de regresión comparados
- ✅ Evaluación de rendimiento (R², RMSE, MAE)
- ✅ Interpretación de variables
- 📤 Output: 3 gráficos + 2 tablas

### Notebook 5: Visualización Georreferenciada
- ✅ Mapas de Argentina por aglomerado
- ✅ Gráficos de barras geográficos
- ✅ Heatmaps de indicadores
- ✅ Mapa interactivo (opcional)
- 📤 Output: 3-4 gráficos + 2 tablas

---

## 🎯 Checklist del Proyecto

### Antes de Empezar
- [ ] Python 3.9+ instalado
- [ ] Git instalado (opcional)
- [ ] 5GB+ de espacio en disco
- [ ] Conexión a Internet estable

### Configuración Inicial
- [ ] Repositorio clonado/descargado
- [ ] Entorno virtual creado
- [ ] Dependencias instaladas
- [ ] Jupyter funcionando

### Ejecución
- [ ] Datos EPH descargados
- [ ] Notebook 1 ejecutado
- [ ] Notebook 2 ejecutado
- [ ] Notebook 3 ejecutado
- [ ] Notebook 4 ejecutado
- [ ] Notebook 5 ejecutado

### Entregables
- [ ] Gráficos generados (20+)
- [ ] Tablas generadas (10+)
- [ ] Informe escrito (6-10 páginas)
- [ ] Código documentado
- [ ] README actualizado

---

## ⚠️ Solución de Problemas Comunes

### Error: "No module named 'pandas'"
```powershell
pip install pandas numpy matplotlib seaborn
```

### Error al descargar datos EPH
- Verificar conexión a Internet
- Algunos trimestres pueden no estar disponibles
- Ejecutar nuevamente después de unos minutos

### Jupyter no abre
```powershell
pip install --upgrade jupyter
jupyter notebook --no-browser
```

### Notebook muy lento
- Cerrar notebooks no utilizados
- Reiniciar kernel: Kernel → Restart
- Liberar RAM cerrando aplicaciones

### Gráficos no se muestran
```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.show()
```

---

## 📈 Indicadores Principales

### Fórmulas Clave

**Tasa de Actividad**
```
TA = (PEA / PET) × 100
```

**Tasa de Empleo**
```
TE = (Ocupados / PET) × 100
```

**Tasa de Desocupación**
```
TD = (Desocupados / PEA) × 100
```

### Variables EPH Importantes

| Variable | Descripción |
|----------|-------------|
| `CODUSU` | Código de vivienda |
| `ANO4` | Año de la encuesta |
| `TRIMESTRE` | Trimestre (1-4) |
| `AGLOMERADO` | Código de aglomerado |
| `CH04` | Sexo (1=Varón, 2=Mujer) |
| `CH06` | Edad |
| `NIVEL_ED` | Nivel educativo |
| `ESTADO` | Condición de actividad |
| `P21` | Ingreso ocupación principal |
| `PONDERA` | Factor de expansión |

---

## 💡 Tips y Buenas Prácticas

### Gestión de Datos
- ✅ Usar `.parquet` para archivos grandes (más rápido que CSV)
- ✅ Guardar checkpoints después de cada notebook
- ✅ Verificar datos antes de análisis (`.head()`, `.info()`)

### Visualización
- ✅ Usar títulos descriptivos en gráficos
- ✅ Incluir unidades en ejes (%, $, etc.)
- ✅ Guardar gráficos en alta resolución (dpi=300)
- ✅ Usar paletas de colores consistentes

### Modelado
- ✅ Dividir datos en train/test (80/20)
- ✅ Estandarizar variables antes de regresión
- ✅ Evaluar múltiples modelos
- ✅ Interpretar coeficientes/importancias

### Documentación
- ✅ Comentar código complejo
- ✅ Explicar decisiones metodológicas
- ✅ Documentar fuentes de datos
- ✅ Incluir limitaciones del análisis

---

## 📞 Ayuda Adicional

### Recursos Útiles
- **INDEC - EPH**: https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/
- **Scikit-learn**: https://scikit-learn.org/stable/

### Comunidad
- Stack Overflow (etiqueta: python, pandas, matplotlib)
- GitHub Issues de este proyecto
- Foros de análisis de datos

---

**¡Éxito con tu análisis! 🎉**

*Última actualización: Noviembre 2025*
