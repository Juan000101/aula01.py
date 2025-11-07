import streamlit as st
def Celsius_Fahrenheit(temp):
    return (temp * 1.8) + 32
def Celsius_Kelvin(temp):
    return temp+273.15
def F_Celsius(t):
    return (t - 32) * 5/9
    def F_Kelvin(t):
        return ((t -32 ) * 5/9 + 273.15
def K_Celsius(t):
    return t - 273.15
def K_Faherenheit(t):
    return Celsius_Fahrenheit(t - 273.15)

#Problema temperatura
st.sidebar.title("Conversor de tempreratura")
st.title("Conversor de tempreratura")
st.sidebar.markdown("Converte a temperaura em Celsius, para Fahrenheit e Kelvin.")
celcius_selecionado = st.sidebar.checkbox("celcius", key="temp_celcius")
fahrenheit_selecionado = st.sidebar.checkbox("fahrenheit", key="temp_fahrenheit")
kelvin_selecionado = st.sidebar.checkbox("kelvin", key="temp_kelvin")
#entrada de dados
temp = st.number_input("Valor da temperatura",format="%.2f",step=1.0)
if celsius_selecionado + fahrenheit_selecionado + kelvin_selecionado > 1:
#processamento de dados
if st.button("converter",icon="🌡"):
    if celcius_selecionado:
        st.write(f"{temp}°C em Fahrenheit: {Celsius_Fahrenheit(temp):.2f}°F")
        st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp):.2f}K")
    elif fahrenheit_selecionado:
        st.write(f"{temp}°F em Celsius: °C")
        st.write(f"{temp}°F em Kelvin: {F_Kelvin(temp):.2f}K")
    elif kelvin_selecionado:
        st.write(f"{temp} K em Celsius: {K_Celsius(temp):.2f}°C")
        st.write(f"{temp} K em Fahrenheit: {K_Faherenheit(temp):.2f}°F"
