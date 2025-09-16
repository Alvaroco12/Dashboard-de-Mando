import streamlit as st
import numpy as np

st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide")
st.title("⚡ ChronoLogistics - Dashboard de Crisis")

# FUNCIONES
def predecir_riesgo(velocidad, lluvia):
    """Calcula un riesgo simulado en % basado en velocidad y lluvia"""
    riesgo = min(100, velocidad * 0.5 + lluvia * 1.2)
    return riesgo

def protocolo_activo(viento, inundacion):
    """Devuelve qué protocolo está activo según condiciones"""
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
        st.write("🌱 Defensa: Una ciudad sostenible y resiliente para el futuro de Madrid.")
    else:
        st.image("images/bunker_tecnologico.webp", caption="Visión: Búnker Tecnológico")
        st.write("🤖 Defensa: Madrid como bastión tecnológico blindado y seguro.")

# ========== K-Lang

elif menu == "K-Lang: Protocolos":
    st.header("K-Lang - Manual de Batalla Interactivo")
    
    # Protocolo
    protocolo = st.selectbox("Selecciona Protocolo", ["VÍSPERA", "CÓDIGO ROJO", "RENACIMIENTO"])
    st.write(f"📋 Ficha Técnica del protocolo {protocolo}")
    
    # Sensores
    viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 30)
    inundacion = st.slider("Nivel de Inundación (cm)", 0, 200, 20)
    
    #Protocolo
    activo = protocolo_activo(viento, inundacion)
    st.subheader(f"🚨 Protocolo Activo: {activo}")
