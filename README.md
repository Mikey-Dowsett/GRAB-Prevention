# GRAB Prevention
### Guarding RAG Against Breaches

> A defensive cybersecurity project focused on detecting and preventing prompt injection attacks against Retrieval-Augmented Generation (RAG) systems.

---

## Team

| Role | Responsibilities |
|---|---|
| **Project Lead** | dogaes |
| **Threat Analyst** | ashdoda |
| **Defense Engineer** | LukasViski0603 |
| **RAG Systems Developer** | Mikey-Dowsett |
| **Evaluation & QA** | mikeumkc |

---

## The Domain

Security of LLM Applications

---

## Project Overview

RAG (Retrieval-Augmented Generation) chatbots supplement AI responses with domain-specific documents — internal business data, policy files, knowledge bases, and more. This power comes with a risk: **prompt injection attacks** can trick the model into revealing information it was never meant to expose.

**GRAB Prevention** studies how these attacks work and builds practical defenses to ensure users can only extract information the system is authorized to share — even when the model has access to sensitive source material internally.

---

## System Description
The system is a Retrieval-Augmented Generation (RAG) chatbot that retrieves information from an internal document store and generates responses using a large language model. User queries are processed through a defensive AI layer before interacting with protected data.

---

## Objective
The objective of this project is to explore and evaluate a prototype AI-based method for detecting suspicious inputs and demonstrating how they can be handled before reaching critical parts of a system.

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

## The Problem

A RAG system may have access to sensitive files (e.g., HR records, financial data, internal policy documents) to answer legitimate queries. Without proper guardrails, a malicious user can craft inputs that:

- Extract raw document content the model should summarize but not quote
- Bypass access-level restrictions through indirect prompt manipulation
- Trick the model into ignoring its system prompt or safety instructions
- Leak confidential data through seemingly innocuous follow-up questions

---

## Assets Being Protected

The following assets are considered sensitive and must be protected from unauthorized access or leakage:
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
## System Overview Diagram

```text
                +----------------------+
                |   User / Attacker    |
                |  sends input/request |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Input Interface    |
                |  Web app / API / UI  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Defensive AI Module  |
                | Detection / Analysis |
                +----------+-----------+
                           |
            +--------------+--------------+
            |                             |
            v                             v
+-------------------------+   +--------------------------+
| Alert / Block / Log     |   | Normal Request Allowed   |
| suspicious activity     |   | if no threat detected    |
+------------+------------+   +------------+-------------+
             |                             |
             v                             v
+--------------------------------------------------------+
|                Protected Assets                        |
| model, training data, logs, user accounts, server      |
+--------------------------------------------------------+
```


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
