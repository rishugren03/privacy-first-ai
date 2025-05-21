# Setup Instructions

Steps followed so far to set up the backend:

1. Create and activate virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   # OR
   source venv/bin/activate  # On macOS/Linux
   ```

2. Install required packages:

   ```bash
   pip install fastapi uvicorn
   ```

3. (Optional) For privacy filtering later:

   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

4. Create `main.py` with FastAPI app:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Hello from Mesh LLM"}

   @app.get("/health")
   def health_check():
       return {"status": "ok"}
   ```

5. Run the development server:

   ```bash
   uvicorn main:app --reload
   ```

6. Open in browser to test:

   - Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
