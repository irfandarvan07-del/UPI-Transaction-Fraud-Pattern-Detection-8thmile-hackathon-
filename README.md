# UPI Transaction Fraud Detector (The 8th Mile Hackathon Build)
"Because losing money to a QR code scam shouldn't be a thing."
Hey! Thanks for checking out our submission for the 8th Mile Hackathon. We decided to tackle something that annoys (and scares) pretty much everyone: UPI Fraud. You know those "accidentally sent you money" scams or the shady QR codes? We built a prototype to catch those in real-time before the money actually leaves your account.

##  💡 The Big Idea
We didn't want to just build a simple rule-checker. Scammers are smart, so our code needs to be smarter. We built a Hybrid Engine that thinks in two ways:

The "By the Book" Cop (Rule Engine): Checks for obvious red flags we know about, like micro-transactions meant to verify an account or fake refund patterns. Built in C++ for blazing-fast performance.
The "Gut Feeling" Cop (Machine Learning): We trained an IsolationForest model to look at the data and spot weird anomalies that don't fit the usual patterns, even if they pass the specific rules.


###    What's Inside?

A Live Dashboard: We whipped up a UI using HTML/CSS/JavaScript with Python handling the backend API. It visualizes the transaction flow so you can actually see the fraud getting flagged in real-time.
Synthetic Data: Obviously, we don't have access to private bank records (we'd be in jail). So, we wrote a script to generate realistic-looking transaction data to train our model.
Hybrid Logic: The cool part is how the C++ Rule Engine and the Python ML model talk to each other via REST API to give a final "Safe" or "Suspicious" verdict.


(IMP) The Tech Stack
We kept it lean and mean for the hackathon:
Backend:

C++ does the heavy lifting for rule-based fraud detection (fast, efficient, production-ready)
Python powers the ML anomaly detection engine
Flask/FastAPI bridges the C++ and Python services via REST API

Frontend:

HTML/CSS for the UI structure and styling
JavaScript for interactivity and real-time updates
Chart.js or similar for data visualization

ML & Data:

Scikit-Learn powers the anomaly detection
Pandas manages the messy data
NumPy for numerical operations


🗺️ A Tour of the Code
If you're diving into the files, here's where everything lives:
upi-fraud-detector/
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── CMakeLists.txt
├── data/
│   └── sample_txns.csv
├── cpp/
│   ├── src/
│   │   ├── main.cpp
│   │   ├── csv_reader.h
│   │   ├── csv_reader.cpp
│   │   ├── rules.h
│   │   ├── rules.cpp
│   │   ├── detector.h
│   │   └── detector.cpp
│   └── build/         # created by CMake (should be in .gitignore)
├── app/
│   └── upi_ui.py
├── models/
│   └── model.joblib   # optional (add to .gitignore unless small)
├── scripts/
│   ├── generate_dataset.py
│   └── train_model.py
├── notebooks/
│   └── train.ipynb    # optional EDA/training notebook
└── .streamlit/
    └── secrets.toml.example




Top-level

.gitignore — (already provided). Ignore virtualenvs, model files, data, .streamlit/secrets.toml, build/, etc. Must commit.

README.md — (already provided). Project overview, run instructions, demo steps, etc. Must commit.

LICENSE — pick MIT or your favorite license. Must commit.

requirements.txt — (already provided). E.g. streamlit pandas scikit-learn joblib supabase-py python-Levenshtein sendgrid (keep minimal). Must commit.

CMakeLists.txt — (already provided). For building the C++ binary. Must commit.

data/

sample_txns.csv — (already provided). Small synthetic dataset you can run immediately. Must commit for demo reproducibility.

Contains headers: txn_id,timestamp,from_vpa,to_vpa,amount,message,is_new_payee[,severity,why].

Note: any large datasets should go outside the repo or be stored in cloud (Supabase storage / Google Drive).

cpp/

cpp/src/main.cpp — C++ main program (provided). Reads CSV and outputs flagged txns. Must commit.

cpp/src/csv_reader.h / csv_reader.cpp — simple CSV reader (provided). Must commit.

cpp/src/rules.h / rules.cpp — rule definitions (provided). Must commit.

cpp/src/detector.h / detector.cpp — detector and z-score logic (provided). Must commit.

cpp/build/ — build output (do not commit; add to .gitignore).

This C++ code is your engineering core to demo local high-performance detection.

app/

app/upi_ui.py — Streamlit UI (provided).

Handles CSV upload, displays metrics, filtered table with color-coded severity, chart summaries, transaction detail expander, and email-send button.

Reads model (models/model.joblib) if present; or uses rule + z-score fallback.

Uses st.secrets for email/Supabase keys.

Must commit.

models/

models/model.joblib — trained IsolationForest model (optional).

Do not commit large models. If small (<5–10 MB) you may commit for convenience; otherwise add to .gitignore and upload to Supabase Storage or GitHub Release.

If you include the model in repo, mention it in README.

scripts/

scripts/generate_dataset.py — generator to create synthetic CSV with injected scams (I can provide code if you want). Must commit (helps reproducibility).

scripts/train_model.py — training script to generate features and train IsolationForest and save models/model.joblib. Must commit (or include in notebooks/).

notebooks/

notebooks/train.ipynb — optional Jupyter notebook showing data generation, training, evaluation, and visualizations. Optional but helpful.

.streamlit/

.streamlit/secrets.toml.example — template file (do NOT commit .streamlit/secrets.toml with real credentials). In your repo include secrets.toml.example with placeholders:

[email]
host = "smtp.gmail.com"
port = "587"
username = "your.email@gmail.com"
password = "APP_PASSWORD_HERE"

[sendgrid]
api_key = "SG.xxxxx"
from_email = "alerts@example.com"

[supabase]
url = "https://xyz.supabase.co"
key = "public-anon-key-or-service-role-key"


Instruct collaborators to copy to .streamlit/secrets.toml locally or add secrets to Streamlit Cloud UI before deploy.

Extra helpful files (optional)

.github/ (optional): GitHub Actions workflow to run linters/tests. Not required for hackathon.

docs/: screenshots, demo flows.

deploy/: deployment notes/scripts (optional).



this is not the final over viwe plz wait


t
