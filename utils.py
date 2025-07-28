import json
import datetime

def create_output_json(input_docs, persona, job, ranked, top_k=3):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    metadata = {"input_documents": input_docs, "persona": persona, "job_to_be_done": job,
                "processing_timestamp": now}
    extracted = []
    subs = []
    for rank, (score, sec) in enumerate(ranked[:top_k], start=1):
        extracted.append({
            "document": sec["doc"],
            "page_number": sec["page"],
            "section_title": sec["section_title"],
            "importance_rank": rank
        })
        subs.append({
            "document": sec["doc"],
            "refined_text": sec["refined_text"],
            "page_number": sec["page"]
        })
    return {"metadata": metadata, "extracted_sections": extracted, "subsection_analysis": subs}
