import streamlit as st
import pickle
st.title("Titanic Survival Prediction")

pClass= st.radio("PClass",[1,2,3])
sex= st.radio("Female/Male",[0,1])
age =st.number_input("Age")
sibsp= st.radio("Sibsp",[0,1,2,3])
pArch= st.radio("PArch",[0,1,2])
fare= st.number_input("Fare")



clicked=st.button("Get Prediction")

with open('model.pkl', 'rb') as f:
    model= pickle.load(f)


if clicked==True:
    #predict when button is clicked
    data=[pClass, sex, age, sibsp, pArch, fare]
    print(data)
    pred= model.predict([data])[0] #2D array needed thus use nested list and use the first element

    if pred == 0:
        st.header("Not Survived")
    else:
        st.header("Survived")
