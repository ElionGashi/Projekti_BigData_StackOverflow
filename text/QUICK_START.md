# 🚀 Quick Start Guide

Get the Stack Overflow Data Dashboard up and running in 2 minutes!

## One-Time Setup

### 1. Install Python Dependencies
```bash
cd /Users/eliongashi/Projekti_BigData
pip install flask flask-cors
```

### 2. Install Node/React Dependencies
```bash
cd frontend
npm install
```

## Running the Dashboard

### Terminal 1: Start Flask Backend
```bash
cd /Users/eliongashi/Projekti_BigData
python app.py
```

You should see:
```
✅ Data loaded successfully!
🚀 Starting Flask server...
 * Running on http://127.0.0.1:5000
```

### Terminal 2: Start React Frontend
```bash
cd /Users/eliongashi/Projekti_BigData/frontend
npm start
```

The dashboard will automatically open at `http://localhost:3000`

## What You'll See

✅ **Summary Cards** - Total questions, answers, tags, and average score
✅ **Line Charts** - Question volume and answer rates over time
✅ **Bar Charts** - Average scores and response times
✅ **Pie Chart** - Top 8 tags distribution
✅ **Data Tables** - Top 10 questions and 20 most popular tags

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Failed to load data" | Make sure Flask is running on port 5000 |
| Port 5000 already in use | Close the other process or use `python app.py --port 5001` |
| No data in dashboard | Verify CSV files exist in `data/` folder |
| Blank charts | Wait a few seconds for data to load, then refresh browser |

## File Structure

```
Projekti_BigData/
├── app.py                    ← Flask API server
├── requirements.txt          ← Python packages
├── data/                     ← CSV data files
│   ├── Questions.csv
│   ├── Answers.csv
│   └── Tags.csv
└── frontend/                 ← React dashboard
    └── src/
        ├── Dashboard.jsx     ← Main component
        ├── Dashboard.css     ← Styling
        └── App.js
```

## API Endpoints

- `http://localhost:5000/api/summary` - Overall stats
- `http://localhost:5000/api/yearly-analysis` - Trends by year
- `http://localhost:5000/api/top-questions` - Top 20 questions
- `http://localhost:5000/api/top-tags` - Top 20 tags

---

📚 For detailed info, see `DASHBOARD_SETUP.md`
