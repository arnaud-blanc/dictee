import math
import streamlit as st

st.header('La dictée c\'est :blue[cool] :sunglasses:', divider="rainbow")

words_nb = st.number_input("**Nombre total de mots :**", value=1, min_value=1)


faults_nb = st.number_input("**Nombre total d'erreurs :**", value=0,)

score = (words_nb - faults_nb)/ words_nb
st.write(f"**Pourcentage de réussite** : {score * 100:.2f}%")

notation = st.radio(
    "Note minimale :",
    ["**0**", "**10**",],
    index=None, horizontal=True
)

if notation is None:
    st.write(":red[^^ choisir la note minimale ^^]")

def which_decimal(score: float) -> float:
    decimal_value = score - math.floor(score)
    if decimal_value < 0.3:
        res = 0
    elif decimal_value < 0.8:
        res = 0.5
    else:
        res = 1
    return math.floor(score) + res


if notation == "**0**":
    score = round(score * 20, 1)
elif notation == "**10**":
    score = 10 + score * 10
    score = round(score, 1)

if notation is not None:
    "**résultat réel** :"
    st.write(f"=> {score} / 20")
    "**résultat arrondi** :"
    st.write(f"=> **:red[{which_decimal(score)}]** / 20")
    
    
    

