# Setup

In ./RAG Model run:

```python -m venv venv```

On linux or mac use python3

Activate the venv with:

```source venv/Scripts/activate```

or linux:

```source venv/bin/activate```

---

# Packages
```
pip install chromadb
pip install -q -U google-genai
```

---

# API Key
If you want to use Gemini, create a .env file in ./RAG Model, and add the line GENAI_KEY="API_KEY"

---

# Local
If you want to use a local model, install ollama if you haven't, and then run

```ollama pull llama3.2```

or change the code to use the model of your choosening
