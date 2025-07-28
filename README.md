
````
# Adobe Hackathon Round 1B: Persona-Driven Document Intelligence

This project implements an intelligent document analyst that extracts and ranks the most relevant sections from a collection of documents, tailored to a given persona and job-to-be-done.

---

##  Build Docker Image

```bash
docker build --platform linux/amd64 -t persona_intel .
````

---

## ▶ Run the Container

Assuming you have:

* An `input/` folder with `persona.json`, `job.txt`, and 3–10 PDF documents.
* An empty `output/` folder.

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none persona_intel
```

---

##  Folder Structure

```
persona_intel/
├── Dockerfile
├── requirements.txt
├── main.py
├── extractor.py
├── ranker.py
├── utils.py
├── approach_explanation.md
└── README.md
```

---

##  Input Format

Place these files in the `/input` folder:

* `persona.json`

  ```json
  {
    "role": "PhD Researcher",
    "expertise": "Computational Biology"
  }
  ```

* `job.txt`

  ```
  Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks.
  ```

* 3–10 PDF documents.

---

##  Output

The container creates `/output/output.json` with:

* Extracted relevant sections (with ranking)
* Refined sub-section summaries
* Metadata including timestamp

---

##  Constraints Met

*  CPU-only execution
*  Model size < 1GB (`MiniLM`)
*  Completes in under 60 seconds for 3–5 PDFs
*  No internet access during execution

```


