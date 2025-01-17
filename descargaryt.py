import streamlit as st
import subprocess
import os
import platform

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
        resultado = subprocess.run(
            comando, check=True, text=True, capture_output=True)

        # Mostrar éxito en Streamlit
        st.success(
            f"Descarga completada con éxito. Archivo guardado en: {salida}")
        return carpeta_descargas

    except subprocess.CalledProcessError as e:
        st.error(f"Error al ejecutar yt-dlp: {e.stderr}")
    except FileNotFoundError:
        st.error(
            "yt-dlp no está instalado o no es accesible. Instálalo con 'pip install yt-dlp'.")
    except Exception as e:
        st.error(f"Error inesperado: {e}")

    return None

# Función para abrir la carpeta de descargas en Windows


def abrir_carpeta(carpeta):
    try:
        if os.path.exists(carpeta):  # Verificar si la carpeta existe
            # Abre la carpeta en el explorador de Windows
            os.startfile(carpeta)
            st.info(f"Abriendo la carpeta: {carpeta}")
        else:
            st.warning(f"La carpeta no existe: {carpeta}")
    except Exception as e:
        st.error(f"No se pudo abrir la carpeta: {e}")


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

# Botón para abrir la carpeta de descargas
if st.button("Abrir carpeta de descargas"):
    if st.session_state.carpeta_descargas:
        abrir_carpeta(st.session_state.carpeta_descargas)
    else:
        st.warning("No hay descargas recientes o la carpeta no está disponible.")