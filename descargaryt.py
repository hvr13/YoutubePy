import streamlit as st
import subprocess
import os

# Función para descargar el video
def descargar_video_con_audio(url):
    try:
        # Crear carpeta temporal para almacenar el video
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

        # Verificar si el archivo se descargó correctamente
        if os.path.exists(salida):
            st.success("Descarga completada con éxito.")
            return salida
        else:
            st.error("Hubo un problema al descargar el video.")
            return None

    except subprocess.CalledProcessError as e:
        st.error(f"Error al ejecutar yt-dlp: {e.stderr}")
    except Exception as e:
        st.error(f"Error inesperado: {e}")
    return None


# Interfaz en Streamlit
st.header("Descargar videos de YouTube con Python")

# Entrada de la URL
url = st.text_input("Introduce la URL del video de YouTube:")

# Botón para iniciar la descarga
if st.button("Descargar"):
    if url.strip():
        archivo_descargado = descargar_video_con_audio(url)
        if archivo_descargado:
            with open(archivo_descargado, "rb") as file:
                st.download_button(
                    label="Descargar video",
                    data=file,
                    file_name="video_descargado.mp4",
                    mime="video/mp4"
                )
    else:
        st.warning("Por favor, introduce una URL válida.")
