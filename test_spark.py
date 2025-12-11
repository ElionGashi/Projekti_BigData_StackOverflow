from datetime import datetime

import numpy as np
import pandas as pd

# --- I. KONFIGURIMI DHE NGARKIMI I TË DHËNAVE ---

QUESTIONS_FILE = "data/Questions.csv"
ANSWERS_FILE = "data/Answers.csv"

print("--- TENTATIVE PER LEXIMIN E TE DHENAVE ---")
print(
    f"Duke lexuar skedarët CSV nga disku lokal: {QUESTIONS_FILE} dhe {ANSWERS_FILE}..."
)

try:
    # 1. Ngarkoni Questions.csv me kodim tolerant
    # Zgjidhim problemin e UnicodeDecodeError
    questions_df = pd.read_csv(QUESTIONS_FILE, encoding="latin-1")

    # 2. Ngarkoni Answers.csv me kodim tolerant
    answers_df = pd.read_csv(ANSWERS_FILE, encoding="latin-1")

    print("✅ Ngarkimi i të dhënave u krye me sukses!")
    print(f"Questions (rreshta): {len(questions_df):,}")
    print(f"Answers (rreshta): {len(answers_df):,}")

except FileNotFoundError as e:
    print(f"\nNDODHI NJE GABIM GJATE LEXIMIT TE SKEDARIT: {e}")
    print(
        "SIGUROHUNI që skedarët 'Questions.csv' dhe 'Answers.csv' të jenë direkt në direktoriumin 'data/'."
    )
    exit()

# ------------------------------------------------------------------
# II. KODI I ANALIZËS PËRFUNDIMTARE (Llogaritja e Treguesve)
# ------------------------------------------------------------------

# 1. Rregullimi i Kolonave të Datës
print("\nDuke kryer analizën e të dhënave...")
questions_df["CreationDate"] = pd.to_datetime(questions_df["CreationDate"])
answers_df["CreationDate"] = pd.to_datetime(answers_df["CreationDate"])

# 2. Llogaritja e Kohës së Përgjigjes (Response Time)
# Gjeni datën e përgjigjes së parë për çdo pyetje
# Kjo është mënyra më efikase për të gjetur radhën e parë (idxmin)
first_answer = answers_df.loc[answers_df.groupby("ParentId")["CreationDate"].idxmin()][
    ["ParentId", "CreationDate"]
]
first_answer.rename(columns={"CreationDate": "FirstAnswerDate"}, inplace=True)

# Bashkoni Questions me datën e përgjigjes së parë
merged_df = questions_df.merge(
    first_answer, left_on="Id", right_on="ParentId", how="left"
)

# Llogaritni Response Time në orë
merged_df["ResponseTime_Hours"] = (
    merged_df["FirstAnswerDate"] - merged_df["CreationDate"]
).dt.total_seconds() / 3600

# 3. Analiza Sipas Vitit
merged_df["Year"] = merged_df["CreationDate"].dt.year

# Gruponi dhe llogaritni të 3 Treguesit: Volumi, Cilësia, Latenca
analysis_results = (
    merged_df.groupby("Year")
    .agg(
        # TREGUESI A: Volumi (Total Questions)
        Total_Questions=("Id", "count"),
        # TREGUESI B: Cilësia (Avg Score)
        Average_Score=("Score", "mean"),
        # TREGUESI C: Latenca (Avg Response Time)
        Avg_Response_Time_Hours=("ResponseTime_Hours", "mean"),
        # Metrika Plotësuese: Answer Rate
        Questions_Answered=("FirstAnswerDate", "count"),
    )
    .reset_index()
)

# Llogaritni Përqindjen e Përgjigjeve (Answer Rate)
analysis_results["Answer_Rate_Percent"] = (
    analysis_results["Questions_Answered"] / analysis_results["Total_Questions"] * 100
).round(2)

# Fshini kolonën e panevojshme dhe formatoni
analysis_results.drop(columns=["Questions_Answered"], inplace=True)
analysis_results["Average_Score"] = analysis_results["Average_Score"].round(2)
analysis_results["Avg_Response_Time_Hours"] = analysis_results[
    "Avg_Response_Time_Hours"
].round(2)

print("\n✅ REZULTATET E ANALIZËS PËRFUNDIMTARE:")
print(analysis_results.to_markdown(index=False))

print("\nProcesi i përfundoi me sukses.")
