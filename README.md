
# Real-Time Personalized Health Advisory System

## Overview
This project demonstrates a real-time health advisory system using the Pathway framework for data processing and a Streamlit dashboard for visualization.

### Features
- Real-time data ingestion and processing using Pathway.
- Retrieval-Augmented Generation (RAG) pipeline for personalized recommendations.
- Streamlit-based interactive dashboard.

## Setup Instructions
1. Install required libraries: `pip install pathway streamlit pandas`.
2. Run the backend: `python backend.py`.
3. Launch the frontend: `streamlit run app.py`.
4. (Optional) Simulate data: `python simulate_data.py`.

## Files
- `backend.py`: Core data processing and RAG pipeline setup.
- `app.py`: Frontend dashboard for live data and recommendations.
- `simulate_data.py`: Simulated real-time data generator.
