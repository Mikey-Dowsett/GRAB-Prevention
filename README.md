# GRAB Prevention
### Guarding RAG Against Breaches

> A defensive cybersecurity project focused on detecting and preventing prompt injection attacks against Retrieval-Augmented Generation (RAG) systems.

---

## Project Overview

RAG (Retrieval-Augmented Generation) chatbots supplement AI responses with domain-specific documents — internal business data, policy files, knowledge bases, and more. This power comes with a risk: **prompt injection attacks** can trick the model into revealing information it was never meant to expose.

**GRAB Prevention** studies how these attacks work and builds practical defenses to ensure users can only extract information the system is authorized to share — even when the model has access to sensitive source material internally.

---

## The Problem

A RAG system may have access to sensitive files (e.g., HR records, financial data, internal policy documents) to answer legitimate queries. Without proper guardrails, a malicious user can craft inputs that:

- Extract raw document content the model should summarize but not quote
- Bypass access-level restrictions through indirect prompt manipulation
- Trick the model into ignoring its system prompt or safety instructions
- Leak confidential data through seemingly innocuous follow-up questions

---

## Project Scope

| Item | Details |
|---|---|
| **Domain** | AI/ML Security — Prompt Injection Defense |
| **System** | RAG-based chatbot with a document knowledge base |
| **Threat** | Prompt injection leading to unauthorized data extraction |
| **Approach** | Defensive — detection, mitigation, and evaluation |
| **Timeline** | ~1 month |

---

## Team

| Role | Responsibilities |
|---|---|
| **Project Lead** | Coordinates timeline, manages GitHub, leads documentation and final report |
| **Threat Analyst** | Researches and documents prompt injection attack techniques; builds the initial threat model |
| **Defense Engineer** | Designs and implements input/output filtering, guardrails, and system prompt hardening |
| **RAG Systems Developer** | Builds and maintains the test RAG environment (document store + LLM pipeline) |
| **Evaluation & QA** | Designs test cases, runs red-team prompts against defenses, tracks results and metrics |

---

## Assets Being Protected

- Source documents used to ground RAG responses (business data, policy files, etc.)
- The system prompt and model instructions
- Access control logic governing what information the model is permitted to surface
- Query logs (prevent leakage through observable side channels)

---

## Initial Threat Assumptions

- Attackers are external users with access to the chat interface but no direct access to the document store
- Attackers will attempt to extract document content through crafted natural language inputs
- The model is assumed to be a commercially available LLM (e.g., GPT-class) with no fine-tuning
- Some attacks may be multi-turn (building context across several messages before extracting data)

---

## Repository Structure

```
grab-prevention/
├── README.md
├── docs/
│   ├── project-charter.md
│   ├── threat-model.md
│   └── diagrams/
├── rag-system/          # Test RAG environment
├── defenses/            # Input/output filtering, guardrails
├── attacks/             # Red-team prompt test cases
└── evaluation/          # Scoring, metrics, and results
```

---

## Getting Started

> Setup instructions will be added as the RAG test environment is built out.

---

## References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [MITRE ATLAS — Prompt Injection](https://atlas.mitre.org/)
- [Greshake et al. — Indirect Prompt Injection Threats](https://arxiv.org/abs/2302.12173)
