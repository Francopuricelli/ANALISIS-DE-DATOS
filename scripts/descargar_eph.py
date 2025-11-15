"""
Script para descargar los microdatos de la EPH (Encuesta Permanente de Hogares)
del INDEC para el período 2016-2025.

Autor: Equipo de Análisis
Fecha: Noviembre 2025
"""

import requests
import os
from pathlib import Path
import zipfile
import pandas as pd
from typing import List, Tuple


class DescargadorEPH:
    """Clase para descargar y organizar los datos de EPH del INDEC"""
    
    def __init__(self, directorio_destino: str = "../datos/raw"):
        """
        Inicializa el descargador de EPH
        
        Args:
            directorio_destino: Ruta donde se guardarán los archivos descargados
        """
        self.directorio_destino = Path(directorio_destino)
        self.directorio_destino.mkdir(parents=True, exist_ok=True)
        
        # URL base del INDEC para microdatos EPH
        self.url_base = "https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph"
        
    def generar_urls_trimestres(self, anio_inicio: int = 2016, anio_fin: int = 2025) -> List[Tuple[int, int, str]]:
        """
        Genera las URLs de descarga para cada trimestre
        
        Args:
            anio_inicio: Año inicial del período
            anio_fin: Año final del período
            
        Returns:
            Lista de tuplas (año, trimestre, url)
        """
        urls = []
        trimestres = [1, 2, 3, 4]
        
        for anio in range(anio_inicio, anio_fin + 1):
            for trimestre in trimestres:
                # Formato típico: EPH_usu_1_Trim_2016_txt.zip
                nombre_archivo = f"EPH_usu_{trimestre}_Trim_{anio}_txt.zip"
                url = f"{self.url_base}/{nombre_archivo}"
                urls.append((anio, trimestre, url))
                
        return urls
    
    def descargar_archivo(self, url: str, anio: int, trimestre: int) -> bool:
        """
        Descarga un archivo ZIP de EPH
        
        Args:
            url: URL del archivo a descargar
            anio: Año del dato
            trimestre: Trimestre del dato
            
        Returns:
            True si la descarga fue exitosa, False en caso contrario
        """
        nombre_archivo = f"EPH_{anio}_T{trimestre}.zip"
        ruta_destino = self.directorio_destino / nombre_archivo
        
        # Si el archivo ya existe, no lo descarga
        if ruta_destino.exists():
            print(f"✓ El archivo {nombre_archivo} ya existe. Saltando descarga.")
            return True
        
        try:
            print(f"Descargando: {anio} - Trimestre {trimestre}...", end=" ")
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                with open(ruta_destino, 'wb') as f:
                    f.write(response.content)
                print("✓")
                return True
            else:
                print(f"✗ (Error {response.status_code})")
                return False
                
        except Exception as e:
            print(f"✗ (Error: {str(e)})")
            return False
    
    def extraer_archivos(self, archivo_zip: Path) -> bool:
        """
        Extrae los archivos de un ZIP
        
        Args:
            archivo_zip: Ruta al archivo ZIP
            
        Returns:
            True si la extracción fue exitosa
        """
        try:
            directorio_extraccion = self.directorio_destino / archivo_zip.stem
            directorio_extraccion.mkdir(exist_ok=True)
            
            with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
                zip_ref.extractall(directorio_extraccion)
            
            print(f"  Extraído: {archivo_zip.name}")
            return True
            
        except Exception as e:
            print(f"  Error al extraer {archivo_zip.name}: {str(e)}")
            return False
    
    def descargar_todo(self, anio_inicio: int = 2016, anio_fin: int = 2025, 
                       extraer: bool = True):
        """
        Descarga todos los archivos de EPH para el período especificado
        
        Args:
            anio_inicio: Año inicial
            anio_fin: Año final
            extraer: Si True, extrae los archivos ZIP descargados
        """
        print(f"\n{'='*60}")
        print(f"DESCARGA DE DATOS EPH ({anio_inicio}-{anio_fin})")
        print(f"{'='*60}\n")
        
        urls = self.generar_urls_trimestres(anio_inicio, anio_fin)
        
        exitosos = 0
        fallidos = 0
        
        for anio, trimestre, url in urls:
            if self.descargar_archivo(url, anio, trimestre):
                exitosos += 1
            else:
                fallidos += 1
        
        print(f"\n{'='*60}")
        print(f"Resumen de descarga:")
        print(f"  ✓ Exitosos: {exitosos}")
        print(f"  ✗ Fallidos: {fallidos}")
        print(f"{'='*60}\n")
        
        # Extraer archivos si se solicitó
        if extraer:
            print("Extrayendo archivos...")
            archivos_zip = list(self.directorio_destino.glob("*.zip"))
            for archivo_zip in archivos_zip:
                self.extraer_archivos(archivo_zip)
            print("Extracción completada.\n")
    
    def listar_archivos_descargados(self) -> pd.DataFrame:
        """
        Lista los archivos descargados en formato DataFrame
        
        Returns:
            DataFrame con información de archivos descargados
        """
        archivos = []
        
        for archivo in self.directorio_destino.glob("*.zip"):
            tamanio_mb = archivo.stat().st_size / (1024 * 1024)
            archivos.append({
                'archivo': archivo.name,
                'tamanio_mb': round(tamanio_mb, 2)
            })
        
        df = pd.DataFrame(archivos)
        return df.sort_values('archivo') if not df.empty else df


def main():
    """Función principal para ejecutar la descarga"""
    # Crear descargador
    descargador = DescargadorEPH(directorio_destino="../datos/raw")
    
    # Descargar datos de 2016 a 2025
    descargador.descargar_todo(anio_inicio=2016, anio_fin=2025, extraer=True)
    
    # Mostrar resumen
    print("\nArchivos descargados:")
    df_archivos = descargador.listar_archivos_descargados()
    if not df_archivos.empty:
        print(df_archivos.to_string(index=False))
        print(f"\nTotal: {len(df_archivos)} archivos")
        print(f"Tamaño total: {df_archivos['tamanio_mb'].sum():.2f} MB")
    else:
        print("No se encontraron archivos descargados.")


if __name__ == "__main__":
    print("=" * 70)
    print("DESCARGADOR DE DATOS EPH - INDEC")
    print("=" * 70)
    
    # Usar ruta absoluta desde el script
    script_dir = Path(__file__).parent
    datos_dir = script_dir.parent / "datos" / "raw"
    descargador = DescargadorEPH(directorio_destino=str(datos_dir))
    
    # Descargar todos los trimestres disponibles
    print("\nDescargando datos EPH (2016-2025)...")
    print("Esto puede tomar varios minutos dependiendo de tu conexión.\n")
    
    descargador.descargar_todo()
    
    print("\n" + "=" * 70)
    print("DESCARGA COMPLETADA")
    print("=" * 70)
    print(f"\nLos datos EPH se descargaron en: {descargador.directorio_destino}")
    print("Ahora puedes ejecutar los notebooks en la carpeta 'notebooks/'.")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
