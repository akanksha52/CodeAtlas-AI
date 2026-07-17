from app.services.index_manager import IndexManager
from app.services.rag_service import RAGService

manager = IndexManager()
manager.build("sample_repo")
rag = RAGService(manager)
response = rag.ask(
    "How is authentication implemented?"
)

print(response)