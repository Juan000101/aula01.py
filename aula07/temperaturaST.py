import streamlit as st

# Function definitions remain correct
def Celsius_Fahrenheit(t):
        return (t * 1.8) + 32
def Celsius_Kelvin(t):
        return t + 273.15
def F_Celsius(t):
        return (t - 32) * 5/9
def F_Kelvin(t):
        # Corrected: Use the F_Celsius result to get Kelvin
        return F_Celsius(t) + 273.15
def K_Celsius(t):
        return t - 273.15
def K_Fahrenheit(t):
        # Corrected: Use the K_Celsius result to get Fahrenheit
        return Celsius_Fahrenheit(K_Celsius(t))

# Streamlit UI elements
st.sidebar.title("Conversor de temperatura")
st.title("Conversor de temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")

# Using radio buttons for single selection
# The previous checkbox logic was commented out, which is good.
opcao_selecionada = st.sidebar.radio(options=['Celsius', 'Kelvin', 'Fahrenheit'], key="opcao_radio", label="Selecionar unidade de origem")

# Input field
temp = st.number_input("Valor da temperatura", format="%.2f", step=1.0)

# Process data
if st.button("Converter", icon="🌡️"):
    if opcao_selecionada == "Celsius":
        st.write(f"{temp}°C em Fahrenheit: {Celsius_Fahrenheit(temp):.2f}°F")
        st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp):.2f}K")
    elif opcao_selecionada == "Fahrenheit":
        # Corrected logic: user enters Fahrenheit, converts to Celsius and Kelvin
        st.write(f"{temp}°F em Celsius: {F_Celsius(temp):.2f}°C")
        st.write(f"{temp}°F em Kelvin: {F_Kelvin(temp):.2f}K")
    elif opcao_selecionada == "Kelvin":
        # Corrected logic: user enters Kelvin, converts to Celsius and Fahrenheit
        st.write(f"{temp} K em Celsius: {K_Celsius(temp):.2f}°C")
        st.write(f"{temp} K em Fahrenheit: {K_Fahrenheit(temp):.2f}°F")

