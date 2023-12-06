from gingerit.gingerit import GingerIt
import streamlit as st

st.title('Grammar & Spell Checker In Python')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
parser = GingerIt()
if st.button('Correct Sentence'):
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        result_dict = parser.parse(text)
        st.markdown('**Corrected Sentence - **' + str(result_dict["result"]))
else: pass

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
tokens=word_tokenize(text)
tag=pos_tag(tokens)
for word,tag in tag:
    st.write("Word:", word, "Tag:", tag)
