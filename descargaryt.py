import streamlit as st
from pytube import YouTube

# Función para generar el enlace de descarga
def generar_enlace_descarga(url):
    try:
        # Crear objeto YouTube
        yt = YouTube(url)

        # Obtener el stream de mayor resolución
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        # Enlace de descarga
        enlace = stream.url
        return enlace, yt.title

    except Exception as e:
        st.error(f"Error al procesar la URL: {str(e)}")
        return None, None

# Interfaz en Streamlit
st.header("Descargar videos de YouTube con Python")

# Entrada de la URL
url = st.text_input("Introduce la URL del video de YouTube:")

# Botón para generar enlace de descarga
if st.button("Generar enlace de descarga"):
    if url.strip():
        enlace, titulo = generar_enlace_descarga(url)
        if enlace:
            st.success(f"Enlace de descarga generado para: {titulo}")
            st.markdown(f"[Haz clic aquí para descargar el video](<{enlace}>)", unsafe_allow_html=True)
        else:
            st.warning("No se pudo generar el enlace de descarga.")
    else:
        st.warning("Por favor, introduce una URL válida.")
