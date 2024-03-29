# Langchain RAG Tutorial

Create venv

```sh
pip install virtualenv
python -m venv .venv
. .venv/bin/activate

# Deactivate and remvoe .venv
deactivate
rm -rf .venv
```

Install dependencies.

```sh
pip install -r requirements.txt
```

Create the Chroma DB.

```sh
python create_database.py
```

Query the Chroma DB.

```sh
python query_data.py "How does Alice meet the Mad Hatter?"
```

You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

# Weaviate

Docker

https://weaviate.io/developers/weaviate/installation/docker-compose
