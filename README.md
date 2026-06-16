# Resume Screener API

A REST API that scores how well a resume matches a job description using **sentence similarity** and a fine-tuned MiniLM model served via **FastAPI**.

---

## Demo Results

Real-world resumes tested against a Data Scientist job description:

| Resume | Match Score | Verdict |
|--------|-------------|----------|
| Data Scientist (3 years Python, ML, data analysis) | 79.6% | ✅ Strong Match |
| Software Developer (Python, Django, REST APIs) | 50.23% | ⚠️ Moderate Match |
| Experienced Chef (fine dining, kitchen management) | 23.99% | ❌ Weak Match |

> **How it works:** Both the job description and resume are converted into semantic vector embeddings using a fine-tuned sentence transformer. Cosine similarity is then calculated between the two vectors — the closer the vectors, the higher the match score. This goes beyond keyword matching by understanding the *meaning* of the text.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Model | sentence-transformers/all-MiniLM-L6-v2 |
| Framework | HuggingFace Sentence Transformers |
| API | FastAPI |
| Server | Uvicorn |
| Language | Python 3.11+ |

---

## Project Structure

```
resume-screener/
├── main.py          # FastAPI app and /screen endpoint
├── model.py         # Sentence transformer and cosine similarity logic
├── requirements.txt # Python dependencies
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ShivamKumar20-AI/resume-screener.git
cd resume-screener
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`

---

## API Usage

### Endpoint

```
POST /screen
```

### Request

Send a JSON body with `job_description` and `resume` fields:

```bash
curl -X POST "http://127.0.0.1:8000/screen" \
     -H "Content-Type: application/json" \
     -d '{
       "job_description": "We are looking for a Data Scientist with experience in Python, machine learning, and data analysis.",
       "resume": "Experienced Data Scientist with 3 years in Python, machine learning models, and statistical data analysis."
     }'
```

### Response

```json
{
  "match_score": "79.6%",
  "verdict": "Strong Match",
  "feedback": "Resume scored 79.6% similarity against the job description."
}
```

### Verdict Thresholds

| Score | Verdict |
|-------|---------|
| 75% and above | Strong Match |
| 50% – 74% | Moderate Match |
| Below 50% | Weak Match |

### Interactive Docs

FastAPI auto-generates interactive documentation. Once the server is running, visit:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## How It Works

1. Both the job description and resume are passed through `all-MiniLM-L6-v2` to generate 384-dimensional vector embeddings
2. Cosine similarity is calculated between the two vectors
3. The score is converted to a percentage and mapped to a verdict
4. Unlike keyword matching, this approach understands semantic meaning — "software engineer" and "developer" score as similar even without exact word overlap

---

## Limitations

- **No keyword extraction** — does not highlight specific missing skills
- **Score is holistic** — a resume that mentions many unrelated things may score lower than expected
- **English only** — the model was trained on English text

---

## Author

**Shivam Kumar** — AI & ML Engineer

[![GitHub](https://img.shields.io/badge/GitHub-ShivamKumar20--AI-black?logo=github)](https://github.com/ShivamKumar20-AI)
