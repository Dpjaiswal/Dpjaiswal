<h1 align="center">Durga Prasad Jaiswal</h1>
<h3 align="center">GenAI Engineer • Production RAG Systems • Agentic AI • LLM Application Development</h3>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=36BCF7&center=true&vCenter=true&width=900&lines=Building+Production-Grade+RAG+Pipelines;Agentic+AI+%7C+Multi-Agent+Systems;Hybrid+Retrieval+%2B+Cross-Encoder+Reranking;FastAPI+%2B+LangGraph+%2B+LangChain;Grounded+LLMs+with+Near-Zero+Hallucination;Scalable+Backend+Engineering;Enterprise+AI+Applications" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/dp-jaiswal/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:dpjaiswal.lkouniv@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://Dpjaiswal.github.io/my-portfolio/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://ijamred.com/volume1/issue4/IJAMRED-V1I4P56.pdf"><img src="https://img.shields.io/badge/Research_Paper-4CAF50?style=for-the-badge&logo=readthedocs&logoColor=white"/></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Dpjaiswal&label=Profile%20Views&color=0e75b6&style=flat-square"/>
</p>

<p align="center">
  <b>4+ Production RAG Systems</b> &nbsp;|&nbsp; 
  <b>40% Retrieval Accuracy Gain</b> (Hybrid + Cross-Encoder) &nbsp;|&nbsp; 
  <b>Published AI Research Paper</b>
</p>

---

# Summary

Dedicated GenAI Engineer specializing in building production-grade RAG pipelines and scalable backend systems. Proven expertise in LLM orchestration, hybrid semantic retrieval, and minimizing model hallucinations through robust guardrail implementation. Committed to bridging complex AI algorithms with high-performance, user-centric applications to deliver measurable operational impact.

---

# Technical Proficiencies

### Languages & Frameworks
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

### GenAI, LLM & Search Engineering
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-FF4F00?style=for-the-badge&logo=diagram&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-FF6B35?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)
![Claude API](https://img.shields.io/badge/Claude_API-D97706?style=for-the-badge&logo=anthropic&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-D13253?style=for-the-badge&logo=qdrant&logoColor=white)
![RAGAS](https://img.shields.io/badge/RAGAS-009688?style=for-the-badge)
![BGE Reranker](https://img.shields.io/badge/BGE_Reranker-8A2BE2?style=for-the-badge)

### Databases, Asynchronous & Cloud Infrastructure
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37B24D?style=for-the-badge&logo=celery&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_(EC2_S3_Lambda_IAM)-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

# Production RAG Architecture Flow

```mermaid
graph LR
    A[User Query] --> B[Two-Stage Hybrid Search: BM25 + Qdrant Dense]
    B --> C[Reciprocal Rank Fusion RRF Merging]
    C --> D[Cross-Encoder Reranking BGE-Reranker-Large]
    D --> E[LangGraph Multi-Agent Workflow & Guardrails]
    E --> F[Grounded & Source-Cited Output Response]
