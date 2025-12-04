UPI Transaction Fraud Detector (The 8th Mile Hackathon Build)
"Because losing money to a QR code scam shouldn't be a thing."

Hey! Thanks for checking out our submission for the 8th Mile Hackathon.

We decided to tackle something that annoys (and scares) pretty much everyone: UPI Fraud. You know those "accidentally sent you money" scams or the shady QR codes? We built a prototype to catch those in real-time before the money actually leaves your account.

💡 The Big Idea
We didn't want to just build a simple rule-checker. Scammers are smart, so our code needs to be smarter. We built a Hybrid Engine that thinks in two ways:

The "By the Book" Cop (Rule Engine): Checks for obvious red flags we know about, like micro-transactions meant to verify an account or fake refund patterns.

The "Gut Feeling" Cop (Machine Learning): We trained an IsolationForest model to look at the data and spot weird anomalies that don't fit the usual patterns, even if they pass the specific rules.

🎨 What's inside?
A Live Dashboard: We whipped up a UI using Streamlit. It visualizes the transaction flow so you can actually see the fraud getting flagged.

Synthetic Data: obviously, we don't have access to private bank records (we’d be in jail). So, we wrote a script to generate realistic-looking transaction data to train our model.

Hybrid Logic: The cool part is how the Rule Engine and the ML model talk to each other to give a final "Safe" or "Suspicious" verdict.

🧩 The Tech Stack
We kept it lean and mean for the hackathon:

Python does the heavy lifting.

Streamlit handles the frontend (because who has time for React in a 24h hackathon?).

Scikit-Learn powers the anomaly detection.

Pandas manages the messy data.

🗺️ A Tour of the Code
If you're diving into the files, here's where everything lives:

app/ 👉 Start here. This has the main dashboard code and the detection logic.

scripts/ 👉 The tools we used to create the fake data.

notebooks/ 👉 Our digital scratchpad. This is where we messed around with the data and tested the ML models before moving them to the app.

models/ & data/ 👉 (Git ignored) These hold the trained model and CSVs.
