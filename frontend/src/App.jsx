import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Activity, PlusCircle } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

function App() {
  const [formData, setFormData] = useState({
    previousDayCases: 45,
    temperature: 22.5,
    holidayStatus: 0,
    fluCases: 12,
    dayOfWeek: 0,
    humidity: 50,
    aqi: 45,
    localEvent: 0
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Predict initial state on load
    handlePredict();
  }, []);

  const handlePredict = async (e) => {
    if (e) e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:5000/api/predict', formData);
      setResult(res.data);
    } catch (error) {
      console.error("Prediction error", error);
    }
    setLoading(false);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: Number(value) }));
  };

  return (
    <div style={{ padding: '40px 5%', maxWidth: '1400px', margin: '0 auto' }}>
      
      {/* HEADER */}
      <header style={{ marginBottom: '40px', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '10px' }}>
          <Activity size={36} style={{ display: 'inline', verticalAlign: 'middle', marginRight: '10px', color: '#3b82f6' }}/>
          Hospital Emergency Forecast
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.1rem' }}>
          AI-powered predictive analytics for modern healthcare resource management.
        </p>
      </header>

      {/* MAIN GRID */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '30px' }}>
        
        {/* LEFT COL: INPUTS */}
        <div className="glass-card">
          <h2 style={{ marginBottom: '24px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <PlusCircle size={24} color="#3b82f6"/> Current Conditions
          </h2>
          <form onSubmit={handlePredict}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
              <div className="input-group">
                <label>Previous Day Cases</label>
                <input type="number" name="previousDayCases" value={formData.previousDayCases} onChange={handleChange} />
              </div>
              <div className="input-group">
                <label>Flu Cases</label>
                <input type="number" name="fluCases" value={formData.fluCases} onChange={handleChange} />
              </div>
              
              <div className="input-group">
                <label>Temperature (°C)</label>
                <input type="number" step="0.1" name="temperature" value={formData.temperature} onChange={handleChange} />
              </div>
              <div className="input-group">
                <label>Humidity (%)</label>
                <input type="number" name="humidity" value={formData.humidity} onChange={handleChange} />
              </div>

              <div className="input-group">
                <label>Air Quality Index</label>
                <input type="number" name="aqi" value={formData.aqi} onChange={handleChange} />
              </div>
              <div className="input-group">
                <label>Day of Week</label>
                <select name="dayOfWeek" value={formData.dayOfWeek} onChange={handleChange}>
                  <option value={0}>Monday</option>
                  <option value={1}>Tuesday</option>
                  <option value={2}>Wednesday</option>
                  <option value={3}>Thursday</option>
                  <option value={4}>Friday</option>
                  <option value={5}>Saturday</option>
                  <option value={6}>Sunday</option>
                </select>
              </div>

              <div className="input-group">
                <label>Holiday?</label>
                <select name="holidayStatus" value={formData.holidayStatus} onChange={handleChange}>
                  <option value={0}>No</option>
                  <option value={1}>Yes</option>
                </select>
              </div>
              <div className="input-group">
                <label>Local Event?</label>
                <select name="localEvent" value={formData.localEvent} onChange={handleChange}>
                  <option value={0}>No</option>
                  <option value={1}>Yes</option>
                </select>
              </div>
            </div>
            <button type="submit" className="btn-predict" style={{ marginTop: '16px' }}>
              {loading ? 'Predicting...' : 'Predict'}
            </button>
          </form>
        </div>

        {/* RIGHT COL: RESULTS & CHARTS */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '30px' }}>
          
          {/* RESULT CARD */}
          <div className="glass-card" style={{ borderTop: '4px solid #ef4444', textAlign: 'center', padding: '40px 20px' }}>
             <h3 style={{ color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '10px' }}>
               Expected Emergency Admissions
             </h3>
             <div style={{ fontSize: '5rem', fontWeight: 800, color: '#ef4444', lineHeight: 1 }}>
               {result ? result.prediction : '--'}
             </div>
             <p style={{ marginTop: '10px', color: 'var(--text-muted)' }}>Patients</p>
          </div>

          {/* IMPACT CHART */}
          {result && result.impact && (
            <div className="glass-card" style={{ flexGrow: 1 }}>
              <h3 style={{ marginBottom: '20px' }}>Model Feature Impact</h3>
              <div style={{ width: '100%', height: '250px' }}>
                <ResponsiveContainer>
                  <BarChart data={result.impact} layout="vertical" margin={{ left: 40, right: 20 }}>
                    <XAxis type="number" hide />
                    <YAxis dataKey="feature" type="category" axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} width={120}/>
                    <Tooltip cursor={{fill: 'rgba(255,255,255,0.05)'}} contentStyle={{background: '#1e293b', border: 'none', borderRadius: '8px'}} />
                    <Bar dataKey="weight" radius={[0, 4, 4, 0]}>
                      {result.impact.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.weight > 0 ? '#3b82f6' : '#ef4444'} />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          )}

        </div>
      </div>

    </div>
  );
}

export default App;
