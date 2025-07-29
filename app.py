import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import sqlite3
from datetime import datetime

# Inicjalizacja bazy danych SQLite
conn = sqlite3.connect('intentions.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS intentions 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, intention TEXT, timestamp TEXT)''')
conn.commit()

# Stylizacja CSS
st.markdown("""
<style>
    .main { background-color: #f0f2f6; padding: 20px; }
    .stButton>button { background-color: #1e90ff; color: white; border-radius: 8px; }
    .stTextInput>label { font-size: 1.1rem; font-weight: bold; }
    .sidebar .sidebar-content { background-color: #e6f3ff; }
</style>
""", unsafe_allow_html=True)

# Tytuł i nagłówek aplikacji
st.title("QuantumPerformansApp: Fizyka XXI Wieku w Akcji")
st.markdown("""
Witaj w rozszerzonej aplikacji inspirowanej książką Krystiana Defera *"Fizyka XXI Wieku: Performans"*.
Eksploruj kwantową tajemnicę, świadome tworzenie i ezofizykę przez interaktywne moduły!
""")

# Sidebar z nawigacją
st.sidebar.header("Nawigacja")
page = st.sidebar.selectbox("Wybierz moduł:", [
    "Edukacja", "Symulacje Kwantowe", "Praktyczne Narzędzia", "Społeczność"
])

# Moduł Edukacyjny
if page == "Edukacja":
    st.header("Moduł Edukacyjny: Kluczowe Koncepcje Ezofizyki")
    chapter = st.selectbox("Wybierz temat:", [
        "Kryzys Materialistycznego Światopoglądu",
        "Splątanie Intencjonalne",
        "Algorytm Kamienia Filozoficznego",
        "Kwantowa Koherencja w Biologii",
        "Zastosowania w Życiu Codziennym"
    ])
    
    chapters_content = {
        "Kryzys Materialistycznego Światopoglądu": {
            "text": "Materializm, dominujący od Oświecenia, nie wyjaśnia paradoksów kwantowych. Ezofizyka oferuje nowy paradygmat łączący naukę i duchowość (str. 11).",
            "image": lambda: plt.figure(figsize=(8, 4), dpi=100, facecolor='white'), plt.plot([0, 1], [0, 1], 'k--', label="Materializm"), plt.plot([0, 1], [1, 0], 'b-', label="Ezofizyka"), plt.legend(), plt.title("Przejście Paradygmatów"), st.pyplot(plt)
        },
        "Splątanie Intencjonalne": {
            "text": "Świadoma intencja może tworzyć korelacje kwantowe między obserwatorem a obiektem, umożliwiając nielokalny wpływ (str. 4, 80).",
            "image": lambda: st.image("https://via.placeholder.com/400x200.png?text=Splątanie+Kwantowe", caption="Ilustracja splątania intencjonalnego")
        },
        "Algorytm Kamienia Filozoficznego": {
            "text": "Algorytm pozwala świadomie manifestować rzeczywistość poprzez wizualizację i intencję (str. 70-74).",
            "image": lambda: st.image("https://via.placeholder.com/400x200.png?text=Algorytm+Manifestacji", caption="Schemat algorytmu Kamienia Filozoficznego")
        },
        "Kwantowa Koherencja w Biologii": {
            "text": "Kwantowa koherencja w mikrotubulach mózgu wspiera procesy świadomości (str. 36, Penrose i Hameroff).",
            "image": lambda: plt.figure(figsize=(8, 4), dpi=100, facecolor='white'), plt.plot(np.sin(np.linspace(0, 10, 100)), label="Koherencja"), plt.title("Kwantowa Koherencja"), plt.legend(), st.pyplot(plt)
        },
        "Zastosowania w Życiu Codziennym": {
            "text": "Ezofizyka znajduje zastosowanie w zdrowiu, relacjach i obfitości, łącząc naukę z praktyką (str. 189).",
            "image": lambda: st.image("https://via.placeholder.com/400x200.png?text=Zastosowania+Ezofizyki", caption="Przykłady praktycznych zastosowań")
        }
    }
    
    st.write(chapters_content[chapter]["text"])
    chapters_content[chapter]["image"]()

# Moduł Symulacyjny
elif page == "Symulacje Kwantowe":
    st.header("Moduł Symulacyjny: Eksperymenty Kwantowe")
    sim_type = st.selectbox("Wybierz symulację:", [
        "Podwójna Szczelina", "Koherencja w Mikrotubulach", "Równanie Schrödingera"
    ])
    
    if sim_type == "Podwójna Szczelina":
        st.write("Symulacja wpływu intencji na wzorzec interferencyjny (str. 56).")
        intensity = st.slider("Siła Intencji:", 0.0, 1.0, 0.5)
        x = np.linspace(-5, 5, 1000)
        wave = np.exp(-x**2 / 2) * np.cos(5 * x)
        collapsed = wave * (1 + intensity * np.sin(10 * x))
        
        fig, ax = plt.subplots(figsize=(8, 4), dpi=100, facecolor='white')
        ax.plot(x, np.abs(wave)**2, label="Przed Kolapsem", color='blue')
        ax.plot(x, np.abs(collapsed)**2, label="Po Kolapsie (Intencja)", color='red')
        ax.legend()
        ax.set_title("Eksperyment z Podwójną Szczeliną")
        st.pyplot(fig)
    
    elif sim_type == "Koherencja w Mikrotubulach":
        st.write("Symulacja koherencji kwantowej w mikrotubulach (str. 36).")
        coherence_time = st.slider("Czas Koherencji (ms):", 0, 100, 50)
        t = np.linspace(0, 100, 1000)
        coherence = np.exp(-t / coherence_time) * np.cos(2 * np.pi * t / 10)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=coherence, mode='lines', name='Koherencja'))
        fig.update_layout(title="Kwantowa Koherencja w Mikrotubulach", xaxis_title="Czas (ms)", yaxis_title="Amplituda")
        st.plotly_chart(fig)
    
    elif sim_type == "Równanie Schrödingera":
        st.write("Wizualizacja funkcji falowej (str. 181).")
        hbar = 1
        m = 1
        x = np.linspace(-5, 5, 1000)
        psi = np.exp(-x**2 / 2) / np.sqrt(np.sqrt(np.pi))  # Funkcja falowa
        V = 0.5 * x**2  # Potencjał harmoniczny
        
        fig, ax = plt.subplots(figsize=(8, 4), dpi=100, facecolor='white')
        ax.plot(x, np.abs(psi)**2, label="Gęstość Prawdopodobieństwa", color='purple')
        ax.plot(x, V, label="Potencjał", color='green', linestyle='--')
        ax.legend()
        ax.set_title("Równanie Schrödingera: Funkcja Falowa")
        st.pyplot(fig)

# Moduł Praktyczny
elif page == "Praktyczne Narzędzia":
    st.header("Moduł Praktyczny: Świadome Tworzenie")
    st.subheader("Generator Afirmacji")
    intention = st.text_input("Wpisz swoją intencję (np. Zdrowie, Obfitość):")
    chakra = st.selectbox("Wybierz czakrę do wizualizacji:", ["Korzenia", "Splotu Słonecznego", "Serca"])
    
    if st.button("Generuj Afirmację"):
        if intention:
            affirmation = f"Moja intencja '{intention}' manifestuje się poprzez energię czakry {chakra.lower()} zgodnie z Wolą Absolutu."
            st.success(affirmation)
            c.execute("INSERT INTO intentions (intention, timestamp) VALUES (?, ?)", 
                     (intention, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
        else:
            st.error("Proszę wpisać intencję!")
    
    st.subheader("Wizualizacja Czakry")
    chakra_colors = {"Korzenia": "Czerwony", "Splotu Słonecznego": "Żółty", "Serca": "Zielony"}
    if chakra:
        st.write(f"Wyobraź sobie {chakra_colors[chakra]} światło emanujące z czakry {chakra.lower()} (str. 75).")
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[1, 1, 1, 1, 1], theta=[0, 72, 144, 216, 288], 
                                     fill='toself', line_color=chakra_colors[chakra]))
        fig.update_layout(title=f"Wizualizacja Czakry {chakra}", polar=dict(radialaxis=dict(visible=False)))
        st.plotly_chart(fig)

# Moduł Społecznościowy
elif page == "Społeczność":
    st.header("Moduł Społecznościowy: Dziel się Intencjami")
    st.write("Zapisz swoją intencję i zobacz inspiracje od innych (str. 146).")
    community_intention = st.text_input("Podziel się swoją intencją:")
    if st.button("Zapisz Intencję"):
        if community_intention:
            c.execute("INSERT INTO intentions (intention, timestamp) VALUES (?, ?)", 
                     (community_intention, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            st.success("Intencja zapisana!")
    
    st.subheader("Inspiracje Społeczności")
    c.execute("SELECT intention, timestamp FROM intentions ORDER BY timestamp DESC LIMIT 5")
    intentions = c.fetchall()
    df = pd.DataFrame(intentions, columns=["Intencja", "Data"])
    st.table(df)

# Stopka
st.markdown("---")
st.markdown("Aplikacja stworzona w Pythonie z użyciem Streamlit. Odkrywaj ezofizykę i manifestuj rzeczywistość!")

# Zamknięcie połączenia z bazą danych
conn.close()import streamlit as st
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
