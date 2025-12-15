import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  LineChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import './Dashboard.css';

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [yearlyAnalysis, setYearlyAnalysis] = useState([]);
  const [topQuestions, setTopQuestions] = useState([]);
  const [topTags, setTopTags] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_BASE_URL = 'http://localhost:5000/api';

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [summaryRes, yearlyRes, questionsRes, tagsRes] = await Promise.all([
          axios.get(`${API_BASE_URL}/summary`),
          axios.get(`${API_BASE_URL}/yearly-analysis`),
          axios.get(`${API_BASE_URL}/top-questions`),
          axios.get(`${API_BASE_URL}/top-tags`)
        ]);

        setSummary(summaryRes.data);
        setYearlyAnalysis(yearlyRes.data);
        setTopQuestions(questionsRes.data);
        setTopTags(tagsRes.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to load dashboard data. Make sure the Flask server is running on port 5000.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="dashboard-container loading">
        <div className="spinner"></div>
        <p>Loading dashboard data...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="dashboard-container error">
        <div className="error-message">
          <h2>⚠️ Error</h2>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8', '#82CA9D', '#FFC658', '#FF7C7C'];

  return (
    <div className="dashboard-container">
      {/* Header */}
      <header className="dashboard-header">
        <h1>📊 Stack Overflow Data Analysis Dashboard</h1>
        <p>Comprehensive insights and analytics</p>
      </header>

      {/* Summary Cards */}
      {summary && (
        <div className="summary-cards">
          <div className="card">
            <div className="card-icon">❓</div>
            <div className="card-content">
              <h3>Total Questions</h3>
              <p className="card-value">{summary.total_questions?.toLocaleString() || 'N/A'}</p>
            </div>
          </div>
          <div className="card">
            <div className="card-icon">💬</div>
            <div className="card-content">
              <h3>Total Answers</h3>
              <p className="card-value">{summary.total_answers?.toLocaleString() || 'N/A'}</p>
            </div>
          </div>
          <div className="card">
            <div className="card-icon">🏷️</div>
            <div className="card-content">
              <h3>Unique Tags</h3>
              <p className="card-value">{summary.unique_tags?.toLocaleString() || 'N/A'}</p>
            </div>
          </div>
          <div className="card">
            <div className="card-icon">⭐</div>
            <div className="card-content">
              <h3>Avg Score</h3>
              <p className="card-value">{summary.avg_score?.toFixed(2) || 'N/A'}</p>
            </div>
          </div>
        </div>
      )}

      {/* Charts Section */}
      <div className="charts-grid">
        {/* Yearly Analysis Chart */}
        {yearlyAnalysis.length > 0 && (
          <div className="chart-container full-width">
            <h2>📈 Questions Over Time</h2>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={yearlyAnalysis}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Year" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="Total_Questions" stroke="#0088FE" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Average Score Trend */}
        {yearlyAnalysis.length > 0 && (
          <div className="chart-container half-width">
            <h2>⭐ Average Score Trend</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={yearlyAnalysis}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Year" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="Average_Score" fill="#00C49F" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Response Time Trend */}
        {yearlyAnalysis.length > 0 && (
          <div className="chart-container half-width">
            <h2>⏱️ Avg Response Time</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={yearlyAnalysis}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Year" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="Avg_Response_Time_Hours" fill="#FFBB28" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Top Tags Pie Chart */}
        {topTags.length > 0 && (
          <div className="chart-container half-width">
            <h2>🏷️ Top 8 Tags Distribution</h2>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={topTags.slice(0, 8)}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ Tag, Count }) => `${Tag} (${Count})`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="Count"
                >
                  {topTags.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Answer Rate */}
        {yearlyAnalysis.length > 0 && (
          <div className="chart-container half-width">
            <h2>💯 Answer Rate Over Time</h2>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={yearlyAnalysis}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Year" />
                <YAxis domain={[0, 100]} />
                <Tooltip formatter={(value) => `${value.toFixed(2)}%`} />
                <Line type="monotone" dataKey="Answer_Rate_Percent" stroke="#FF8042" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>

      {/* Top Questions Table */}
      {topQuestions.length > 0 && (
        <div className="table-container">
          <h2>🌟 Top 10 Questions by Score</h2>
          <div className="table-scroll">
            <table className="data-table">
              <thead>
                <tr>
                  <th>Score</th>
                  <th>Title</th>
                  <th>Answers</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {topQuestions.slice(0, 10).map((q, idx) => (
                  <tr key={idx} className={idx % 2 === 0 ? 'even' : 'odd'}>
                    <td className="score-cell"><strong>⭐ {q.Score}</strong></td>
                    <td className="title-cell">{q.Title?.substring(0, 60)}...</td>
                    <td>{q.AnswerCount || 0}</td>
                    <td className="date-cell">{new Date(q.CreationDate).toLocaleDateString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Top Tags Table */}
      {topTags.length > 0 && (
        <div className="table-container">
          <h2>🏷️ Top 20 Tags</h2>
          <div className="tags-grid">
            {topTags.slice(0, 20).map((tag, idx) => (
              <div key={idx} className="tag-item">
                <span className="tag-name">{tag.Tag}</span>
                <span className="tag-count">{tag.Count?.toLocaleString()}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="dashboard-footer">
        <p>© 2024 Stack Overflow Data Analysis Dashboard | Data powered by Stack Overflow</p>
      </footer>
    </div>
  );
};

export default Dashboard;
