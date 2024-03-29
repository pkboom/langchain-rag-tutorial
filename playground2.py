import dspy
from dotenv import load_dotenv, find_dotenv
import os
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dspy.retrieve.chromadb_rm import ChromadbRM

_ = load_dotenv(find_dotenv())  # read local .env file

llm = dspy.OpenAI(
    model="gpt-3.5-turbo", api_key=os.environ["OPENAI_API_KEY"], max_tokens=300
)

embedding_function = OpenAIEmbeddingFunction(
    api_key=os.environ.get("OPENAI_API_KEY"), model_name="text-embedding-ada-002"
)

retriever_model = ChromadbRM(
    "alice_in_wonderland",
    "chroma",
    embedding_function=embedding_function,
    k=5,
)

# results = retriever_model("How does Alice meet the Mad Hatter?", k=5)
# print(results)
# quit()

# for result in results:
#     print("Document:", result.long_text, "\n")


class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()

        dspy.settings.configure(lm=llm, rm=retriever_model)
        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate_answer = dspy.ChainOfThought("context, question -> answer")

    def forward(self, question):
        context = self.retrieve(question).passages
        answer = self.generate_answer(context=context, question=question)
        print("Context:", context)
        print("Answer:", answer)
        print("Question:", question)

        return answer


rag = RAG()  # zero-shot, uncompiled version of RAG

answer = rag("How does Alice meet the Mad Hatter?").answer

print(answer)
