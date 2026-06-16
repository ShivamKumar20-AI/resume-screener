from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def screen_resume(job_description: str, resume: str):
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume, convert_to_tensor=True)
    
    score = util.cos_sim(jd_embedding, resume_embedding).item()
    percentage = round(score * 100, 2)

    if percentage >= 75:
        verdict = "Strong Match"
    elif percentage >= 50:
        verdict = "Moderate Match"
    else:
        verdict = "Weak Match"

    return {
        "match_score": f"{percentage}%",
        "verdict": verdict,
        "feedback": f"Resume scored {percentage}% similarity against the job description."
    }