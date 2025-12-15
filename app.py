import sys

import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Load Data ---
QUESTIONS_FILE = "data/Questions.csv"
ANSWERS_FILE = "data/Answers.csv"
TAGS_FILE = "data/Tags.csv"

try:
    questions_df = pd.read_csv(QUESTIONS_FILE, encoding="latin-1")
    answers_df = pd.read_csv(ANSWERS_FILE, encoding="latin-1")
    tags_df = pd.read_csv(TAGS_FILE, encoding="latin-1")
    tags_df.columns = ["Id", "Tag"]
    print("✅ Data loaded successfully!")
except Exception as e:
    print(f"Error loading data: {e}")
    sys.exit(1)

# --- Data Processing ---
questions_df["CreationDate"] = pd.to_datetime(questions_df["CreationDate"])
answers_df["CreationDate"] = pd.to_datetime(answers_df["CreationDate"])

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

merged_df["Year"] = merged_df["CreationDate"].dt.year

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

analysis_results.sort_values(by="Year", inplace=True)
analysis_results["Answer_Rate_Percent"] = (
    analysis_results["Questions_Answered"] / analysis_results["Total_Questions"] * 100
).round(2)

analysis_results.drop(columns=["Questions_Answered"], inplace=True)
analysis_results["Average_Score"] = analysis_results["Average_Score"].round(2)
analysis_results["Avg_Response_Time_Hours"] = analysis_results[
    "Avg_Response_Time_Hours"
].round(2)

analysis_results["Volume_Change_%"] = (
    analysis_results["Total_Questions"].pct_change() * 100
).round(2)

analysis_results["ResponseTime_Change_%"] = (
    analysis_results["Avg_Response_Time_Hours"].pct_change() * 100
).round(2)

# --- API Routes ---


@app.route("/api/yearly-analysis", methods=["GET"])
def get_yearly_analysis():
    """Get yearly analysis data"""
    data = analysis_results.fillna(0).to_dict(orient="records")
    return jsonify(data)


@app.route("/api/summary", methods=["GET"])
def get_summary():
    """Get overall summary statistics"""
    first_year = analysis_results.iloc[0]
    last_year = analysis_results.iloc[-1]

    return jsonify(
        {
            "total_questions": int(questions_df["Id"].count()),
            "total_answers": int(answers_df["Id"].count()),
            "total_tags": int(tags_df["Tag"].nunique()),
            "avg_score": float(questions_df["Score"].mean()),
            "first_year": int(first_year["Year"]),
            "last_year": int(last_year["Year"]),
            "first_year_questions": int(first_year["Total_Questions"]),
            "last_year_questions": int(last_year["Total_Questions"]),
        }
    )


@app.route("/api/top-questions", methods=["GET"])
def get_top_questions():
    """Get top 20 questions by score"""
    top_questions = (
        questions_df.sort_values(by="Score", ascending=False).head(20).copy()
    )
    # Calculate answer counts from answers_df
    answer_counts = answers_df.groupby("ParentId").size().to_dict()
    top_questions["AnswerCount"] = (
        top_questions["Id"].map(answer_counts).fillna(0).astype(int)
    )
    data = top_questions[["Id", "Score", "Title", "CreationDate", "AnswerCount"]].copy()
    data["CreationDate"] = data["CreationDate"].astype(str)
    return jsonify(data.to_dict(orient="records"))


@app.route("/api/top-tags", methods=["GET"])
def get_top_tags():
    """Get top 20 most used tags"""
    top_tags = tags_df["Tag"].value_counts().head(20).reset_index()
    top_tags.columns = ["Tag", "Count"]
    return jsonify(top_tags.to_dict(orient="records"))


@app.route("/api/tag-analysis/<tag_name>", methods=["GET"])
def get_tag_analysis(tag_name):
    """Get analysis for a specific tag"""
    filtered_tags = tags_df[tags_df["Tag"].str.lower() == tag_name.lower()]

    if filtered_tags.empty:
        return jsonify({"error": f"Tag {tag_name} not found"}), 404

    merged_tags = questions_df.merge(
        filtered_tags, left_on="Id", right_on="Id", how="inner"
    )

    top_questions = merged_tags.sort_values(by="Score", ascending=False).head(10)
    data = top_questions[["Id", "Score", "Title", "CreationDate", "AnswerCount"]].copy()
    data["CreationDate"] = data["CreationDate"].astype(str)

    return jsonify(
        {
            "tag": tag_name,
            "total_questions": len(merged_tags),
            "avg_score": float(merged_tags["Score"].mean()),
            "top_questions": data.to_dict(orient="records"),
        }
    )


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "API is running"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
