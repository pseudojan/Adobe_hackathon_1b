import os, json
from extractor import extract_sections
from ranker import score_sections, extract_refined_text
from utils import create_output_json

INPUT = "/app/input"
OUTPUT = "/app/output"

def main():
    persona = json.load(open(os.path.join(INPUT, "persona.json")))
    job = open(os.path.join(INPUT, "job.txt")).read().strip()
    persona_job = f"Role: {persona['role']}. Expertise: {persona.get('expertise','')}. Task: {job}"
    all_sections = []
    input_docs = []
    for fname in os.listdir(INPUT):
        if fname.endswith(".pdf"):
            path = os.path.join(INPUT, fname)
            secs = extract_sections(path)
            for s in secs:
                s["doc"] = fname
            all_sections.extend(secs)
            input_docs.append(fname)
    ranked = score_sections(persona_job, all_sections)
    for score, sec in ranked:
        sec["refined_text"] = extract_refined_text(sec)
    output = create_output_json(input_docs, persona, job, ranked, top_k=5)
    with open(os.path.join(OUTPUT, "output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
