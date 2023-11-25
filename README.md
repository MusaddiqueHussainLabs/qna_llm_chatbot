# Question and Answer System with Microsoft Bot Framework, FastAPI, Google Palm LLM, LangChain, and FAISS

This repository contains a Question and Answer System that integrates various technologies for efficient question answering and chatbot interaction. The system utilizes:

- **Microsoft Bot Framework** for chatbot communication and interaction.
- **FastAPI** to serve APIs and handle requests for question answering.
- **Google Palm LLM** (Large Language Model) for advanced language modeling.
- **LangChain** is a framework designed to simplify the creation of applications using large language models.
- **FAISS** for efficient similarity search and retrieval.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [License](#license)
- [Improving Accuracy](#Improving-Accuracy)

## Overview

This project aims to create a comprehensive Question and Answer System using a combination of state-of-the-art technologies. The integration of Microsoft Bot Framework enables seamless interaction through chat interfaces, while FastAPI handles the backend API requests for answering user queries using advanced language models like Google Palm LLM. LangChain designed to simplify the creation of applications using large language models, and FAISS enables efficient similarity search to enhance the system's accuracy. Additionally, integrating Huggingface Instructor Embeddings enhances contextual understanding for more nuanced responses.

## Features

- **Chatbot Interaction**: Utilize Microsoft Bot Framework + FastAPI for intuitive and interactive communication.
- **Advanced Language Modeling**: LangChain + Google Palm LLM for robust language understanding and context-aware responses.
- **Efficient Similarity Search**: FAISS integration enables quick and accurate similarity search for answering user queries.
- **Enhanced Contextual Understanding**: Leveraging Huggingface Instructor Embeddings for nuanced responses.

## Setup and Installation

### Prerequisites

- Ensure you have Python installed on your system.
- Set up Docker for deployment if using the Dockerized environment.

### Install Python 3.9

### Installation and Running the sample

1. Clone the repository:
   ```bash
   git clone https://github.com/MusaddiqueHussainLabs/qna_llm_chatbot.git
   cd qna_llm_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Acquire an api key through makersuite.google.com and put it in .env file:
   ```bash
   GOOGLE_API_KEY="your_api_key_here"
   ```

4. Run the FastAPI server:
    ```
    uvicorn app.main:app --host localhost --port 3978 --reload
    ```

### Endpoints

- `POST /api/messages/`: Sends a message and echoes it back.

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`

### Docker

To run the entire system using Docker:

1. Build the Docker image:
   ```bash
   docker build -t qna-system .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 qna-system
   ```

## License

This project is licensed under MIT. See the [LICENSE](LICENSE) file for details.

## Improving Accuracy

To enhance the accuracy of the Q&A bot further, consider implementing continuous fine-tuning of language models using domain-specific data. Additionally, explore ensemble methods by combining outputs from multiple models or leveraging diverse embeddings for a more comprehensive understanding. Lastly, integrating active learning techniques to iteratively improve the bot's responses based on user interactions can significantly enhance accuracy over time.