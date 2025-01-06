
# Main Backend Code: Pathway Integration and RAG Pipeline
import pathway as pw
from pathway.xpacks.llm.document_store import PathwayDocumentStore
from pathway.xpacks.llm.retrieval import RetrievalPipeline
from pathway.xpacks.llm.question_answering import AdaptiveRAGQuestionAnswerer

# Mock data sources (simulated real-time data)
data = pw.io.generate(
    columns=["timestamp", "heart_rate", "steps", "calories"],
    rows=[
        ("2025-01-01 12:00", 80, 5000, 200),
        ("2025-01-01 12:01", 85, 5200, 210),
        ("2025-01-01 12:02", 90, 5300, 220),
    ],
)

# Data processing pipeline
def process_data():
    processed = data.select(
        "timestamp",
        "heart_rate",
        "steps",
        calories_per_step=pw.this.calories / pw.this.steps
    )
    return processed

# RAG Pipeline Setup
def setup_rag_pipeline():
    document_store = PathwayDocumentStore()
    document_store.add_documents([
        {"text": "Stay hydrated after exercise to maintain energy."},
        {"text": "Walking 10,000 steps daily improves cardiovascular health."},
    ])

    retriever = RetrievalPipeline(document_store=document_store)
    rag_answerer = AdaptiveRAGQuestionAnswerer(retriever=retriever)

    return rag_answerer

# Main pipeline
rag_pipeline = setup_rag_pipeline()

# Example query and retrieval
query = "What should I do if my heart rate is high?"
response = rag_pipeline.answer(query=query)

print("RAG Response:", response)

# Export processed data
processed_data = process_data()
pw.io.print(processed_data)
