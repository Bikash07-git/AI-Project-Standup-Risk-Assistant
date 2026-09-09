import { useEffect, useMemo, useState } from 'react'
import './App.css'

const initialForm = {
  employee_name: 'Aisha Patel',
  team: 'Product',
  project: 'Project Alpha',
  completed: 'Completed stakeholder summary and refreshed roadmap milestones.',
  today: 'Reviewing sprint risks and aligning execution priorities with engineering.',
  blocker: '',
  dependency: '',
  additional_context: 'No significant blockers.'
}

const defaultData = {
  employees: [],
  projects: [],
  updates: [],
  metrics: {
    adoption_rate: 68,
    update_completion_rate: 91,
    confirmation_rate: 86,
    correction_rate: 14,
    effort_reduction: 42,
    demo_label: 'Demo / Illustrative Data'
  }
}

const navItems = ['Dashboard', 'Updates', 'Projects', 'Risks & Blockers', 'AI Copilot', 'Leadership Metrics', 'Settings']

function App() {
  const [activeView, setActiveView] = useState('Dashboard')
  const [form, setForm] = useState(initialForm)
  const [analysis, setAnalysis] = useState(null)
  const [demoData, setDemoData] = useState(defaultData)
  const [dashboard, setDashboard] = useState(null)
  const [leadership, setLeadership] = useState(null)
  const [copilotQuery, setCopilotQuery] = useState('Which projects are currently at risk?')
  const [copilotResponse, setCopilotResponse] = useState('')
  const [filters, setFilters] = useState({ team: 'All', project: 'All', employee: 'All', risk: 'All', blocker: 'All', date: 'All' })
  const [statusMessage, setStatusMessage] = useState('')
  const [reviewItems, setReviewItems] = useState([
    { id: 1, title: 'Waiting for database credentials', status: 'Pending', label: 'Needs review' },
    { id: 2, title: 'Customer data dependency', status: 'Escalated', label: 'Manager attention required' }
  ])

  useEffect(() => {
    const loadData = async () => {
      try {
        const [demoResponse, dashboardResponse, leadershipResponse] = await Promise.all([
          fetch('http://localhost:8000/demo-data'),
          fetch('http://localhost:8000/dashboard'),
          fetch('http://localhost:8000/leadership')
        ])

        const demo = await demoResponse.json()
        const dashboardSummary = await dashboardResponse.json()
        const metrics = await leadershipResponse.json()

        setDemoData(demo)
        setDashboard(dashboardSummary)
        setLeadership(metrics)
      } catch (error) {
        console.error('Failed to load demo data', error)
      }
    }

    loadData()
  }, [])

  const filteredUpdates = useMemo(() => {
    const rows = demoData.updates ?? []
    return rows.filter((row) => {
      const employee = demoData.employees.find((person) => person.id === row.employee_id)
      const project = demoData.projects.find((item) => item.id === row.project_id)
      const isTeamMatch = filters.team === 'All' || employee?.team === filters.team
      const isProjectMatch = filters.project === 'All' || project?.name === filters.project
      const isEmployeeMatch = filters.employee === 'All' || employee?.name === filters.employee
      const riskMatch = filters.risk === 'All' || row.riskLevel === filters.risk
      const blockerMatch = filters.blocker === 'All' || (filters.blocker === 'Blocked' ? Boolean(row.blocker) : !row.blocker)
      const dateMatch = filters.date === 'All' || row.date === filters.date
      return isTeamMatch && isProjectMatch && isEmployeeMatch && riskMatch && blockerMatch && dateMatch
    })
  }, [demoData, filters])

  const handleInputChange = (event) => {
    const { name, value } = event.target
    setForm((previous) => ({ ...previous, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
      const result = await response.json()
      setAnalysis(result.analysis)
      setStatusMessage('AI analysis generated successfully.')
    } catch (error) {
      console.error('Unable to analyze update', error)
      setStatusMessage('Demo mode is active; using deterministic analysis fallback.')
      setAnalysis({
        blockers: [{
          title: 'Waiting for database credentials',
          dependency: 'Database/Admin team',
          impact: 'Dashboard delivery may be delayed',
          recommended_action: 'Follow up with the database administrator',
          confidence: 91,
          source: 'fallback'
        }],
        risk_level: 'HIGH',
        recommendation: 'Escalate database access request',
        summary: 'Analysis generated using fallback rules.',
        confidence: 91,
        needs_manager_review: true
      })
    }
  }

  const handleNormalize = async () => {
    const text = `${form.completed} ${form.today} ${form.blocker}`.trim()
    if (!text) return
    const response = await fetch('http://localhost:8000/normalize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    })
    const result = await response.json()
    if (result.normalized) {
      setForm((previous) => ({
        ...previous,
        completed: result.completed || previous.completed,
        today: result.today || previous.today,
        blocker: result.blocker || previous.blocker,
        dependency: result.dependency || previous.dependency,
        additional_context: result.additional_context || previous.additional_context
      }))
      setStatusMessage('Free-form update normalized to the standard structure.')
    }
  }

  const handleCopilot = () => {
    const query = copilotQuery.toLowerCase()
    if (query.includes('risk')) {
      setCopilotResponse('Customer Portal is at highest risk because two critical blockers remain unresolved, both tied to database access and customer data dependencies.')
      return
    }
    if (query.includes('blocked') || query.includes('who')) {
      setCopilotResponse('Marcus Lee and Nina Gomez are blocked by database access, and Liam Chen remains blocked by the customer data dependency.')
      return
    }
    if (query.includes('dependency') || query.includes('follow up')) {
      setCopilotResponse('Immediate attention is needed for Database/Admin team and Customer Data team. The recommended follow-up is to escalate access and confirm customer data delivery today.')
      return
    }
    if (query.includes('project alpha') || query.includes('summarize')) {
      setCopilotResponse('Project Alpha is stable but has one unresolved dependency affecting rollout. Most work is on track, and the main risk is delayed customer data input for final validation.')
      return
    }
    setCopilotResponse('I can answer questions about risks, blockers, dependency owners, and project status using the current demo data.')
  }

  const healthyStatus = dashboard ? dashboard.project_health : 'YELLOW'
  const summaryCards = [
    { label: 'Updates Received', value: dashboard?.updates_received ?? 12 },
    { label: 'Completed Tasks', value: dashboard?.completed_tasks ?? 8 },
    { label: 'Active Blockers', value: dashboard?.active_blockers ?? 3 },
    { label: 'High Risks', value: dashboard?.high_risks ?? 2 }
  ]

  const projectNames = demoData.projects.map((project) => project.name)
  const teamNames = ['All', ...new Set(demoData.employees.map((employee) => employee.team))]
  const employeeNames = ['All', ...demoData.employees.map((employee) => employee.name)]

  const updateReviewStatus = async (itemId, nextStatus) => {
    try {
      const response = await fetch('http://localhost:8000/reviews', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ update_id: itemId, status: nextStatus, reviewed_by: 'manager', edited_value: null })
      })
      if (response.ok) {
        const result = await response.json()
        setReviewItems((previous) =>
          previous.map((item) =>
            item.id === itemId ? { ...item, status: nextStatus, label: result.status } : item
          )
        )
        setStatusMessage(`Review saved: ${nextStatus}.`)
      }
    } catch (error) {
      console.error('Failed to save review state', error)
      setReviewItems((previous) =>
        previous.map((item) =>
          item.id === itemId ? { ...item, status: nextStatus, label: nextStatus } : item
        )
      )
      setStatusMessage(`Review action saved locally: ${nextStatus}.`)
    }
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand-block">
          <div className="brand-mark">AI</div>
          <div>
            <h1>Project Stand-up</h1>
            <p>Risk Assistant</p>
          </div>
        </div>
        <nav className="nav-list">
          {navItems.map((item) => (
            <button
              key={item}
              className={activeView === item ? 'nav-item active' : 'nav-item'}
              onClick={() => setActiveView(item)}
              type="button"
            >
              {item}
            </button>
          ))}
        </nav>

        <div className="demo-banner">
          Demo Mode
          <span>AI provider fallback enabled</span>
        </div>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div>
            <p className="eyebrow">Central Operations</p>
            <h2>AI Project Stand-up & Risk Assistant</h2>
          </div>
          <div className="topbar-actions">
            <span className="status-pill success">{healthyStatus} health</span>
            <button type="button" className="primary-btn">Export Summary</button>
          </div>
        </header>

        {statusMessage && <div className="status-toast">{statusMessage}</div>}

        {activeView === 'Dashboard' && (
          <>
            <section className="summary-grid">
              {summaryCards.map((card) => (
                <div key={card.label} className="summary-card">
                  <span>{card.label}</span>
                  <strong>{card.value}</strong>
                </div>
              ))}
            </section>

            <section className="panel-grid">
              <div className="panel panel-large">
                <div className="section-header">
                  <h3>Project Health</h3>
                  <span className="risk-badge yellow">{healthyStatus}</span>
                </div>
                <p className="project-health-text">
                  {dashboard?.project_health_reason || '2 unresolved dependencies are affecting delivery. Priority needs follow-up with both database access and customer data owners.'}
                </p>
                <div className="project-health-metrics">
                  <div>
                    <small>Completed</small>
                    <strong>8 tasks</strong>
                  </div>
                  <div>
                    <small>In Progress</small>
                    <strong>7 tasks</strong>
                  </div>
                  <div>
                    <small>High Risk</small>
                    <strong>2 items</strong>
                  </div>
                </div>
              </div>

              <div className="panel panel-small">
                <div className="section-header">
                  <h3>Critical Blockers</h3>
                </div>
                <ul className="stack-list">
                  {dashboard?.critical_blockers?.map((item) => (
                    <li key={`${item.employee}-${item.blocker}`}>
                      <strong>{item.employee}</strong>
                      <span>{item.blocker}</span>
                    </li>
                  )) ?? []}
                </ul>
                <div className="escalation-box">
                  <strong>Escalation logic</strong>
                  <span>{dashboard?.escalation_rules?.join(' • ') || 'Blocker persists > 2 days • Risk = HIGH • Critical dependency unresolved'}</span>
                </div>
              </div>
            </section>

            <section className="content-grid">
              <div className="panel">
                <div className="section-header">
                  <h3>Risks</h3>
                </div>
                <div className="risk-list">
                  <div className="risk-row danger"><span>High</span><small>Customer Portal blocked by access dependency</small></div>
                  <div className="risk-row warning"><span>Medium</span><small>Customer data dependency affecting validation</small></div>
                  <div className="risk-row ok"><span>Low</span><small>Project Alpha progressing with minor monitoring</small></div>
                </div>
              </div>

              <div className="panel">
                <div className="section-header">
                  <h3>Dependencies</h3>
                </div>
                <ul className="stack-list compact">
                  <li><strong>Database/Admin team</strong><span>Access approval pending</span></li>
                  <li><strong>Customer Data team</strong><span>Delivery delayed</span></li>
                  <li><strong>Security review</strong><span>Cleared</span></li>
                </ul>
              </div>
            </section>

            <section className="panel">
              <div className="section-header">
                <h3>AI Recommended Actions</h3>
              </div>
              <ol className="action-list">
                {dashboard?.recommended_actions?.map((action, index) => (
                  <li key={action}>{`${index + 1}. ${action}`}</li>
                )) ?? []}
              </ol>
            </section>
          </>
        )}

        {activeView === 'Updates' && (
          <section className="two-column-layout">
            <div className="panel">
              <div className="section-header">
                <h3>Employee Update</h3>
                <button type="button" className="secondary-btn" onClick={handleNormalize}>Normalize Free-form</button>
              </div>
              <form className="update-form" onSubmit={handleSubmit}>
                <div className="input-row">
                  <label>
                    Name
                    <input name="employee_name" value={form.employee_name} onChange={handleInputChange} />
                  </label>
                  <label>
                    Team
                    <input name="team" value={form.team} onChange={handleInputChange} />
                  </label>
                </div>
                <div className="input-row">
                  <label>
                    Project
                    <input name="project" value={form.project} onChange={handleInputChange} />
                  </label>
                </div>
                <label>
                  What did you complete yesterday?
                  <textarea name="completed" value={form.completed} onChange={handleInputChange} rows="3" />
                </label>
                <label>
                  What are you working on today?
                  <textarea name="today" value={form.today} onChange={handleInputChange} rows="3" />
                </label>
                <label>
                  What is blocked?
                  <input name="blocker" value={form.blocker} onChange={handleInputChange} placeholder="E.g. Waiting for database credentials" />
                </label>
                <label>
                  What help or dependency do you need?
                  <input name="dependency" value={form.dependency} onChange={handleInputChange} placeholder="E.g. Database/Admin team" />
                </label>
                <label>
                  Additional context
                  <textarea name="additional_context" value={form.additional_context} onChange={handleInputChange} rows="2" />
                </label>
                <button type="submit" className="primary-btn full-width">Analyze Update</button>
              </form>
            </div>

            <div className="panel analysis-panel">
              <div className="section-header">
                <h3>AI Analysis</h3>
              </div>
              {analysis ? (
                <>
                  <div className="analysis-meta-row">
                    <span>Risk: {analysis.risk_level}</span>
                    <span>Confidence: {analysis.confidence}%</span>
                  </div>
                  <div className="analysis-block">
                    <h4>Summary</h4>
                    <p>{analysis.summary}</p>
                  </div>
                  <div className="analysis-block">
                    <h4>Blockers</h4>
                    {analysis.blockers?.length ? (
                      analysis.blockers.map((item) => (
                        <div key={item.title} className="review-card">
                          <p><strong>{item.title}</strong></p>
                          <p>Dependency: {item.dependency}</p>
                          <p>Impact: {item.impact}</p>
                          <div className="review-actions">
                            <button type="button" onClick={() => updateReviewStatus(1, 'Confirmed')}>Confirm</button>
                            <button type="button" onClick={() => updateReviewStatus(1, 'Edited')}>Edit</button>
                            <button type="button" onClick={() => updateReviewStatus(1, 'Rejected')}>Reject</button>
                            <button type="button" onClick={() => updateReviewStatus(1, 'Resolved')}>Resolved</button>
                          </div>
                        </div>
                      ))
                    ) : (
                      <p>No blockers detected.</p>
                    )}
                  </div>
                  <div className="analysis-block">
                    <h4>Recommended action</h4>
                    <p>{analysis.recommendation}</p>
                  </div>
                </>
              ) : (
                <div className="empty-state">Submit an employee update to see AI analysis.</div>
              )}
            </div>
          </section>
        )}

        {activeView === 'Projects' && (
          <section className="panel">
            <div className="section-header">
              <h3>Project Overview</h3>
            </div>
            <div className="project-list">
              {demoData.projects.map((project) => (
                <div key={project.id} className="project-card">
                  <h4>{project.name}</h4>
                  <p>Owner: {project.owner}</p>
                  <p>Team: {project.team}</p>
                  <span className="risk-badge yellow">Needs attention</span>
                </div>
              ))}
            </div>
          </section>
        )}

        {activeView === 'Risks & Blockers' && (
          <section className="panel">
            <div className="section-header">
              <h3>Blocker & Risk Intelligence</h3>
            </div>
            <div className="filter-grid">
              <select value={filters.team} onChange={(event) => setFilters((previous) => ({ ...previous, team: event.target.value }))}>
                {teamNames.map((team) => <option key={team} value={team}>{team === 'All' ? 'All teams' : team}</option>)}
              </select>
              <select value={filters.project} onChange={(event) => setFilters((previous) => ({ ...previous, project: event.target.value }))}>
                <option value="All">All projects</option>
                {projectNames.map((project) => <option key={project} value={project}>{project}</option>)}
              </select>
              <select value={filters.employee} onChange={(event) => setFilters((previous) => ({ ...previous, employee: event.target.value }))}>
                {employeeNames.map((employee) => <option key={employee} value={employee}>{employee === 'All' ? 'All employees' : employee}</option>)}
              </select>
              <select value={filters.risk} onChange={(event) => setFilters((previous) => ({ ...previous, risk: event.target.value }))}>
                <option value="All">All risk levels</option>
                <option value="HIGH">High</option>
                <option value="MEDIUM">Medium</option>
                <option value="LOW">Low</option>
              </select>
              <select value={filters.blocker} onChange={(event) => setFilters((previous) => ({ ...previous, blocker: event.target.value }))}>
                <option value="All">All blocker states</option>
                <option value="Blocked">Blocked</option>
                <option value="Unblocked">Unblocked</option>
              </select>
            </div>
            <div className="update-list">
              {filteredUpdates.map((row) => {
                const employee = demoData.employees.find((person) => person.id === row.employee_id)
                const project = demoData.projects.find((item) => item.id === row.project_id)
                return (
                  <div key={`${row.employee_id}-${row.date}`} className="update-item">
                    <div className="update-head">
                      <strong>{employee?.name}</strong>
                      <span className="risk-badge danger">{row.riskLevel ?? 'MEDIUM'}</span>
                    </div>
                    <p>{project?.name} • {employee?.team}</p>
                    <p>Completed: {row.completed}</p>
                    <p>Blocked: {row.blocker || 'None'}</p>
                    <p>Dependency: {row.dependency || 'Not reported'}</p>
                  </div>
                )
              })}
            </div>
          </section>
        )}

        {activeView === 'AI Copilot' && (
          <section className="panel">
            <div className="section-header">
              <h3>AI Project Copilot</h3>
            </div>
            <div className="copilot-box">
              <textarea value={copilotQuery} onChange={(event) => setCopilotQuery(event.target.value)} rows="3" />
              <button type="button" className="primary-btn" onClick={handleCopilot}>Ask AI</button>
            </div>
            <div className="analysis-block">
              <h4>Answer</h4>
              <p>{copilotResponse || 'Ask a question to get status-based answers from the current project data.'}</p>
            </div>
          </section>
        )}

        {activeView === 'Leadership Metrics' && (
          <section className="panel">
            <div className="section-header">
              <h3>Leadership Metrics</h3>
              <span className="demo-tag">{leadership?.demo_label || 'Demo / Illustrative Data'}</span>
            </div>
            <div className="leadership-grid">
              <div className="metric-card"><span>Adoption Rate</span><strong>{leadership?.adoption_rate ?? 65}%</strong></div>
              <div className="metric-card"><span>Update Completion Rate</span><strong>{leadership?.update_completion_rate ?? 91}%</strong></div>
              <div className="metric-card"><span>Blocker Confirmation Rate</span><strong>{leadership?.blocker_confirmation_rate ?? 86}%</strong></div>
              <div className="metric-card"><span>AI Correction Rate</span><strong>{leadership?.ai_correction_rate ?? 14}%</strong></div>
              <div className="metric-card"><span>Manager Time Saved</span><strong>{leadership?.manager_time_saved_hours ?? 18} hrs</strong></div>
              <div className="metric-card"><span>High-Risk Escalation Rate</span><strong>{leadership?.high_risk_escalation_rate ?? 32}%</strong></div>
              <div className="metric-card"><span>Recurring Blocker Rate</span><strong>{leadership?.recurring_blocker_rate ?? 27}%</strong></div>
              <div className="metric-card"><span>Updates Reviewed</span><strong>{leadership?.updates_reviewed_percent ?? 74}%</strong></div>
            </div>
          </section>
        )}

        {activeView === 'Settings' && (
          <section className="panel">
            <div className="section-header">
              <h3>Configuration</h3>
            </div>
            <ul className="stack-list compact">
              <li><strong>AI Provider</strong><span>Demo deterministic mode</span></li>
              <li><strong>Context retention</strong><span>Recent update history enabled</span></li>
              <li><strong>Human validation</strong><span>Review required for low-confidence results</span></li>
              <li><strong>Escalation rules</strong><span>Blocker persists >2 days or HIGH risk triggers manager attention</span></li>
            </ul>
          </section>
        )}
      </main>
    </div>
  )
}

export default App
