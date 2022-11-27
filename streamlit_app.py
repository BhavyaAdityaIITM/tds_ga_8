import streamlit as st
import pickle
import pandas as pd

st.write('Program For Multiplication of 2 Numbers')

st.header('User Input Parameters')

def user_input():
  num1 = st.number_input('Enter the 1st number')
  num2 = st.number_input('Enter the 2nd number')
  
  inp = [num1, num2]
  ans = num1*num2
  
  return ans

df = user_input()
st.write(df)

#ans = df[0]*df[1
         
