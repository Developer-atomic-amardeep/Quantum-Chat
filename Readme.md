# Quantum Chat

Quantum Chat is an open-source, web-based chat application that leverages Azure OpenAI models. It allows users to bring their own API keys and deploy custom models, making it a flexible and powerful platform for AI-driven conversations.

## Features

- **BYOK (Bring Your Own Key)**: Use your own Azure OpenAI API keys for full control and customization.
- **Custom Model Deployment**: Specify your own deployment name and endpoint for Azure OpenAI models.
- **Document Upload**: Upload documents to Azure Blob Storage or a local server for future RAG (Retrieval-Augmented Generation) functionality.
- **Secure Authentication**: BCrypt-based hashed login using Streamlit's authentication method.

## Upcoming Features

- RAG functionality with various vector stores (e.g., Pinecone)
- Database-based login system
- Chat history storage and retrieval by date and time

## Getting Started

### Prerequisites

- Python 3.7+
- Azure OpenAI API access
- (Optional) Azure Blob Storage account

### Installation

1. Clone the repository:
    git clone https://github.com/yourusername/quantum-chat.git
    cd quantum-chat

2. Install required dependencies:
   
    pip install -r requirements.txt

4. Run the application:

    streamlit run streamlit_app.py

## Usage

1. Launch the application and log in using the provided authentication system.
2. Enter your Azure OpenAI API key, deployment name, and endpoint.
3. Start chatting with your custom-deployed model.
4. (Optional) Upload documents for future RAG functionality.

## Contributing

We welcome contributions to Quantum Chat! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Azure OpenAI for providing the underlying AI models
- Streamlit for the web application framework
- All contributors and supporters of the project

## Contact

For any queries or suggestions, please open an issue on this GitHub repository.

---

Quantum Chat - Empowering open-source AI conversations
