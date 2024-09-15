
import streamlit as st
import patient_equations as eq
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Curva de Frank Starling")
st.write("Adaptado por Jorge Quispe")
st.write("Ingresa las siguientes variables:")

# Variables interactivas con Streamlit para que el usuario ingrese los datos
age = st.number_input("Edad", value=75)
sbp = st.number_input("Presión arterial sistólica (SBP)", value=92)
dbp = st.number_input("Presión arterial diastólica (DBP)", value=58)
bsa = st.number_input("Área de superficie corporal (BSA)", value=1.7)
SaO2 = st.number_input("Saturación arterial de oxígeno (SaO2)", value=100)
SvO2 = st.number_input("Saturación venosa de oxígeno (SvO2)", value=65)
hgb = st.number_input("Hemoglobina (Hgb)", value=8.5)
ef = st.number_input("Fracción de eyección (EF)", value=55)
hr = st.number_input("Frecuencia cardíaca (HR)", value=80)

# Cálculos basados en las ecuaciones del archivo patient_equations.py
co = eq.co_fick_calc(age, bsa, SaO2, SvO2, hgb)
lvedp = ((0.54 * eq.map_calc(sbp, dbp)) * (ef / 100)) - 2.23
sv = eq.sv_calc(co, hr)

# Función principal para generar la curva de Starling
def main():
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
