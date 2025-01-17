import streamlit as st
import subprocess
import os

# Función para descargar el video
def descargar_video_con_audio(url):
    try:
        # Crear carpeta de descargas
        carpeta_descargas = os.path.join(os.getcwd(), "descargas")
        os.makedirs(carpeta_descargas, exist_ok=True)
        salida = os.path.join(carpeta_descargas, "video_descargado.mp4")

        # Mostrar mensaje en Streamlit
        st.info("Iniciando la descarga del mejor video y audio disponibles...")

        # Comando para descargar el video
        comando = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", salida,
            url
        ]

        # Ejecutar el comando
        subprocess.run(comando, check=True, text=True, capture_output=True)

        # Mostrar éxito en Streamlit
        st.success(f"Descarga completada con éxito. Archivo guardado en: {salida}")
        return carpeta_descargas

    except subprocess.CalledProcessError as e:
        st.error(f"Error al ejecutar yt-dlp: {e.stderr}")
    except FileNotFoundError:
        st.error("yt-dlp no está instalado o no es accesible. Instálalo con 'pip install yt-dlp'.")
    except Exception as e:
        st.error(f"Error inesperado: {e}")

    return None

# Interfaz en Streamlit
st.header("Descargar videos de YouTube con Python")

# Inicializar session_state para almacenar la carpeta de descargas
if "carpeta_descargas" not in st.session_state:
    st.session_state.carpeta_descargas = None

# Entrada de la URL
url = st.text_input("Introduce la URL del video de YouTube:")

# Botón para iniciar la descarga
if st.button("Descargar"):
    if url.strip():
        st.session_state.carpeta_descargas = descargar_video_con_audio(url)
    else:
        st.warning("Por favor, introduce una URL válida.")

# Botón para descargar el archivo directamente
if st.button("Descargar archivo"):
    if st.session_state.carpeta_descargas:
        archivo_descargado = os.path.join(st.session_state.carpeta_descargas, "video_descargado.mp4")
        if os.path.exists(archivo_descargado):
            with open(archivo_descargado, "rb") as file:
                st.download_button(
                    label="Descargar video",
                    data=file,
                    file_name="video_descargado.mp4",
                    mime="video/mp4"
                )
        else:
            st.warning("El archivo no está disponible.")
    else:
        st.warning("No hay descargas recientes disponibles.")
