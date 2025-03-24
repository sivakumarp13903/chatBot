#!/bin/bash

# Install Python dependencies
pip install --no-cache-dir -r requirements.txt

# Start the Streamlit app on the specified port and address
streamlit run app.py --server.port "${PORT:-8501}" --server.address 0.0.0.0
