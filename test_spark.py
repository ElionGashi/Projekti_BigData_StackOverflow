import sys

import pandas as pd

# --- I. KONFIGURIMI DHE NGARKIMI I TË DHËNAVE ---

QUESTIONS_FILE = "data/Questions.csv"
ANSWERS_FILE = "data/Answers.csv"
TAGS_FILE = "data/Tags.csv"

print("--- TENTATIVE PER LEXIMIN E TE DHENAVE ---")
print(
    f"Duke lexuar skedarët CSV nga disku lokal: {QUESTIONS_FILE}, {ANSWERS_FILE}, dhe {TAGS_FILE}..."
)

try:
    questions_df = pd.read_csv(QUESTIONS_FILE, encoding="latin-1")
    answers_df = pd.read_csv(ANSWERS_FILE, encoding="latin-1")
    tags_df = pd.read_csv(TAGS_FILE, encoding="latin-1")

    # Fiksimi i emrave të kolonave në tags_df për t'u siguruar (rasti i vogël vs i madh)
    tags_df.columns = ["Id", "Tag"]  # Sigurohuni që kolonat të quhen 'Id' dhe 'Tag'

    print("✅ Ngarkimi i të dhënave u krye me sukses!")
    print(f"Questions (rreshta): {len(questions_df):,}")
    print(f"Answers (rreshta): {len(answers_df):,}")
    print(f"Tags (rreshta): {len(tags_df):,}")

except Exception as e:
    print(f"\nNDODHI NJE GABIM GJATE LEXIMIT: {e}")
    sys.exit(1)

# ------------------------------------------------------------------
# II. KODI I ANALIZËS PËRFUNDIMTARE (Llogaritja e Treguesve)
# ------------------------------------------------------------------

# 1. Rregullimi i Kolonave të Datës
print("\nDuke kryer analizën e të dhënave...")
questions_df["CreationDate"] = pd.to_datetime(questions_df["CreationDate"])
answers_df["CreationDate"] = pd.to_datetime(answers_df["CreationDate"])

# 2. Llogaritja e Kohës së Përgjigjes (Response Time)
first_answer = answers_df.loc[answers_df.groupby("ParentId")["CreationDate"].idxmin()][
    ["ParentId", "CreationDate"]
]
first_answer.rename(columns={"CreationDate": "FirstAnswerDate"}, inplace=True)

merged_df = questions_df.merge(
    first_answer, left_on="Id", right_on="ParentId", how="left"
)

merged_df["ResponseTime_Hours"] = (
    merged_df["FirstAnswerDate"] - merged_df["CreationDate"]
).dt.total_seconds() / 3600

# 3. Analiza Sipas Vitit
merged_df["Year"] = merged_df["CreationDate"].dt.year

# Gruponi dhe llogaritni të 3 Treguesit: Volumi, Cilësia, Latenca
analysis_results = (
    merged_df.groupby("Year")
    .agg(
        Total_Questions=("Id", "count"),
        Average_Score=("Score", "mean"),
        Avg_Response_Time_Hours=("ResponseTime_Hours", "mean"),
        Questions_Answered=("FirstAnswerDate", "count"),
    )
    .reset_index()
)

# ------------------------------------------------------------------
# III. FORMATIMI, KRAHASIMI DHE PARAQITJA
# ------------------------------------------------------------------

analysis_results.sort_values(by="Year", inplace=True)

# Llogaritni Përqindjen e Përgjigjeve (Answer Rate)
analysis_results["Answer_Rate_Percent"] = (
    analysis_results["Questions_Answered"] / analysis_results["Total_Questions"] * 100
).round(2)

# Fshini kolonën e panevojshme dhe formatoni vlerat numerike
analysis_results.drop(columns=["Questions_Answered"], inplace=True)
analysis_results["Average_Score"] = analysis_results["Average_Score"].round(2)
analysis_results["Avg_Response_Time_Hours"] = analysis_results[
    "Avg_Response_Time_Hours"
].round(2)


# --- PËRMBLEDHJE E VITIT TË PARË ---
first_year_analysis = analysis_results.iloc[0]

print("\n--- PËRMBLEDHJE: VITI I PARË I ANALIZËS (2008) ---")
print(f"Viti i Të Dhënave: {int(first_year_analysis['Year'])}")
print(f"Pyetje Totale (Volumi): {first_year_analysis['Total_Questions']:,}")
print(f"Nota Mesatare (Cilësia): {first_year_analysis['Average_Score']:.2f}")
print(
    f"Koha Mesatare e Përgjigjes (Orë): {first_year_analysis['Avg_Response_Time_Hours']:.2f}"
)
print(
    f"Përqindja e Përgjigjeve (Answer Rate): {first_year_analysis['Answer_Rate_Percent']:.2f}%"
)
print("------------------------------------------")

print("\n--- Analiza e Etiketave (Tags) ---")
print(f"Numri Total i Etiketave Unike (Tags): {tags_df['Tag'].nunique():,}")
print("------------------------------------------")


# --- Analiza Diferenciale (Viti ndaj Vitit Paraardhës) ---
print("\n--- Analiza Diferenciale (Viti ndaj Vitit Paraardhës) ---")

analysis_results["Volume_Change_%"] = (
    analysis_results["Total_Questions"].pct_change() * 100
).round(2)

analysis_results["ResponseTime_Change_%"] = (
    analysis_results["Avg_Response_Time_Hours"].pct_change() * 100
).round(2)

# VËREJTJE: Analiza e AcceptedAnswerId hiqet si e pamundur
print(
    "\n⚠️ VËREJTJE: Analiza e cilësisë së përgjigjeve të pranuara nuk u krye (Kolona 'AcceptedAnswerId' mungon)."
)


# --- Seksioni IV: Analiza e Etiketave (Tags) ---
def analyze_top_questions_by_tag(questions_df, tags_df, tag_name, top_n=10):
    """
    Kryen bashkimin e Questions me Tags, filtron sipas etiketës, dhe shfaq Top N.
    """
    print(f"\n--- Analiza: Top {top_n} Pyetjet me Etiketën <{tag_name}> ---")

    # 1. Filtro vetëm etiketat e dëshiruara nga tags_df
    filtered_tags = tags_df[tags_df["Tag"].str.lower() == tag_name.lower()]

    if filtered_tags.empty:
        print(f"⚠️ Nuk u gjetën pyetje me etiketën <{tag_name}>.")
        return

    # 2. Bashko (JOIN) me questions_df
    merged_tags_df = questions_df.merge(
        filtered_tags, left_on="Id", right_on="Id", how="inner"
    )

    # 3. Rendit sipas Score dhe merr TOP N
    top_questions = merged_tags_df.sort_values(by="Score", ascending=False).head(top_n)

    print(
        f"Pyetje gjithsej të filtruara (me etiketën <{tag_name}>): {len(merged_tags_df):,}"
    )

    # Zgjedhim vetëm kolonat më të rëndësishme
    display_cols = ["Id", "Score", "Title", "CreationDate", "Tag"]

    print(top_questions[display_cols].to_markdown(index=False, floatfmt=".0f"))


# --- PËRDORIMI FINAL I FUNKSIONIT TË ETiKETAVE ---

analyze_top_questions_by_tag(questions_df, tags_df, "python", top_n=10)
analyze_top_questions_by_tag(questions_df, tags_df, "javascript", top_n=5)


# --- REZULTATET FINALE ---
print("\n✅ REZULTATET E ANALIZËS PËRFUNDIMTARE (ME KRAHASIM VJETOR):")
print(analysis_results.to_markdown(index=False, floatfmt=".2f"))

# --- Kërkesa SQL: Top 10 Pyetjet sipas Score (Gjithsej) ---
print("\n--- Kërkesa SQL (Pandas): Top 10 Pyetjet me Score më të Lartë (Gjithsej) ---")
top_10_questions = questions_df.sort_values(by="Score", ascending=False).head(10)

display_cols_top10 = ["Id", "Score", "Title", "CreationDate"]
print(top_10_questions[display_cols_top10].to_markdown(index=False, floatfmt=".0f"))


print("\nProcesi i përfundoi me sukses. Urime!")
