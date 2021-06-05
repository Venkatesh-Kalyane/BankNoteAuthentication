import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction= classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():

    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bank Note Authentication ML App</h1> 
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    variance= st.text_input("Varience", "Enter Positive or Negative Value")
    skewness = st.text_input("Skewness", "Enter Positive or Negative Value")
    curtosis = st.text_input("Curtosis", "Enter Positive or Negative Value")
    entropy = st.text_input("Entropy", "Enter Positive or Negative Value")
    result=""

    if st.button("Predict"):
        result= predict_note_authentication(variance, skewness, curtosis, entropy)

    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn....")
        st.text("App Built By Venkatesh Kalyane")

if __name__ == '__main__':
    main()


