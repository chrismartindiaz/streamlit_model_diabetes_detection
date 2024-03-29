import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("./model/diabetes_model.pkl")

# SideBar
st.sidebar.image("./src/diabetes.png", use_column_width=True)
st.sidebar.image("./src/diabetesdoc.jpg", use_column_width=True)
st.sidebar.image("./src/diabetes3.png", use_column_width=True)

# Content
st.image("./src/diabetesbanner.png")
st.title('Anticípate a la Diabetes!')

col1, col2, col3, col4 = st.columns(4)

with col1:

    age = st.slider('Introduce tu edad:', 18, 65)


    gender = st.selectbox('Introduce tu **sexo**:',
                          ('Masculino', 'Femenino'))
    
    polyuria = st.radio('**Poliuria**: ¿Orinas en grandes cantidades? (+ de 3.5 Litros / Cada vez que se orina)', 
                        ("No", "Sí"))
    

    polydipsia = st.radio('**Polidipsia**: ¿Tienes sed de forma constante?(+ de 3.5 Litros de Agua / Día)',
                        ("No","Sí"))
    
with col2:

    weight_loss = st.radio('**Pérdidas de peso invulontarias**: ¿Has tenido perdidas de peso muy repentinas?',
                        ("No","Sí"))
    weakness = st.radio('**Debilidad**: ¿Sientes fatiga o debilidad en tu día a día?',
                        ("No","Sí"))
    polyphagia = st.radio('**Polifagia**: ¿Tienes ganas de comer constantemente?',
                        ("No","Sí"))
    genital_thrush = st.radio('**Escozor íntimo**: ¿Sientes escozor o irritación en tus partes íntimas?',
                        ("No","Sí"))
    
with col3:
    visual_blurring = st.radio('**Borrosidad visual**: ¿Te cuesta enfocar la vista en ciertas ocasiones?',
                        ("No","Sí"))
    itching = st.radio('**Picores**: ¿Sientes picores de vez en cuando?',
                        ("No","Sí"))
    irritability = st.radio('**Irritabilidad**: ¿Te enfadas por cosas sin importancia?',
                        ("No","Sí"))
    delayed_healing = st.radio('**Cicatrización lenta**: ¿Tardas mucho en cicatrizar una herida o un corte?',
                        ("No","Sí"))
with col4:

    partial_paresis = st.radio('**Fatiga muscular**: ¿Tienes parálisis musculares a menudo?',
                        ("No","Sí"))
    muscle_stiffness = st.radio('**Dolor muscular**: ¿Sientes dolores musculares cada poco?',
                        ("No","Sí"))
    alopecia = st.radio('**Alopecia**: ¿Tienes caída de pelo cada poco tiempo?',
                        ("No","Sí"))
    obesity = st.radio('**Obesidad**: ¿Tienes obesidad?',
                        ("No","Sí"))
    
if st.button('Comprobar'):
    X = pd.DataFrame([[age, gender, polyuria, polydipsia, weight_loss, weakness, polyphagia, genital_thrush, visual_blurring, itching, irritability, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity]], columns=['Age', 'Gender', 'Polyuria','Polydipsia','sudden weight loss','weakness','Polyphagia','Genital thrush','visual blurring','Itching','Irritability','delayed healing','partial paresis','muscle stiffness','Alopecia','Obesity'])
    X = X.replace(['No', 'Sí'], [0, 1])
    X = X.replace(['Masculino', 'Femenino'], [0, 1])
    
    prediction = clf.predict(X)[0]
    
    if prediction == 0:
        prediction = "negativo"
    else:
        prediction = "positivo"
    
    st.text(f"Usted es {prediction} en presentar principios de diabetes")

# End
st.divider()
st.caption('Una idea original de Christian Martín Díaz ©')
