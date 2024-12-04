# Conversational Recommender System

This project implements a conversational recommender system using FastAPI, LangChain, and various NLP models. The system retrieves relevant documents based on user queries and generates responses using a language model.

## Prerequisites

- Docker

## Setup and Run

1. Clone the repository and navigate to the project directory.

2. Create a `.env` file in the `app` directory and add your OpenAI API key and other configurations. You can use the `.env.example` file as a reference:

   ```env
    export EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
    export LLM_MODEL="gpt-4"
    export TEMPERATURE=0.7
    export OPENAI_API_KEY="your_openai_api_key"
    ```

3. Build and run the Docker containers:

    ```sh
    docker-compose up --build
    ```

4. The API will be available at `http://localhost:8001/api/recommendation`.

## API Endpoint

### Recommendation API

- **Endpoint:** `POST /api/recommendation`
- **Request Body:**

    ```json
    {
      "question": "What are some good movies to watch?",
      "history": ["I like action movies.", "I enjoyed watching Inception."]
    }
    ```

- **Response:**

    ```json
    {
      "response": "Based on your interest in action movies and enjoyment of Inception, I recommend watching The Dark Knight, Mad Max: Fury Road, and John Wick."
    }
    ```

You can also check the API documentation using Swagger UI at `http://127.0.0.1:8001/docs`.

