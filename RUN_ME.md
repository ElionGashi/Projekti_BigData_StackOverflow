# 🚀 RUN ME - Start Your Dashboard in Seconds!

## Quick Start (Choose Your Operating System)

### 🍎 **macOS & Linux**
```bash
cd /Users/eliongashi/Projekti_BigData
./start-dashboard.sh
```

**That's it!** The dashboard will automatically:
- ✅ Start Flask backend on http://localhost:5000
- ✅ Start React frontend on http://localhost:3000
- ✅ Open your browser automatically

### 🪟 **Windows**
```bash
cd C:\Users\YourUsername\Projekti_BigData
start-dashboard.bat
```

**That's it!** Two windows will open:
- ✅ Flask Backend window
- ✅ React Frontend window
- ✅ Dashboard opens in your browser

---

## 📊 What Happens Next

1. **Flask Backend Starts** (5000)
   - Loads your Stack Overflow CSV data
   - Starts REST API server
   - Shows: `✓ Flask backend started successfully`

2. **React Frontend Starts** (3000)
   - Compiles React application
   - Shows: `✓ React frontend started successfully`
   - Browser opens automatically

3. **Dashboard Loads**
   - Charts load with your data
   - Summary cards display metrics
   - Tables show top questions and tags

---

## 🌐 Access Your Dashboard

**Once started, visit:**
```
http://localhost:3000
```

Or click this link: [http://localhost:3000](http://localhost:3000)

---

## 🛑 Stop the Dashboard

### macOS & Linux
- Press `Ctrl+C` in the terminal

### Windows
- Close the Flask Backend window
- Close the React Frontend window
- Or press `Ctrl+C` in each

---

## ⚠️ Troubleshooting

### "Command not found" on macOS/Linux
```bash
# Make the script executable
chmod +x start-dashboard.sh

# Then run it
./start-dashboard.sh
```

### Ports Already in Use
If port 5000 or 3000 is busy, edit the files:
- `app.py` - Change `port=5000` to `port=5001`
- `frontend/src/Dashboard.jsx` - Update `API_BASE_URL`

### "Python not found"
```bash
# Check if Python is installed
python3 --version

# If not installed, install it from python.org
```

### "Node not found"
```bash
# Check if Node is installed
node --version

# If not installed, install from nodejs.org
```

### Still having issues?
Check the log files:
- **Flask errors**: `/tmp/flask_dashboard.log`
- **React errors**: `/tmp/react_dashboard.log`

Or read: `QUICK_START.md` for manual setup

---

## 📚 What's Inside

Your dashboard includes:
- **5 Interactive Charts** - Questions, scores, response times, tags, answer rates
- **4 Summary Cards** - Total questions, answers, tags, average score
- **2 Data Tables** - Top questions and popular tags
- **Modern Design** - Purple/blue gradient, responsive, smooth animations
- **REST API** - 6 endpoints for data serving
- **Auto Data Caching** - Lightning fast performance

---

## 🎯 Dashboard Features at a Glance

```
📊 Main Dashboard (http://localhost:3000)
├── 📈 Questions Over Time (Line Chart)
├── ⭐ Average Score Trend (Bar Chart)
├── ⏱️ Response Time Trend (Bar Chart)
├── 🏷️ Top Tags Distribution (Pie Chart)
├── 💯 Answer Rate Over Time (Line Chart)
├── 📋 Top 10 Questions Table
└── 🏷️ Top 20 Tags Grid

🔌 API Server (http://localhost:5000/api)
├── /api/summary
├── /api/yearly-analysis
├── /api/top-questions
├── /api/top-tags
├── /api/health
└── /api/tag-analysis/<tag>
```

---

## 💡 Pro Tips

✓ **First Run?** The first startup may take 30-60 seconds for React to compile
✓ **Data Loads Instantly** - All 4 API calls happen in parallel
✓ **Hot Reload** - Change code and it updates automatically (hot reload)
✓ **Dark Mode?** Not yet, but easy to add! See `DASHBOARD_SETUP.md`
✓ **Want More Charts?** See `DASHBOARD_SETUP.md` for customization guide

---

## 🎉 Ready?

### Run This Now:

**macOS/Linux:**
```bash
./start-dashboard.sh
```

**Windows:**
```bash
start-dashboard.bat
```

Then visit: **http://localhost:3000**

---

## 📞 Need Help?

- **Quick Setup Questions**: See `QUICK_START.md`
- **Feature Explanations**: See `DASHBOARD_SETUP.md`
- **Technical Details**: See `IMPLEMENTATION_SUMMARY.md`
- **Architecture Diagrams**: See `VISUAL_GUIDE.md`
- **Navigation Help**: See `INDEX.md`

---

**Happy analyzing!** 📊✨