# 🚀 Redrob AI Candidate Ranker

An AI-powered candidate ranking system built for the **Redrob AI Hiring Challenge**. Instead of relying only on keyword matching, this solution understands both the **Job Description (JD)** and **candidate profiles** using semantic embeddings, evidence-based scoring, and explainable AI to recommend the most relevant candidates.

---

## 📌 Problem Statement

Recruiters often miss great candidates because traditional ATS systems depend heavily on keyword matching.

This project aims to build a smarter ranking system that:
- Understands the job description
- Evaluates complete candidate profiles
- Uses semantic similarity instead of exact keyword matches
- Produces an explainable ranked shortlist

---

## ✨ Features

- 📄 Automatic Job Description understanding
- 🧠 Semantic candidate matching using Sentence Transformers
- 📊 Hybrid ranking with multiple scoring signals
- 🔍 Evidence-based career evaluation
- 💡 Explainable AI recommendations
- 📈 Fast ranking over 100,000 candidate profiles
- 📁 Generates submission-ready CSV output

<img width="1920" height="1080" alt="Screenshot 2026-06-28 225839" src="https://github.com/user-attachments/assets/43b8124e-e50b-43b5-8d05-446ca39948fa" />

---

# 🏗️ Project Structure

```
redrob_ranker/
│
├── src/
│   ├── jd_analyzer.py
│   ├── ranker.py
│   ├── semantic_ranker.py
│   ├── explanation.py
│   ├── report.py
│   └── ...
│
├── main.py
├── requirements.txt
├── submission.csv
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

- Python
- Sentence Transformers
- Hugging Face Transformers
- NumPy
- Pandas
- tqdm
- JSON
- Semantic Search
- Hybrid Ranking
- Explainable AI

---

# 🧠 Ranking Methodology

The ranking process consists of four stages:

### 1️⃣ JD Understanding
The system extracts important requirements from the Job Description such as:
- Skills
- Technologies
- Experience
- Domain requirements

---

### 2️⃣ Candidate Filtering

Candidates are filtered using:
- Current role
- Experience
- Relevant job titles

This reduces unnecessary computation before semantic ranking.

---

### 3️⃣ Hybrid Ranking

Each candidate receives scores from multiple components:

- Semantic Similarity
- Career Evidence Score
- Skill Match
- Recruiter Signals
- Platform Activity

These are combined into one final score.

---

### 4️⃣ Explainable Recommendation

Instead of returning only a score, the system explains **why** a candidate was ranked highly.

Example:

```
Recommendation: STRONG HIRE

Strengths:
✓ Embeddings
✓ Retrieval
✓ Ranking

Explanation:
✓ Strong semantic match
✓ Relevant production experience
✓ High recruiter response rate
```

---

# 📊 Sample Output

```
Candidate ID : CAND_0071974

Final Score : 59.08

Recommendation : STRONG HIRE

Strengths
✓ Embeddings
✓ Retrieval
✓ Ranking

Explanation
✓ Strong semantic match
✓ Relevant production experience
✓ High recruiter response rate
```

---

# 📈 Performance

| Metric | Result |
|---------|--------|
| Total Profiles | 100,000 |
| Relevant Candidates | 5,694 |
| Embedding Model | all-MiniLM-L6-v2 |
| Ranking Method | Hybrid AI Ranking |
| Output | Ranked CSV |

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/rithikashanmugam-web/redrob-ai-candidate-ranker.git
```

Move into the project

```bash
cd redrob-ai-candidate-ranker
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python main.py
```

The program will:

- Load the Job Description
- Filter candidates
- Generate semantic embeddings
- Rank candidates
- Produce explanations
- Save

```
submission.csv
```

---

# 📂 Dataset

The competition dataset is **not included** in this repository because it exceeds GitHub's file size limit.

Place the provided dataset inside:

```
data/
```

before running the project.

Example:

```
data/
    candidates.jsonl
```

---

# 📁 Output

The generated submission file:

```
submission.csv
```

contains

| Rank | Candidate ID | Final Score |
|------|--------------|------------|

which is ready for challenge submission.

---

# 💡 Future Improvements

- LLM-based reasoning for candidate explanations
- Cross-encoder reranking
- Recruiter feedback learning
- Skill graph matching
- Real-time API deployment
- Interactive recruiter dashboard

---

# 👩‍💻 Author

**Rithika S**

Built for the **Redrob AI Candidate Ranking Challenge 2026**

---

# ⭐ Acknowledgements

- Redrob AI
- Hack2Skill
- Hugging Face
- Sentence Transformers
- Python Open Source Community
