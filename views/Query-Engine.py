import streamlit as st
from openai import AzureOpenAI

st.title("ContextAI: Chat Engine")

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear Chat"):
        st.session_state["Sustain-AI"] = []

# with col2:
#     authenticator.logout("Logout", "main")

if "Sustain-AI" not in st.session_state:
    st.session_state["Sustain-AI"] = []

with st.chat_message("assistant"):
    st.markdown("Hi, How may I help you?")

    # Display chat history for Sustain-AI
for message in st.session_state["Sustain-AI"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter Your Query Here !!!"):
    st.session_state["Sustain-AI"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            api_key = st.session_state.get("azure_openai_api_key")
            endpoint = st.session_state.get("azure_openai_endpoint")
            deployment_name = st.session_state.get("azure_openai_deployment_name")

            if not api_key or not endpoint or not deployment_name:
                st.error("Azure OpenAI settings are not configured. Please go to the Settings page to set them up.")
            else:
                client = AzureOpenAI(
                    api_key=api_key,
                    api_version="2024-02-01",
                    azure_endpoint=endpoint
                )

                    # Send a completion call to generate an answer
                try:
                    response = client.chat.completions.create(
                        model=deployment_name, # model = "deployment_name".
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state["Sustain-AI"].append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
