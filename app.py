import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Tytuł aplikacji, inspirowany książką
st.title("QuantumPerformansApp: Fizyka XXI Wieku w Akcji")
st.markdown("""
Witaj w interaktywnej aplikacji opartej na książce Krystiana Defera "Fizyka XXI Wieku: Performans". 
Eksploruj kwantową tajemnicę i świadome tworzenie rzeczywistości!
""")

# Moduł Edukacyjny: Podsumowania rozdziałów
st.header("Moduł Edukacyjny: Kluczowe Koncepcje z Książki")
chapter = st.selectbox("Wybierz rozdział:", [
    "Kryzys Materialistycznego Światopoglądu",
    "Splątanie Intencjonalne",
    "Algorytm Kamienia Filozoficznego",
    "Zastosowania w Życiu Codziennym"
])
if chapter == "Splątanie Intencjonalne":
    st.write("Splątanie intencjonalne to zjawisko, gdzie świadoma intencja tworzy korelacje kwantowe między obserwatorem a obiektem. Nawiązuje do mechanizmu nielokalnego wpływu świadomości na odległe układy fizyczne.")

# Moduł Symulacyjny: Symulacja kolapsu funkcji falowej
st.header("Moduł Symulacyjny: Wpływ Intencji na Kwantowy Układ")
st.write("Symuluj kolaps funkcji falowej pod wpływem 'intencji'. Wybierz siłę intencji (0-1), a zobaczysz zmianę w rozkładzie probabilistycznym.")

intensity = st.slider("Siła Intencji (wpływ świadomości):", 0.0, 1.0, 0.5)

# Symulacja prostego układu kwantowego (superpozycja)
x = np.linspace(-5, 5, 1000)
wave_function = np.exp(-x**2 / 2) * np.cos(5 * x)  # Przykładowa funkcja falowa
collapsed = wave_function * (1 + intensity * np.sin(10 * x))  # "Kolaps" pod wpływem intencji

fig, ax = plt.subplots()
ax.plot(x, np.abs(wave_function)**2, label="Przed Kolapsem (Superpozycja)")
ax.plot(x, np.abs(collapsed)**2, label="Po Kolapsie (z Intencją)")
ax.legend()
ax.set_title("Symulacja Kwantowego Kolapsu")
st.pyplot(fig)

# Moduł Praktyczny: Generator Afirmacji
st.header("Moduł Praktyczny: Świadome Tworzenie")
intention = st.text_input("Wpisz swoją intencję (np. 'Zdrowie i obfitość'):")
if st.button("Generuj Afirmację"):
    affirmation = f"Moja intencja '{intention}' manifestuje się w rzeczywistości kwantowej zgodnie z Wolą Absolutu."
    st.success(affirmation)

# Przykładowe dane z książki (symulowane)
data = pd.DataFrame({
    "Zjawisko": ["Splątanie", "Superpozycja", "Kolaps"],
    "Prawdopodobieństwo": [0.8, 0.5, intensity]
})
st.table(data)

st.markdown("Aplikacja stworzona w Pythonie z użyciem Streamlit. Eksperymentuj i odkrywaj!")
