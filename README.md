# Stack Overflow Data Analysis Dashboard

A modern, full-stack web application for analyzing Stack Overflow data with beautiful visualizations and real-time analytics.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js 14+ and npm
- Stack Overflow CSV data files in `data/` folder

### Setup (One-Time)
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies
cd frontend && npm install
```

### Run the Dashboard
**Terminal 1 - Backend:**
```bash
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend && npm start
```

The dashboard will open automatically at `http://localhost:3000`

## 📊 Features

### Interactive Visualizations
- **5 Interactive Charts** - Questions volume, scores, response times, tag distribution, answer rates
- **4 Summary Cards** - Total questions, answers, tags, average score
- **2 Data Tables** - Top questions and popular tags
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Real-time Data** - Parallel API loading with caching

### Dashboard Elements
1. **Questions Over Time** (Line Chart) - Volume trends by year
2. **Average Score Trend** (Bar Chart) - Quality evolution
3. **Response Time Trend** (Bar Chart) - Answer speed analysis
4. **Top Tags Distribution** (Pie Chart) - 8 most popular tags
5. **Answer Rate** (Line Chart) - Percentage of answered questions
6. **Summary Cards** - Key metrics at a glance
7. **Top Questions Table** - 10 highest-scoring questions
8. **Tags Grid** - 20 most frequently used tags

## 🔌 API Endpoints

```
GET /api/summary              - Overall statistics
GET /api/yearly-analysis      - Year-by-year trends
GET /api/top-questions        - Top 20 questions by score
GET /api/top-tags             - Top 20 most used tags
GET /api/health               - Server health check
GET /api/tag-analysis/<tag>   - Analysis for specific tag
```

## 📁 Project Structure

```
Projekti_BigData/
├── app.py                      # Flask API server
├── requirements.txt            # Python dependencies
├── QUICK_START.md             # Fast setup guide
├── DASHBOARD_SETUP.md         # Detailed documentation
├── IMPLEMENTATION_SUMMARY.md  # Technical overview
├── VISUAL_GUIDE.md            # Architecture diagrams
├── data/
│   ├── Questions.csv
│   ├── Answers.csv
│   └── Tags.csv
└── frontend/                  # React application
    ├── package.json
    └── src/
        ├── Dashboard.jsx      # Main dashboard component
        ├── Dashboard.css      # Styling
        └── App.js
```

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0** - REST API server
- **Pandas** - Data processing
- **Python 3.7+** - Backend logic

### Frontend
- **React 19** - UI framework
- **Recharts** - Interactive charts
- **Axios** - HTTP client
- **CSS3** - Styling & animations

## 🎨 Design Features

- **Modern Gradient** - Purple/blue gradient backgrounds
- **Responsive Layout** - Auto-adjusts to screen size
- **Smooth Animations** - Hover effects and transitions
- **Loading States** - Spinner while fetching data
- **Error Handling** - Helpful error messages
- **Dark Footer** - Professional styling

## 📊 Data Processing

The Flask backend automatically:
1. Loads CSV files (Questions, Answers, Tags)
2. Parses dates and converts data types
3. Calculates response times (question to first answer)
4. Groups data by year
5. Computes aggregations (counts, averages, percentages)
6. Caches results in memory for fast API responses

## 🐛 Troubleshooting

### "Failed to load data" Error
- Ensure Flask is running: `http://localhost:5000/api/health`
- Verify CSV files exist in `data/` folder
- Check that data files have correct encoding (latin-1)

### Port Already in Use
```bash
# Use different ports
python app.py --port 5001
PORT=3001 npm start
```
Then update `API_BASE_URL` in `Dashboard.jsx`

### No Data Showing
- Check browser console (F12) for errors
- Verify CSV column names match expectations
- Clear browser cache (Ctrl+Shift+R)

## 📚 Documentation

- **QUICK_START.md** - 2-minute setup guide
- **DASHBOARD_SETUP.md** - Detailed features & customization
- **IMPLEMENTATION_SUMMARY.md** - Technical architecture
- **VISUAL_GUIDE.md** - System diagrams & data flow

## 🔄 Development

### Backend
```bash
# Changes auto-reload (debug mode enabled)
python app.py
```

### Frontend
```bash
# Hot reload on file changes
cd frontend && npm start
```

## 🚀 Production Build

### Frontend
```bash
cd frontend
npm run build
# Static files in frontend/build/
```

### Backend
```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

## 📈 Key Metrics

- **Volume** - Questions per year trend
- **Quality** - Average question scores over time
- **Performance** - Average response time (hours to first answer)
- **Engagement** - Answer rate percentage by year
- **Popularity** - Top tags and questions by score

## ✨ Features Highlights

✅ Real-time data loading
✅ 5 different chart types
✅ Fully responsive design
✅ Server-side caching
✅ Error handling
✅ Loading states
✅ Mobile optimized
✅ Cross-browser compatible

## 🤝 Customization

### Change Colors
Edit color scheme in `frontend/src/Dashboard.css`:
```css
/* Primary Gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add More Charts
Use Recharts in `frontend/src/Dashboard.jsx`:
```javascript
<ResponsiveContainer width="100%" height={300}>
  <LineChart data={data}>
    {/* chart config */}
  </LineChart>
</ResponsiveContainer>
```

### Extend API
Add new endpoints in `app.py`:
```python
@app.route("/api/new-endpoint", methods=["GET"])
def new_endpoint():
    # Your logic
    return jsonify(data)
```

## 📊 Dataset Info

The dashboard analyzes Stack Overflow data including:
- **Questions** - Problem statements, scores, creation dates
- **Answers** - Responses to questions, timestamps
- **Tags** - Programming language and technology tags

## 🎓 Learning Resources

- [React Documentation](https://react.dev)
- [Recharts Gallery](https://recharts.org)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Pandas Documentation](https://pandas.pydata.org)

## 📝 Notes

- Data is loaded into memory on Flask startup
- Charts are fully responsive and touch-friendly
- Dates displayed in local browser timezone
- Scores calculated using Stack Overflow's official system
- Parallel API requests for optimal performance

## 🚨 Support

For issues, check the documentation:
1. QUICK_START.md - Common setup questions
2. DASHBOARD_SETUP.md - Feature details
3. IMPLEMENTATION_SUMMARY.md - Technical details
4. Browser console (F12) - Error messages

## 📄 License

This project uses Stack Overflow data. Ensure you comply with Stack Overflow's data usage terms.

---

**Ready to analyze?** Run `python app.py` and `npm start` to get started! 🚀📊