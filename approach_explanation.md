# Approach Explanation

This solution addresses the Persona-Driven Document Intelligence challenge by extracting and ranking relevant sections from multiple PDFs based on a persona’s role and a job-to-be-done.

## Architecture Overview

1. **Document Parsing**: Uses PyMuPDF to extract page-level text.
2. **Text Chunking**: Splits text into manageable sections.
3. **Embedding & Ranking**: Uses `sentence-transformers` (MiniLM) to embed sections and query (persona+job) into vector space. Computes cosine similarity to rank relevance.
4. **Subsection Extraction**: Extracts a refined snippet from top-ranked sections using a token threshold.
5. **Output Formatting**: Assembles the final output in the required JSON format.

## Constraints Handled

- **CPU Only**: All models are small and efficient.
- **Model Size <1GB**: MiniLM (90MB) fits within limits.
- **Time <60s**: Works efficiently on 3-5 PDFs.
- **Offline Execution**: No internet required.

## Modules

- `extractor.py`: PDF parsing and sectioning.
- `ranker.py`: Embedding and scoring logic.
- `utils.py`: JSON formatting utilities.
- `main.py`: Pipeline orchestration.

This modular design ensures both scalability and clarity. The system is designed to be generic, applicable across domains and personas.
