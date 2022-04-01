st.title ('Calculadora de Índice de Masa Corporal IMC')
st.header('''
Introduccion:
El sobrepeso puede causar la elevación de la concentración de colesterol total y de la presión arterial, y aumentar el riesgo de sufrir la enfermedad arterial coronaria. La obesidad
aumenta las probabilidades de que se presenten otros factores de riesgo cardiovascular, en
especial, presión arterial alta, colesterol elevado y diabetes.''')
st.image('https://significado.com/img/ciencia/indice-masa-corporal.jpg')
st.latex(r''' IMC = \frac{peso}{estatura^2} ''')
peso = st.number_input('Escribe el peso en Kg',50)
st.write(peso) 
estatura = st.number_input('Escribe la estatura en metros',1.6)
st.write(estatura) 
imc = peso/estatura**2 
imc = round(imc,3)
cal=st.button('Calcular')
st.write(cal)
if cal==True:
    st.write('# El IMC es:',imc,'kg/m2')
