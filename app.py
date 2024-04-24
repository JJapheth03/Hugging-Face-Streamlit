import streamlit as st
from transformers import pipeline

# Initialize the question-answering pipeline
nlp = pipeline("question-answering")

# Function to answer the question and return context
def answer_question(question, context):
    answer = nlp(question=question, context=context)
    return answer["answer"], context  # Return context for display

# Main app code
st.title("Question Answering App")

# Text input for user's question
question = st.text_input("Ask a question:")

# Text area for context or passage input
context = st.text_area("Context:")

if question and context:
    answer, context = answer_question(question, context)
    
    # Display answer and context
    st.markdown(f"**Answer:** {answer}")
    st.markdown(f"**Context:** {context}")

