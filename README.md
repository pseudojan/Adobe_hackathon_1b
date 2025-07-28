# Adobe_hackathon_1b

# Persona-Driven Document Intelligence

## Build
docker build --platform linux/amd64 -t persona_intel .

## Run
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none persona_intel

# 📁 Project Structure
css
Copy
Edit
persona_intel/
├── Dockerfile
├── requirements.txt
├── main.py
├── extractor.py
├── ranker.py
├── utils.py
├── approach_explanation.md
└── README.md

