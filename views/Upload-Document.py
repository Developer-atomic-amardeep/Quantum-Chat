import os
import io
import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from tqdm import tqdm

def get_azure_storage_client():
    account_name = st.session_state.get("azure_storage_account_name")
    account_key = st.session_state.get("azure_storage_account_key")
    container_name = st.session_state.get("azure_storage_container_name")

    if not all([account_name, account_key, container_name]):
        st.error("Azure Blob Storage settings are not configured. Please go to the Settings page to enter your credentials.")
        return None

    blob_service_client = BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net",
        credential=account_key,
    )
    return blob_service_client, container_name

def upload_to_azure(file, blob_service_client, container_name):
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=file.name
    )

    file_bytes = file.getvalue()
    total_bytes = len(file_bytes)
    progress_bar = st.progress(0)

    with st.spinner(f"Uploading {file.name}..."):
        with io.BytesIO(file_bytes) as byte_stream:
            with tqdm.wrapattr(byte_stream, "read", total=total_bytes, desc=f"Uploading {file.name}") as wrapped_stream:
                blob_client.upload_blob(wrapped_stream, overwrite=True, blob_type="BlockBlob", max_concurrency=10)
        st.success(f"File {file.name} uploaded successfully to Azure Blob Storage!")

    progress_bar.progress(1.0)

def upload_to_local(file, local_path):
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    file_path = os.path.join(local_path, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    st.success(f"File {file.name} uploaded successfully to local storage!")

def upload_pdf():
    st.title("Upload PDF")

    account_name = st.session_state.get("azure_storage_account_name")
    account_key = st.session_state.get("azure_storage_account_key")
    container_name = st.session_state.get("azure_storage_container_name")

    if not all([account_name, account_key, container_name]):
        st.error("Azure Blob Storage settings are not configured. Please go to the Settings page to enter your credentials.")
        return None

    # File uploader
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        if st.session_state.storage_type == "azure":
            azure_client = get_azure_storage_client()
            if azure_client:
                blob_service_client, container_name = azure_client
                for file in uploaded_files:
                    upload_to_azure(file, blob_service_client, container_name)
        else:
            local_path = st.session_state.get("local_storage_path", "./uploads")
            for file in uploaded_files:
                upload_to_local(file, local_path)

pages = {
    "Upload PDF": upload_pdf,
}

selection = st.sidebar.radio("Go To", list(pages.keys()))
pages[selection]()