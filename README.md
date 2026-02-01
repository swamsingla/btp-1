
# NCERT Multilingual Smart Wiki

A structured digital knowledge platform for students in grades 6–12, converting NCERT textbooks into a multilingual (Hindi/Odia) smart wiki.

## Setup Instructions

1.  **Environment Setup**:
    ```bash
    pip install -r requirements.txt
    ```
    Create a `.env` file in the root directory with your API keys:
    ```env
    OPENAI_API_KEY=your_openai_key
    TAVILY_API_KEY=your_tavily_key
    YOUTUBE_API_KEY=your_youtube_key
    AI4BHARAT_API_KEY=your_ai4bharat_key # If using API, or configure local model
    DATABASE_URL=postgresql://user:password@localhost/ncert_wiki
    ```

2.  **Directory Structure**:
    - Place your raw NCERT PDFs in `data/input/pdfs/`.

## Running the Pipeline

The pipeline is split into 4 stages:

1.  **Structure Generation**:
    Parses the PDF Table of Contents to create a hierarchical JSON skeleton.
    ```bash
    python scripts/structure_gen.py
    ```

2.  **Content Enrichment**:
    Extracts text for each topic and enriches it using an LLM + Web Search.
    ```bash
    python scripts/content_gen.py
    ```

3.  **Translation**:
    Translates the English content to Hindi and Odia (skipping preserving math/code).
    ```bash
    python scripts/translator.py
    ```

4.  **Database Upload**:
    Seeds the final data into PostgreSQL.
    ```bash
    python scripts/db_uploader.py
    ```

## Development

- **Scripts**: Located in `scripts/` folder.
- **Data**: All intermediate data is stored in `data/`.
