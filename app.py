import streamlit as st

st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide")
st.title("ChronoLogistics - Dashboard de Crisis")

# FUNCIONES
def predecir_riesgo(velocidad, lluvia): # Simulación simple de riesgo
    riesgo = min(100, velocidad * 0.5 + lluvia * 1.2)
    return riesgo

def protocolo_activo(viento, inundacion): # Determina protocolo activo
    if viento > 90 or inundacion > 80:
        return "CÓDIGO ROJO: TITÁN"
    elif viento > 50 or inundacion > 40:
        return "VÍSPERA: ALERTA"
    else:
        return "RENACIMIENTO: ESTABLE"

# ========== MENU
menu = st.sidebar.radio("Ir a:", ["Precog: Riesgo", "Chronos: Estrategia", "K-Lang: Protocolos"])

# ========== PRECOG

if menu == "Precog: Riesgo":
    st.header("Precog - Monitor de Riesgo Táctico")
    
    # Mapa
    st.image("images/mapa_clusters.jpg", caption="Mapa de Clústeres de Riesgo")
    
    # Simulador
    velocidad = st.slider("Velocidad Media del Viento (km/h)", 0, 200, 50)
    lluvia = st.slider("Intensidad de la Lluvia (mm/h)", 0, 200, 30)
    
    # Riesgo
    riesgo = predecir_riesgo(velocidad, lluvia)
    st.metric("Nivel de Riesgo en Cascada", f"{riesgo:.1f}% - {'ALTO' if riesgo>70 else 'MEDIO' if riesgo>40 else 'BAJO'}")


# ========== Chronos

elif menu == "Chronos: Estrategia":
    st.header("Chronos - Visión Estratégica 2040")
    
    # Estrategia
    estrategia = st.selectbox("Selecciona Estrategia", ["Fortaleza Verde", "Búnker Tecnológico"])
    
    if estrategia == "Fortaleza Verde":
        st.image("images/fortaleza_verde.webp", caption="Visión: Fortaleza Verde")
        st.write("Defensa: Una ciudad sostenible y resiliente para el futuro de Madrid.")
    else:
        st.image("images/bunker_tecnologico.webp", caption="Visión: Búnker Tecnológico")
        st.write("Defensa: Madrid como bastión tecnológico blindado y seguro.")

# ========== K-Lang

elif menu == "K-Lang: Protocolos":
    st.header("K-Lang: Manual de Batalla Interactivo")

    # Selector de protocolos
    st.subheader("Selector de Protocolos")
    protocolos = {
        "VÍSPERA": {
            "Disparador": "Condiciones meteorológicas leves pero inestables.",
            "Acciones": "- Activar monitoreo reforzado\n- Preparar equipo en alerta temprana\n- Revisar comunicaciones"
        },
        "CÓDIGO ROJO": {
            "Disparador": "Tormenta intensa, vientos > 90 km/h o inundación grave.",
            "Acciones": "- Evacuación parcial\n- Activar escudos logísticos\n- Suspender rutas críticas"
        },
        "RENACIMIENTO": {
            "Disparador": "Tras la crisis, fase de recuperación.",
            "Acciones": "- Reactivar infraestructuras\n- Evaluar daños\n- Iniciar protocolos de reconstrucción"
        }
    }

    protocolo_sel = st.selectbox("Elige un protocolo", list(protocolos.keys()))
    st.write(f"**Disparador:** {protocolos[protocolo_sel]['Disparador']}")
    st.write(f"**Acciones:**\n{protocolos[protocolo_sel]['Acciones']}")

    # Simulador
    st.subheader("Simulador de Protocolos en tiempo real")
    viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 20)
    agua = st.slider("Nivel de Inundación (cm)", 0, 200, 0)


    # Lógica protocolos
    if viento > 90 or agua > 100:
        protocolo_activo = "CÓDIGO ROJO"
        color = "red"
    elif viento > 40 or agua > 30:
        protocolo_activo = "VÍSPERA"
        color = "orange"
    else:
        protocolo_activo = "RENACIMIENTO"
        color = "green"

    # Resultado
    st.markdown(
        f"<h2 style='color:{color};'>PROTOCOLO ACTIVO: {protocolo_activo}</h2>",
        unsafe_allow_html=True
    )