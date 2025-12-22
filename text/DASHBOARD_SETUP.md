# Stack Overflow Data Analysis Dashboard

A modern, responsive web dashboard for analyzing Stack Overflow data with beautiful visualizations and real-time analytics.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js 14+ and npm
- Stack Overflow CSV data files (Questions.csv, Answers.csv, Tags.csv)

### Setup Instructions

#### 1. Install Python Backend Dependencies

```bash
cd /Users/eliongashi/Projekti_BigData
pip install -r requirements.txt
```

#### 2. Start the Flask Backend Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

You should see output like:
```
✅ Data loaded successfully!
Questions: X,XXX
Answers: X,XXX,XXX
Tags: XX,XXX
🚀 Starting Flask server...
 * Running on http://127.0.0.1:5000
```

#### 3. In a New Terminal, Start the React Frontend

```bash
cd /Users/eliongashi/Projekti_BigData/frontend
npm start
```

The dashboard will automatically open in your browser at `http://localhost:3000`

## 📊 Dashboard Features

### Summary Cards
- **Total Questions**: Overall count of all questions in the dataset
- **Total Answers**: Complete answer count across all questions
- **Unique Tags**: Number of distinct tags used
- **Average Score**: Mean score of all questions

### Charts & Visualizations

#### 📈 Questions Over Time
Line chart showing question volume trends by year

#### ⭐ Average Score Trend
Bar chart displaying how average question scores have evolved

#### ⏱️ Average Response Time
Bar chart showing the average time from question to first answer

#### 🏷️ Top Tags Distribution
Pie chart showing the distribution of the 8 most popular tags

#### 💯 Answer Rate Over Time
Line chart tracking the percentage of questions that received answers

### Data Tables

#### Top Questions Table
Shows the 10 highest-scoring questions with:
- Score
- Title
- Answer count
- Creation date

#### Top Tags Grid
Visual cards for the 20 most frequently used tags with their usage counts

## 🔌 API Endpoints

The Flask backend provides the following REST API endpoints:

### `/api/summary`
Returns overall statistics
```json
{
  "total_questions": 12345,
  "total_answers": 54321,
  "total_tags": 999,
  "unique_tags": 999,
  "avg_score": 1.23
}
```

### `/api/yearly-analysis`
Returns yearly trends data
```json
[
  {
    "Year": 2008,
    "Total_Questions": 1000,
    "Average_Score": 2.5,
    "Avg_Response_Time_Hours": 24.5,
    "Answer_Rate_Percent": 75.5
  }
]
```

### `/api/top-questions`
Returns top 20 questions by score
```json
[
  {
    "Id": 123,
    "Score": 9999,
    "Title": "Question Title...",
    "CreationDate": "2008-07-31T...",
    "AnswerCount": 15
  }
]
```

### `/api/top-tags`
Returns top 20 most used tags
```json
[
  {
    "Tag": "python",
    "Count": 5000
  }
]
```

### `/api/health`
Health check endpoint
```json
{
  "status": "ok",
  "dataLoaded": true
}
```

## 🎨 Customization

### Changing Colors
Edit `frontend/src/Dashboard.css` to modify the color scheme:
- Primary gradient: `#667eea` to `#764ba2`
- Accent colors: `#0088FE`, `#00C49F`, `#FFBB28`, etc.

### Adding More Charts
Edit `frontend/src/Dashboard.jsx` to add new charts using Recharts components.

### Data File Locations
Update the file paths in `app.py`:
```python
QUESTIONS_FILE = "data/Questions.csv"
ANSWERS_FILE = "data/Answers.csv"
TAGS_FILE = "data/Tags.csv"
```

## 🐛 Troubleshooting

### "Failed to load dashboard data" Error
- Ensure Flask backend is running on port 5000
- Check that data CSV files exist in the `data/` folder
- Verify CORS is enabled (should be automatic)

### Port Already in Use
If port 5000 or 3000 is already in use:

For Flask:
```bash
python app.py --port 5001
```

For React:
```bash
PORT=3001 npm start
```

Then update the API URL in `frontend/src/Dashboard.jsx`:
```javascript
const API_BASE_URL = 'http://localhost:5001/api';
```

### Data Not Loading
1. Verify CSV files are in the `data/` folder
2. Check file encoding (should be latin-1)
3. Ensure column names match expected names
4. Check console for detailed error messages

## 📁 Project Structure

```
Projekti_BigData/
├── app.py                          # Flask backend API
├── requirements.txt                # Python dependencies
├── data/
│   ├── Questions.csv
│   ├── Answers.csv
│   └── Tags.csv
└── frontend/                       # React application
    ├── src/
    │   ├── Dashboard.jsx           # Main dashboard component
    │   ├── Dashboard.css           # Dashboard styles
    │   ├── App.js
    │   ├── App.css
    │   └── index.js
    ├── package.json
    └── public/
```

## 🔧 Development

### Backend Development
1. Make changes to `app.py`
2. Flask will auto-reload on save (debug mode enabled)
3. Test endpoints using Postman or curl:
```bash
curl http://localhost:5000/api/summary
```

### Frontend Development
1. Make changes to React components in `frontend/src/`
2. Browser will hot-reload automatically
3. Open browser DevTools (F12) for debugging

## 📦 Building for Production

### Build React Frontend
```bash
cd frontend
npm run build
```

This creates optimized static files in `frontend/build/`

### Deploy Flask Backend
For production, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

## 📝 Notes

- Data is loaded into memory on Flask startup for performance
- Charts are responsive and work on mobile devices
- All dates are displayed in your local timezone
- Scores are calculated using Stack Overflow's official scoring system

## 🤝 Contributing

Feel free to enhance the dashboard by:
- Adding more visualization types
- Implementing filtering and search
- Adding export functionality (CSV, PDF)
- Creating more detailed analytics views
- Improving mobile responsiveness

## 📄 License

This project uses Stack Overflow data. Ensure you comply with Stack Overflow's data usage terms.

---

**Happy Analyzing! 📊✨**