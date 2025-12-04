# UPI Fraud Detector — Hackathon MVP

**One-line:** Real-time detection of suspicious UPI transactions (micro-verification, fake refunds, QR-swap, impersonation) using rule-based heuristics + lightweight ML.

**Status:** Prototype / Hackathon demo — Streamlit UI, synthetic dataset generator, rule engine, IsolationForest anomaly detector.

---

## Contents
- `app/` — main app code (Streamlit demo + detection logic)
- `data/` — (ignored) store CSVs or generated datasets here (do not commit)
- `models/` — (ignored) trained model files (joblib, h5)
- `notebooks/` — optional EDA / experiments
- `scripts/` — data generation & utility scripts
- `requirements.txt` — Python dependencies
- `.gitignore` — recommended ignore rules

---

## Quick demo (run locally, 3 minutes)
1. Clone repo:
   ```bash
   git clone <your-repo-url>
   cd upi-fraud-detector
