# 🛰️ ChronoLogistics - Dashboard de Crisis

**Proyecto académico** desarrollado en **Python + Streamlit** como respuesta al memorando interno de ChronoLogistics.  
El objetivo es construir un **Dashboard Operativo en VIVO** para monitorizar riesgos, explorar escenarios estratégicos y consultar protocolos de crisis en tiempo real.  

---

## 📋 Descripción del Proyecto

Este dashboard actúa como **centro de mando y control** en situaciones de crisis.  
Ofrece tres secciones principales:

1. **Precog: Monitor de Riesgo Táctico**  
   - Visualización de un mapa de clústeres de riesgo.  
   - Simulador interactivo con sliders de velocidad del viento e intensidad de la lluvia.  
   - Cálculo en tiempo real del **Nivel de Riesgo en Cascada** (BAJO, MEDIO, ALTO).

2. **Chronos: Visión Estratégica 2040**  
   - Selector de estrategia entre **Fortaleza Verde** y **Búnker Tecnológico**.  
   - Visualización de imágenes de escenarios futuros.  
   - Argumentación estratégica para la junta directiva e inversores.

3. **K-Lang: Manual de Batalla Interactivo**  
   - Consulta de protocolos: **VÍSPERA**, **CÓDIGO ROJO** y **RENACIMIENTO**.  
   - Simulador en tiempo real con datos de viento e inundación.  
   - Indicador automático del protocolo activo según condiciones simuladas.

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.9+**
- [Streamlit](https://streamlit.io) – para la interfaz web.
- Imágenes generadas o predefinidas para ilustrar mapas y escenarios.

---

## 📂 Estructura del Proyecto

```bash
ChronoLogistics-Dashboard/
├── app.py                  # Código principal del dashboard
├── requirements.txt        # Dependencias del proyecto
├── images/                 # Carpeta con imágenes usadas en el dashboard
│   ├── mapa_clusters.jpg
│   ├── fortaleza_verde.webp
│   └── bunker_tecnologico.webp
└── README.md               # Este archivo
```

---

## 🚀 Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/usuario/ChronoLogistics-Dashboard.git
   cd ChronoLogistics-Dashboard
   ```

2. **Crea un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**:
   ```bash
   streamlit run app.py
   ```

5. Abre en tu navegador:  
   👉 http://localhost:8501

---

## 🌍 Despliegue

El proyecto puede desplegarse fácilmente en:

- **Streamlit Community Cloud**
- **Hugging Face Spaces**
- **Heroku** u otros servicios compatibles con Python.

---

## 📖 Ejemplo de Uso

- Ajusta los sliders en la pestaña **Precog** para simular condiciones meteorológicas extremas y observar cómo varía el nivel de riesgo.
- Cambia entre las estrategias de **Fortaleza Verde** y **Búnker Tecnológico** para explorar distintos futuros posibles de Madrid.
- Simula un aumento del viento a 95 km/h en la pestaña **K-Lang** y observa cómo se activa automáticamente el protocolo **CÓDIGO ROJO: TITÁN**.

---

## 🧑‍💻 Autor

Proyecto realizado por **Álvaro** y **Nicolás** como parte de un ejercicio práctico de ingeniería informática.  
Inspirado en el memorando ficticio de **ChronoLogistics** para la gestión de crisis.

---

## Streamlit

Enlace de la app en Streamlit: https://dashboard-de-mando-oemtjuaawfmumcwfkegrtp.streamlit.app