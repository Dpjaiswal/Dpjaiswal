<h1 align="center">Hi, I'm Durga Prasad Jaiswal</h1>
<h3 align="center">GenAI Engineer • Production RAG Systems • LLM Application Development</h3>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=Building+Production-Grade+RAG+Pipelines;Hybrid+Retrieval+%2B+Cross-Encoder+Reranking;LLM+Guardrails+%26+Hallucination+Mitigation;FastAPI+%2B+LangChain+%2B+Qdrant" />
</p>

<p align="center">
<a href="https://www.linkedin.com/in/dp-jaiswal/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="mailto:dpjaiswal.lkouniv@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://dpjaiiswal-portfolio.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
<a href="https://ijamred.com/volume1/issue4/IJAMRED-V1I4P56.pdf"><img src="https://img.shields.io/badge/Research_Paper-4CAF50?style=for-the-badge&logo=readthedocs&logoColor=white" /></a>
</p>

<p align="center">
<img src="https://komarev.com/ghpvc/?username=Dpjaiswal&label=Profile%20Views&color=0e75b6&style=flat-square" />
</p>

---

### About Me

I'm a GenAI Engineer specializing in **production-grade Retrieval-Augmented Generation** — building systems that are accurate, source-cited, and auditable, not just conversational. I work at the intersection of hybrid retrieval, LLM orchestration, and scalable backend engineering to turn research-grade AI techniques into reliable, deployable products.

Currently building RAG pipelines and agentic workflows at **Mobcoder AI**, with hands-on production experience across financial, legal, and career-guidance domains.

- Currently focused on: **Advanced RAG architectures & Agentic AI workflows**
- Core strength: turning hallucination-prone LLM systems into **grounded, citation-backed, evaluable pipelines**
- Actively exploring: multi-agent orchestration and deterministic LLM evaluation
- Open to GenAI Engineer / ML Engineer / Backend (AI-focused) roles

---

### Tech Stack

**Languages & Backend**
<p>
<img src="https://skillicons.dev/icons?i=python,fastapi,django,flask" />
</p>

**GenAI & Retrieval**
<p>
<img src="https://img.shields.io/badge/RAG-FF6B35?style=flat-square"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square"/>
<img src="https://img.shields.io/badge/LangGraph-4B32C3?style=flat-square"/>
<img src="https://img.shields.io/badge/LangSmith-FF6B35?style=flat-square"/>
<img src="https://img.shields.io/badge/Hybrid_Search-228B22?style=flat-square"/>
<img src="https://img.shields.io/badge/BM25-FF5722?style=flat-square"/>
<img src="https://img.shields.io/badge/Cross_Encoder_Reranking-8A2BE2?style=flat-square"/>
<img src="https://img.shields.io/badge/RRF-0A66C2?style=flat-square"/>
</p>

**ML & CV**
<p>
<img src="https://skillicons.dev/icons?i=tensorflow,pytorch" />
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-FF6F00?style=flat-square"/>
</p>

**Databases & Tools**
<p>
<img src="https://skillicons.dev/icons?i=mysql,mongodb,docker,git,github,vscode" />
<img src="https://img.shields.io/badge/Qdrant_Vector_DB-EA4335?style=flat-square"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
</p>

---

### Professional Experience

**AIML Software Trainee — Mobcoder AI** · *Feb 2026 – Present*
- Engineer production RAG pipelines: document ingestion, semantic chunking, embedding generation, and vector indexing.
- Design hybrid retrieval systems (dense + sparse) with cross-encoder reranking to improve contextual relevance.
- Build grounded LLM answer-generation workflows with fallback strategies and guardrails to minimize hallucinations.

**AI/ML Engineer Intern — Apana Time Tech Solutions** · *Oct 2025 – Jan 2026*
- Built scalable backend APIs with Python and FastAPI for workflow automation and task tracking.
- Implemented RBAC and secure authentication to maintain data integrity across system modules.
- Automated approval workflows and activity auditing, improving operational transparency.

---

### Featured Projects

#### [Financial RAG Copilot (Multi-Entity, Audit-Grade)](#)
A six-layer, audit-grade RAG system for 10-K/10-Q financial filings — built for accuracy and traceability, not just fluency.
- Hybrid search engine (dense `qwen3-embedding:4b` + BM25 sparse + RRF) with metadata filtering for multi-company comparison.
- Two-stage retrieval with `BGE-Reranker-Base` cross-encoder reranking.
- Deterministic evaluation layer (faithfulness, groundedness, hallucination rate, citation accuracy) — no LLM-as-judge shortcuts.
- Full audit logging in PostgreSQL; regex-based heuristic fallback for robustness; FastAPI `/application/query` endpoint with a Streamlit UI.

`FastAPI` `LangChain` `Qdrant` `BM25` `Groq` `BGE-Reranker` `PostgreSQL`

#### [Legal Judgment RAG System](#)
A modular legal question-answering system built to answer strictly from retrieved context — never from model memory.
- Dense (Qdrant) + TF-IDF sparse scoring + cross-encoder reranking with score normalization.
- Threshold-based fallback returns "Not found" instead of guessing, cutting hallucination risk at the source.
- Clean modular design (`config` / `indexer` / `retriever` / `api`) exposed via FastAPI (`/health`, `/retrieve`, `/query`).

`FastAPI` `Qdrant` `InLegalBERT` `TF-IDF` `RRF` `Cross-Encoder`

#### [AI-Powered Personalized Learning & Skill Gap Navigator](#)
An end-to-end career guidance platform combining classical ML and RAG.
- Resume parsing + automated skill-gap analysis + personalized learning roadmaps.
- Random Forest for career path prediction, K-Means clustering for user persona segmentation.
- RAG-based AI Career Mentor using FAISS + LLM integration (Groq/Gemini) for grounded interview prep.

`FastAPI` `FAISS` `Scikit-learn` `LangChain` `Groq`

#### [AI for Real-Time Sign Language Translation](#)
Real-time gesture recognition and translation system, published as peer-reviewed research.
- Hand tracking and gesture recognition using MediaPipe and OpenCV.
- Text-to-speech integration for real-time, accessible communication.
- Published in **IJAMRED** (Dec 2025) — [read the paper](https://ijamred.com/volume1/issue4/IJAMRED-V1I4P56.pdf).

`Python` `OpenCV` `MediaPipe` `Flask`

---

### Research Publication

**AI for Real-Time Translation of Sign Language**
*International Journal of Advanced Multidisciplinary Research and Educational Development (IJAMRED)* — Dec 2025
[Read the paper](https://ijamred.com/volume1/issue4/IJAMRED-V1I4P56.pdf)

---

### GitHub Analytics

<p align="center">
  <img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Dpjaiswal&theme=tokyonight" />
  <img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Dpjaiswal&theme=tokyonight" />
</p>

<p align="center">
  <img width="70%" src="https://streak-stats.demolab.com?user=Dpjaiswal&theme=tokyonight&hide_border=true" />
</p>

---

### 2026 Goals

- Ship enterprise-grade agentic AI systems in production
- Deepen expertise in deterministic RAG evaluation and guardrails
- Contribute to open-source GenAI tooling
- Publish additional research in applied AI

---

<p align="center">
<b>Building reliable AI systems — grounded, auditable, production-ready.</b>
</p>
