# -*- coding: utf-8 -*-
"""4. Code Generation App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HyMd3G2HdiFqg-DrG7hu5tQMKP2iAHLe

4. **Code Generation App**

**Steps to Run**

Replace YOUR_API_KEY with your OpenAI API key.

Save as code_gen.py.

Run with streamlit run code_gen.py.

Provide a prompt and view the generated code.
"""

# Install dependencies: pip install streamlit openai
import streamlit as st
import openai

# OpenAI API key setup
openai.api_key = "YOUR_API_KEY"

# Streamlit UI
st.title("Code Generator")
st.write("Describe the code you want, and the app will generate it.")

# User input
prompt = st.text_area("Describe your code requirements", height=200)

if st.button("Generate Code"):
    if prompt.strip():
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        st.subheader("Generated Code:")
        st.code(response.choices[0].text.strip())
    else:
        st.warning("Please provide a description.")