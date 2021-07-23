import streamlit as st
import pandas as pd
import pickle
import sklearn

age = 0 
g = 0
cp = 0
rest_bp = 0
chol = 0
max_heart_rate = 0

with st.form("Enter the details below",clear_on_submit=True):
	col1, col2, col3 = st.beta_columns([1,3,1])
	with col2:
		st.title("**Heart Attack Prediction App**")

	st.subheader("Enter Age")
	age = st.slider(label="Drag the Slider Below",min_value=0,max_value=110)

	st.subheader("Enter Gender")
	gender = st.radio(label="",options=("Female","Male"))

	st.subheader("Enter Chest Pain Type")
	chest_pain = st.selectbox(label="Select Below",options=("Typical Angina","Atypical Angina","Non-Angina Pain","Asymptomatic"))


	st.subheader("Enter Resting Blood Pressure")
	rest_bp = st.text_input(label="Enter Value")


	st.subheader("Enter Cholestrol Level")
	chol = st.text_input(key="restbp",label="Enter Value")

	global submitted
	submitted = st.form_submit_button("Submit")


max_heart_rate = 220 - age;
cp,g = 0,0
if chest_pain == "Typical Angina":
	cp = 0
elif chest_pain == "ATypical Angina":
	cp = 1
elif chest_pain == "Non-Angina Pain":
	cp = 2
else:
	cp = 3

if gender == "Male":
	g = 1
else:
	g = 0


if submitted:
	data = [[age,g,cp,rest_bp,chol,max_heart_rate]]
	X = pd.DataFrame(data,columns=['age','gender','chest pain','blood pressure','cholestrol level','max heart rate'])
	pickle_in = open('finalized_model2.pkl', 'rb') 
	model = pickle.load(pickle_in)
	result = model.predict(X)

	col1, col2, col3 = st.beta_columns([1,3,1])
	with col2:
		if result == 1:
			st.header("You have a risk of experiencing a **heart attack**. Consult a doctor immediately")
		else:
			st.header("No risk of heart attack")





