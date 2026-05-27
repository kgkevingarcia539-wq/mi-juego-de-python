import streamlit as st
import google.generativeai as genai

# 1. Configuración de seguridad (API Key desde secretos locales)
try:
    gemini_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=gemini_key)
except Exception:
    st.error("🔑 ¡Falta la API Key! Configúrala en tu archivo .streamlit/secrets.toml")
    st.stop()

# 2. Configuración de la interfaz de la página
st.set_page_config(page_title="Traductor Secreto IA", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ ¡Traductor de Idiomas Secretos con IA!")
st.write("Escribe mensajes cifrados y compártelos con tus amigos.")

# 3. Menú lateral con opciones de idiomas
st.sidebar.header("⚙️ Configuración")
idioma_secreto = st.sidebar.selectbox(
    "Elige tu idioma secreto:",
    ["Código Alienígena", "Idioma Pirata Avanzado", "Élfico Mágico", "Idioma Robot", "Idioma del Revés"]
)

# 4. Pestañas de la aplicación
pestaña1, pestaña2 = st.tabs(["🔒 Cifrar (Español ➡️ Secreto)", "🔓 Descifrar (Secreto ➡️ Español)"])

# --- PESTAÑA 1: CIFRAR ---
with pestaña1:
    st.subheader("Escribe tu mensaje para ocultar")
    mensaje_humano = st.text_area("Mensaje en español:", "Hola amigo, nos vemos en el parque a las cinco.", key="txt_humano")
    
    if st.button("✨ Cifrar Mensaje", key="btn_cifrar"):
        with st.spinner("🤖 Codificando mensaje con la IA..."):
            try:
                prompt_cifrar = f"""
                Actúa como un traductor experto en lenguajes secretos.
                Traduce el siguiente texto en español al idioma secreto: "{idioma_secreto}".
                Devuelve ÚNICAMENTE el texto traducido final, sin introducciones ni explicaciones de ningún tipo.
                
                Texto a traducir: {mensaje_humano}
                """
                
                model = genai.GenerativeModel("gemini-1.5-flash")
                respuesta = model.generate_content(prompt_cifrar)
                
                st.success("🔒 ¡Mensaje Cifrado con Éxito!")
                st.code(respuesta.text, language="text")
                st.caption("📋 Haz clic en el icono de copiar del cuadro gris para compartirlo.")
                
            except Exception as e:
                st.error(f"Hubo un error al conectar con Gemini: {e}")

# --- PESTAÑA 2: DESCIFRAR ---
with pestaña2:
    st.subheader("Descifra un código recibido")
    mensaje_oculto = st.text_area("Pega el mensaje secreto aquí:", "", key="txt_oculto")
    
    if st.button("🔑 Descifrar Mensaje", key="btn_descifrar"):
        if not mensaje_oculto.strip():
            st.warning("⚠️ Por favor, pega un mensaje primero.")
        else:
            with st.spinner("🧠 Descifrando código..."):
                try:
                    prompt_descifrar = f"""
                    Actúa como un descifrador de códigos profesional.
                    Te van a dar un mensaje escrito en el idioma secreto: "{idioma_secreto}".
                    Tradúcelo de vuelta a un español perfecto, natural y claro.
                    Devuelve ÚNICAMENTE el texto en español traducido, sin introducciones.
                    
                    Texto secreto a descifrar: {mensaje_oculto}
                    """
                    
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    respuesta = model.generate_content(prompt_descifrar)
                    
                    st.success("🔓 ¡Mensaje Descifrado!")
                    st.info(respuesta.text)
                    
                except Exception as e:
                    st.error(f"Hubo un error al descifrar: {e}")
