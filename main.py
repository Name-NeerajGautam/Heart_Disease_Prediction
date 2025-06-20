
import streamlit as st
import pickle
st.subheader('Heart Disease Prediction')
age=st.number_input('Enter Age')
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
exa = st.selectbox('Exercise Induced Angina', [0, 1])
bps=st.number_input('Enter Resting BP/S')
cho=st.number_input('Enter Cholestrol ')
hrt=st.number_input('Enter Heart Rate  ')
olp=st.selectbox('Enter Old Peak',[0.0,1.0,1.5,2.0])
sts=st.selectbox('Enter ST Slope',[1,2])
button=st.button('Predict!')


if button:
    rfc=pickle.load(open('hd.pkl','rb'))
   
    res=rfc.predict([[age,cp,bps,cho,hrt,exa,olp,sts]])[0].round(2)
    st.markdown(f"### The Person is: {' having Heart Disease' if res == 1 else ' free from Heart Disease'}")
    #  for streamlit analysis please visit:-https://heartdiseaseprediction-3xavrtswkwdiwnfvh4tng2.streamlit.app/
    
