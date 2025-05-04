# Agentic Trading System

## Overview

The **Agentic Trading System** is a multi-agent chatbot platform designed to assist users with stock market-related queries. It integrates various tools, APIs, and machine learning models to provide intelligent responses based on real-time data, user-uploaded documents, and pre-configured knowledge bases. The system is built using modern Python frameworks and libraries, including FastAPI, Streamlit, and LangChain.

---

## Features

1. **Stock Market Query Handling**:
   - Users can ask questions related to stock market data, financials, and trends.
   - The system uses tools like Tavily, Polygon API, and Bing Search to fetch relevant data.

2. **Document Ingestion**:
   - Users can upload PDF or DOCX files containing stock market-related information.
   - The system processes these documents and stores them in a vector database for retrieval.

3. **Multi-Agent Architecture**:
   - The chatbot leverages multiple tools and APIs to provide accurate and context-aware responses.

4. **Real-Time Data Integration**:
   - The system integrates with APIs like Polygon for real-time stock market data.

5. **Streamlit UI**:
   - A user-friendly interface for uploading documents and interacting with the chatbot.

6. **FastAPI Backend**:
   - A robust backend for handling file uploads, queries, and data ingestion pipelines.

---

## System Design

### Architecture Diagram

The system follows a modular architecture with the following components:

1. **Frontend**:
   - **Streamlit UI**: Provides an interface for users to upload documents and interact with the chatbot.

2. **Backend**:
   - **FastAPI**: Handles API requests for file uploads and chatbot queries.
   - **Data Ingestion Pipeline**: Processes uploaded documents and stores them in a vector database.

3. **Core Components**:
   - **GraphBuilder**: Manages the chatbot's state graph and tool integration.
   - **ModelLoader**: Loads LLMs and embedding models for processing queries.
   - **Tools**: Includes Tavily, Polygon Financials, and Bing Search for data retrieval.

4. **Database**:
   - **Pinecone Vector Store**: Stores document embeddings for efficient retrieval.

5. **External APIs**:
   - **Polygon API**: Provides real-time stock market data.
   - **Tavily API**: Fetches advanced search results.
   - **Google Generative AI**: Powers the LLM and embedding models.

---

### Workflow

1. **Document Ingestion**:
   - Users upload PDF/DOCX files via the Streamlit UI.
   - The backend processes these files, splits them into chunks, and stores embeddings in Pinecone.

2. **Query Handling**:
   - Users submit stock market-related questions via the Streamlit UI.
   - The FastAPI backend invokes the chatbot's state graph to process the query.
   - The chatbot uses tools and APIs to fetch relevant data and generate a response.

3. **Response Delivery**:
   - The chatbot's response is sent back to the user via the Streamlit UI.

---

## Project Structure
```bash
agentic-trading-bot/
├── agent/
│   ├── agents.py
│   ├── workflow.py
├── config/
│   ├── config.yaml
│   ├── __init__.py
├── data_ingestion/
│   ├── ingestion_pipeline.py
├── data_models/
│   ├── models.py
│   ├── __init__.py
├── exception/
│   ├── exceptions.py
├── logging/
│   ├── my_logging.py
├── notebook_experiments/
│   ├── experiments.ipynb
├── prompt_library/
│   ├── prompt.py
│   ├── __init__.py
├── toolkit/
│   ├── tools.py
│   ├── __init__.py
├── utils/
│   ├── model_loaders.py
│   ├── config_loader.py
│   ├── __init__.py
├── main.py
├── main2.py
├── streamlit_ui.py
├── setup.py
├── .env
├── .gitignore
├── requirement.txt
```


---

## Key Components

### 1. **Data Ingestion Pipeline**
   - Located in `data_ingestion/ingestion_pipeline.py`.
   - Handles document loading, splitting, and embedding storage in Pinecone.

### 2. **GraphBuilder**
   - Located in `agent/workflow.py`.
   - Manages the chatbot's state graph and integrates tools for query processing.

### 3. **ModelLoader**
   - Located in `utils/model_loaders.py`.
   - Loads LLMs and embedding models using Google Generative AI.

### 4. **Tools**
   - Located in `toolkit/tools.py`.
   - Includes Tavily, Polygon Financials, and Bing Search for data retrieval.

### 5. **Streamlit UI**
   - Located in `streamlit_ui.py`.
   - Provides a user-friendly interface for document uploads and chatbot interaction.

---

## Technologies Used

- **Python Frameworks**: FastAPI, Streamlit
- **Machine Learning**: LangChain, Google Generative AI
- **Database**: Pinecone Vector Store
- **APIs**: Polygon, Tavily, Bing Search
- **Utilities**: dotenv, pydantic, yaml

---

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt

2. **Set Up Environment Variables**:
- Add API keys in the .env file.

3. **Run the Backend**:
  ```bash
  uvicorn main:app --reload
  ```

4. **Run the Frontend**:
  ```bash
    streamlit run streamlit_ui.py
  ```
5. **Access the Application**:

- Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).