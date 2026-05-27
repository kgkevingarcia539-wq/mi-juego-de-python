import streamlit as st

# -----------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Idioma Secreto 👽",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------------
# ESTILOS (Ajustado para compatibilidad total)
# -----------------------------------
st.markdown("""
<style>
/* Forzar fondo oscuro global en la app de Streamlit */
.stApp {
    background-color: #0f172a !important;
}

.main {
    background: linear-gradient(180deg, #111827, #1e293b);
    border-radius: 20px;
    padding: 20px;
}

h1 {
    text-align: center;
    color: #38bdf8;
    font-size: 45px;
    font-family: 'Courier New', Courier, monospace;
}

p, span, label {
    color: white !important;
}

.stTextInput > div > div > input {
    background-color: #111827 !important;
    color: white !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 10px;
    padding: 10px;
}

.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #06b6d4, #3b82f6) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 12px !important;
    font-size: 18px !important;
    font-weight: bold !important;
    box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
}

.stButton button:hover {
    transform: scale(1.03);
    transition: 0.2s;
    box-shadow: 0 4px 25px #38bdf8;
}

.resultado {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #22d3ee;
    color: #67e8f9;
    font-size: 22px;
    text-align: center;
    margin-top: 20px;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TÍTULO
# -----------------------------------
st.title("👽 Idioma Secreto")
st.write("Convierte mensajes normales en lenguaje alienígena 🔐")

# -----------------------------------
# DICCIONARIOS CORREGIDOS
# -----------------------------------
# Diccionario para cifrar letra por letra
idioma_cifrar = {
    "a": "za", "e": "xe", "i": "qi", "o": "po", "u": "mu",
    "A": "Za", "E": "Xe", "I": "Qi", "O": "Po", "U": "Mu"
}

# Diccionario inverso ordenado para descifrar sin romper las sílabas
idioma_descifrar = {
    "za": "a", "xe": "e", "qi": "i", "po": "o", "mu": "u",
    "Za": "A", "Xe": "E", "Qi": "I", "Po": "O", "Mu": "U"
}

# -----------------------------------
# FUNCIONES CORREGIDAS
# -----------------------------------
def traducir(texto):
    resultado = ""
    for letra in texto:
        if letra in idioma_cifrar:
            resultado += idioma_cifrar[letra]
        else:
            resultado += letra
    return resultado

def descifrar_mensaje(texto):
    resultado = texto
    # Reemplazamos las sílabas completas en lugar de letras sueltas
    for secreto, normal in idioma_descifrar.items():
        resultado = resultado.replace(secreto, normal)
    return resultado

# -----------------------------------
# ENTRADA DE DATOS
# -----------------------------------
mensaje = st.text_input(
    "✍️ Escribe tu mensaje:",
    placeholder="Hola humano..."
)

# -----------------------------------
# BOTONES E INTERFAZ
# -----------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🔒 Traducir"):
        if mensaje.strip():
            secreto = traducir(mensaje)
            st.markdown(
                f'<div class="resultado">👽 {secreto}</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning("⚠️ Escribe algo primero, terrícola.")

with col2:
    if st.button("🔓 Descifrar"):
        if mensaje.strip():
            normal = descifrar_mensaje(mensaje)
            st.markdown(
                f'<div class="resultado">🧑 {normal}</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning("⚠️ Pega un código alienígena para descifrar.")

# -----------------------------------
# PIE DE PÁGINA
# -----------------------------------
st.write("---")
st.caption("🚀 Proyecto creado con Python + Streamlit")
