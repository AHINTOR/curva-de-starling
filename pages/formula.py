import streamlit as st
import patient_equations as eq
import matplotlib.pyplot as plt

st.subheader("1. Datos del Paciente")

# Add sidebar:
with st.sidebar:
  st.markdown("# Instrucciones: #")
  #st.divider()  # 👈 Draws a horizontal rule
  st.markdown("## Sección 1 ##")
  st.markdown("- Completar con las variables del paciente.")
  st.markdown("## Sección 2 ##")
  st.markdown("- Aquí se muestran los calculos realizados y la grafica de Frank Starling.")
  st.markdown("- Se muestra con un punto :red[rojo] la ubicación del paciente.")

# Dividir la app en dos columnas
col1, col2, col3 = st.columns([1,1,1])

# Columna 1: Datos a llenar
with col1:
        age = st.number_input("Edad", value=75)
        sbp = st.number_input("Presión arterial sistólica (SBP)", value=92)
        dbp = st.number_input("Presión arterial diastólica (DBP)", value=58)

      

# Columna 2:
with col2:
        bsa = st.number_input("Área de superficie corporal (BSA)", value=1.7)
        SaO2 = st.number_input("Saturación arterial de oxígeno (SaO2)", value=100)
        SvO2 = st.number_input("Saturación venosa de oxígeno (SvO2)", value=65)

# Columna 3:
with col3:
        hgb = st.number_input("Hemoglobina (Hgb)", value=8.5)
        ef = st.number_input("Fracción de eyección (EF)", value=55)
        hr = st.number_input("Frecuencia cardíaca (HR)", value=80)

st.divider()  # 👈 Draws a horizontal rule

      # Cálculos basados en las ecuaciones del archivo patient_equations.py
co = eq.co_fick_calc(age, bsa, SaO2, SvO2, hgb)
lvedp = ((0.54 * eq.map_calc(sbp, dbp)) * (ef / 100)) - 2.23
sv = eq.sv_calc(co, hr)

      # Mostrar los resultados calculados debajo del gráfico
st.subheader("2. Resultados Calculados")
st.write(f"Gasto Cardíaco (CO): {co:.2f} L/min")
st.write(f"Volumen Sistólico (SV): {sv:.2f} mL")
st.write(f"Presión al final de la diástole (LVEDP): {lvedp:.2f} mmHg")

  # Función principal para generar la curva de Starling

#st.subheader("Curva de Starling Calculada")

#def main():
x = [0, 8, 10, 15, 20, 25, 25.2, 30, 35]  # Curva normal estimada de Starling
y = [0, 50, 60, 80, 90, 91, 90, 88, 84]
          
          # Crear el gráfico
fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(lvedp, sv, color="red")  # Punto del paciente en la curva
ax.set_xlabel("LVEDP (a través de ecuación)")
ax.set_ylabel("Volumen Sistólico")
ax.set_title("Curva de Starling")
          
          # Mostrar el gráfico en Streamlit
st.pyplot(fig)

  # Ejecutar la aplicación
if __name__ == "__main__":
    main()