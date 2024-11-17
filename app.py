import streamlit as st
import google.generativeai as genai

api_key="Your API KEY"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-1.5-flash")

st.title(":rainbow[AI Question Answer Platform]")
st.write("Built using :blue[Python], :blue[Gemini] and  :red[Streamlit]")

options=[ 'Geography', 'Health','Sports']

selected_option=st.selectbox("Select Topic",options)


if "question" not in st.session_state:
    st.session_state['question']=None

if st.button("Generate Question"):
    question_prompt=(
        f"Generate a unique trivia question about {selected_option}, different from the any recent questions. focus on interesting and don't repeat questions."
        f"Don't provide the answer ,provide just question."
    )
    response=model.generate_content(question_prompt)
    st.session_state['answer']=""
    st.session_state['question']=response.text
    


if (st.session_state['question']):
    st.write(st.session_state['question'])


answer=st.text_input("Enter Answer",key="answer")

if st.button("Submit Answer"):
    answer_prompt=(
        f"you are a question answer bot, helpful for user to generate the answer for question and evaluate the user's answer"
        f"just give answer to the user, nothing else. also give the input {st.session_state['answer']} correct or incorrect at the start and start answer from next new line"
        f"First check is there any input {st.session_state['answer']} is provided or not , if not then dont's say incorrect answer just provide the output and if provided then evaluate the answer {answer} is correct for the question {st.session_state['question']}"
        f"if the answer is incorrect, provide the correct answer along with short explaination."
        f"such as relevent years, frequency of event, or notable facts in two to three sentences"
    )
    answer=model.generate_content(answer_prompt)
    st.session_state['correct_answer']=answer.text
    st.write(st.session_state['correct_answer'])