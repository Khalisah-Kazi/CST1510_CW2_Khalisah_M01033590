import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page title
st.title("IT Assistant")

# Initialize session state with system prompt
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """You are an IT operations expert assistant.
Help troubleshoot issues, optimize systems, and manage tickets."""
        }
    ]

# Display all previous messages (skip system message)
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system prompt
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Ask about cybersecurity...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to session state
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Call OpenAI API
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages
        )
        
        # Extract assistant response
        response = completion.choices[0].message.content
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add assistant response to session state
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
    
    except Exception as e:
        st.error(f"Error calling OpenAI API: {e}")
        # Remove user message if API call failed
        st.session_state.messages.pop()