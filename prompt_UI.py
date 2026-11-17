# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# # from dotenv import load_dotenv
# import streamlit as st
# import os

# # load_dotenv()

# llm = HuggingFaceEndpoint( huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN"), repo_id="TinyLlama/TinyLlama-1.1B-Chat-v0.6", task="text-generation")

# HF = ChatHuggingFace(llm=llm)

# st.header("Research Tool")

# user_input = st.text_input("Enter your research query/prompt here:")

# if st.button("Summarize"):
#     result = HF.invoke(user_input)
#     st.write(result.content)


### In the above code we used Hugging Face API, and in all the below codes we used Google API. Thats it. 






## IN THE BELOW CODE, WE DIRECTLY TAKE THE INPUT FROM THE USER AND PASS IT TO THE MODEL, AND GET THE RESPONSE.

# from langchain_google_genai import ChatGoogleGenerativeAI
# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8)  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

# st.header("Research Tool")

# user_input = st.text_input("Enter your research query/prompt here:")  

# if st.button("Summarize"):
#     result = chatModel.invoke(user_input) 
#     st.write(result.text)  # this will give us the actual response from the model.







## IN THE BELOW CODE, WE FIRST MAKE A SIMPLE PROMPT TEMPLATE USING F STRINGS, AND THEN PASS IT TO THE MODEL, AND GET THE RESPONSE.

# from langchain_google_genai import ChatGoogleGenerativeAI
# import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()  # Load environment variables from .env file

# chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8)  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

# st.header("Research Tool")

# paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox("Select Explanation Length", ["Short(1-2 paragraphs)", "Medium(3-4 paragraphs)", "Long(5+ paragraphs)"])

# prompt = f"Please summarize the research paper {paper_input} in a {style_input} style and make it {length_input} in length."

# if st.button("Summarize"):
#     result = chatModel.invoke(prompt)
#     st.write(result.text)







##IN THE BELOW CODE, WE FIRST MAKE A SIMPLE PROMPT TEMPLATE USING LANGCHAIN PROMPT TEMPLATES, AND THEN PASS IT TO THE MODEL, AND GET THE RESPONSE.

# from langchain_google_genai import ChatGoogleGenerativeAI
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()  # Load environment variables from .env file

# chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8)  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

# st.header("Research Tool")

# paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox("Select Explanation Length", ["Short(1-2 paragraphs)", "Medium(3-4 paragraphs)", "Long(5+ paragraphs)"])

# # template 

# template = PromptTemplate(
#     template = """ Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  
# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length. """,
# input_variables=["paper_input", "style_input", "length_input"],
# validate_template=True
# )

# # fill the placeholders in the template with the user inputs

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,     
#     'length_input': length_input
# })

# if st.button("Summarize"):
#     result = chatModel.invoke(prompt)
#     st.write(result.text)







## IN THE BELOW CODE, WE FIRST MAKE A SIMPLE PROMPT TEMPLATE USING LANGCHAIN PROMPT TEMPLATES, AND THEN SAVE IT TO A JSON FILE, AND THEN PASS IT TO THE MODEL, AND GET THE RESPONSE.

# from langchain_google_genai import ChatGoogleGenerativeAI
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate, load_prompt  # Import the load_prompt function from prompt_generator.py

# load_dotenv()  # Load environment variables from .env file

# chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8)  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

# st.header("Research Tool")

# paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox("Select Explanation Length", ["Short(1-2 paragraphs)", "Medium(3-4 paragraphs)", "Long(5+ paragraphs)"])

# template = load_prompt("template.json")  # Load the template from the JSON file

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,     
#     'length_input': length_input    
# })

# if st.button("Summarize"):
#     result = chatModel.invoke(prompt)
#     st.write(result.text)






## IN THE BELOW CODE, WE WILL SEE HOW CHAIN CONCEPT WORKS, i.e IN THE ABOVE WE HAD TO CALL invoke() TWICE, ONCE FOR THE PROMPT TEMPLATE AND ONCE FOR THE MODEL, BUT IN CHAIN CONCEPT WE CAN CALL IT ONCE, AND IT WILL AUTOMATICALLY CALL THE PROMPT TEMPLATE AND THEN THE MODEL. 
# THIS IS CALLED LCEL LANG CHAIN EXPRESSION LANGUAGE. THE '|' OPERATOR CONNECTS TWO COMPONENTS INTO A CHAIN. 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8)

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox("Select Explanation Length", ["Short(1-2 paragraphs)", "Medium(3-4 paragraphs)", "Long(5+ paragraphs)"])

template = load_prompt("template.json")

if st.button("Summarize"):
    chain = template | chatModel
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.text)


