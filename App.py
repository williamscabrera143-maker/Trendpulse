import streamlit as st

# 1. Configuración obligatoria de la página
st.set_page_config(page_title="TrendPulse - Buscador de Tendencias", page_icon="🚀", layout="wide")

# 2. Barra lateral con el sistema de pagos premium
st.sidebar.markdown("### 👑 Desbloquea el Plan Pro")
st.sidebar.write("Accede a más de 100 tendencias diarias y guiones ilimitados.")
st.sidebar.link_button("Hacerme Pro por $9.99/mes 💳", "https://stripe.com")



# 3. Base de datos simulada de tendencias para tus videos
TENDENCIAS = {
    "Finanzas / Emprendimiento": [
        {"audio": "Money Pink Floyd (Phonk Remix)", "crecimiento": "+450%", "hook": "El error de $0 que cometen todos al empezar..."},
        {"audio": "Business Casual Beat", "crecimiento": "+210%", "hook": "3 páginas web que se sienten ilegales de conocer..."}
    ],
    "Estilo de Vida / Motivación": [
        {"audio": "Dark Ambient Synth", "crecimiento": "+380%", "hook": "Si tienes entre 18 y 30 años, deja de hacer esto..."},
        {"audio": "Morning Coffee Lo-Fi", "crecimiento": "+190%", "hook": "Mi rutina de 5 minutos para duplicar la productividad..."}
    ]
}

# 4. Diseño visual de la aplicación
st.title("🔥 TrendPulse: Buscador de Tendencias Faceless")
st.subheader("Encuentra audios virales y guiones generados por IA antes que nadie.")

nicho = st.selectbox("Selecciona tu nicho de contenido:", list(TENDENCIAS.keys()))

if st.button("Buscar Tendencias Secretas 🔍"):
    st.write(f"### 📈 Tendencias detectadas para el nicho: **{nicho}**")
    
    for item in TENDENCIAS[nicho]:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Audio en Tendencia", value=item["audio"])
        with col2:
            st.metric(label="Velocidad de Crecimiento", value=item["crecimiento"], delta="EXPLOSIVO")
        with col3:
            st.info(f"**Gancho Viral Sugerido:** \n\n '{item['hook']}'")
            
    st.success("✨ Consejo anónimo: Graba la pantalla mostrando estos datos para tu próximo video viral.")

