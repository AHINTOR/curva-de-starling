import streamlit as st
import patient_equations as eq
import matplotlib.pyplot as plt

st.markdown("## Problemática:")
st.markdown("En la medicina clínica, el monitoreo preciso de estos parámetros es esencial para guiar la gestión de líquidos y fármacos inotrópicos en pacientes críticos, especialmente en aquellos con insuficiencia cardíaca o problemas hemodinámicos. La curva de Frank-Starling describe cómo el corazón se adapta al aumento de volumen diastólico para optimizar el gasto cardíaco, pero la medición directa de estos parámetros a menudo requiere procedimientos invasivos como la colocación de catéteres en el corazón (catéter de arteria pulmonar, catéter venoso central), lo que puede aumentar los riesgos para el paciente.")
st.markdown("Durante las sesiones de clase cuando se toca los temas de monitoreo hemodinamico y manejo de paciente crítico, se da la necesidad de tener herramientas para la simulación de situaciones clinicas sonde se deben tomar medidas en base a los calculos hemodinamicos ralizados en los pacientes. Esto genera la necesidad de crear simuladores para la toma de desiciones en entornos seguros.")
col1, col2 = st.columns([2,1])
with col1:
        st.image("images/cfs.png", caption="Curva de Frank Starling")
with col2:
        st.image("images/FS.jpeg", caption="Bucle P-V ventriculo izquierdo")

st.markdown("## Justificación de la aplicación:")
st.markdown("Esta aplicación busca proporcionar una alternativa no invasiva para calcular estos parámetros y ubicarlos en la curva de Frank-Starling, usando métodos indirectos como el cálculo del CO por el método de Fick modificado y la estimación de LVEDP con la ecuación publicada por Abd-El-Aziz. De esta manera, los clínicos podrán obtener una visión aproximada del estado hemodinámico del paciente sin necesidad de procedimientos invasivos, lo que puede reducir complicaciones y permitir una respuesta más rápida en el manejo clínico.")
st.markdown("## Aplicación:")
st.markdown("La aplicación está diseñada para calcular de forma automática los parámetros clave y graficar la posición del paciente en la curva de Frank-Starling, facilitando la interpretación rápida por parte de los médicos. Con estos cálculos, se puede ajustar el tratamiento del paciente con más precisión, ayudando a decidir si es necesario administrar líquidos o apoyo inotrópico. ")
st.markdown("La fórmula para determinar el LVEDP usada para es app es la siguiente (Abd-El-Aziz, 2012)")
st.latex(r'''
        LVEDP = 
        [0.54 x MABP x (1-EF)]-2.23
        ''')
st.markdown("Para el cálculo del gasto cardiaco se usa el método de Fick, donde la VO2 depende de la edad y la superficie corporal.")
st.latex(r'''
        GC =
        \frac{VO_2}{C(a-v)O_2}
        ''')
st.markdown("De esta forma, la aplicación tiene un gran potencial para mejorar la atención de pacientes críticos, optimizando los recursos disponibles y reduciendo el riesgo asociado a procedimientos invasivos.")

st.image("images/starling.png", caption="resultado de la app")
