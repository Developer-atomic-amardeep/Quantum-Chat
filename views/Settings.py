# import streamlit as st

# st.title("Settings")

#     # Input fields for Azure OpenAI settings
# api_key = st.text_input("Azure OpenAI API Key", type="password")
# endpoint = st.text_input("Azure OpenAI Endpoint")
# deployment_name = st.text_input("Deployment Name")

#     # Storage option
# st.subheader("Storage Settings")
# use_azure_storage = st.toggle("Use Azure Blob Storage", value=True)

# if use_azure_storage:
#     st.session_state.storage_type = "azure"
#     account_name = st.text_input("Azure Storage Account Name")
#     account_key = st.text_input("Azure Storage Account Key", type="password")
#     container_name = st.text_input("Azure Storage Container Name")
# else:
#     st.session_state.storage_type = "local"
#     local_storage_path = st.text_input("Local Storage Path", value="./uploads")

#     # Save button
# if st.button("Save Settings"):
#     st.session_state.azure_openai_api_key = api_key
#     st.session_state.azure_openai_endpoint = endpoint
#     st.session_state.azure_openai_deployment_name = deployment_name

#     if use_azure_storage:
#         st.session_state.azure_storage_account_name = account_name
#         st.session_state.azure_storage_account_key = account_key
#         st.session_state.azure_storage_container_name = container_name
#     else:
#         st.session_state.local_storage_path = local_storage_path

#     st.success("Settings saved successfully!")

import streamlit as st

st.title("Settings")

# Check if values exist in session state
api_key = st.session_state.get("azure_openai_api_key", "")
endpoint = st.session_state.get("azure_openai_endpoint", "")
deployment_name = st.session_state.get("azure_openai_deployment_name", "")

# Input fields for Azure OpenAI settings
api_key = st.text_input("Azure OpenAI API Key", type="password", value=api_key)
endpoint = st.text_input("Azure OpenAI Endpoint", value=endpoint)
deployment_name = st.text_input("Deployment Name", value=deployment_name)

# Storage option
st.subheader("Storage Settings")
use_azure_storage = st.toggle("Use Azure Blob Storage", value=st.session_state.get("storage_type", "azure") == "azure")

if use_azure_storage:
    account_name = st.text_input("Azure Storage Account Name", value=st.session_state.get("azure_storage_account_name", ""))
    account_key = st.text_input("Azure Storage Account Key", type="password", value=st.session_state.get("azure_storage_account_key", ""))
    container_name = st.text_input("Azure Storage Container Name", value=st.session_state.get("azure_storage_container_name", ""))
else:
    local_storage_path = st.text_input("Local Storage Path", value=st.session_state.get("local_storage_path", "./uploads"))

# Save button
if st.button("Save Settings"):
    st.session_state.azure_openai_api_key = api_key
    st.session_state.azure_openai_endpoint = endpoint
    st.session_state.azure_openai_deployment_name = deployment_name

    if use_azure_storage:
        st.session_state.azure_storage_account_name = account_name
        st.session_state.azure_storage_account_key = account_key
        st.session_state.azure_storage_container_name = container_name
        st.session_state.storage_type = "azure"
    else:
        st.session_state.local_storage_path = local_storage_path
        st.session_state.storage_type = "local"

    st.success("Settings saved successfully!")

