import re

with open('/Users/akarshaksingh/Desktop/Wellora/client/dashboard.html', 'r') as f:
    text = f.read()

# Make sure we add fetch authorization
fetch_replace = """const response = await fetch('http://localhost:5555/api/upload-report', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: formData
        });"""

text = re.sub(r'const response \= await fetch.*?body\: formData\n\s+\}\);', fetch_replace, text, flags=re.DOTALL)

# Add layout
sidebar_html = """<body>
<div class="d-flex flex-column flex-md-row" style="min-height: 100vh;">
  <!-- Sidebar -->
  <aside style="width: 260px; background: var(--white); border-right: 1px solid var(--border-light); flex-shrink: 0;" class="d-none d-md-flex flex-column">
    <div style="padding: 24px; border-bottom: 1px solid var(--border-light); display: flex; align-items: center; gap: 10px;">
      <div class="logo-icon" style="width: 32px; height: 32px; background: var(--accent-teal); color: white; display: flex; justify-content: center; align-items: center; border-radius: 8px;"><i class="ph ph-heartbeat"></i></div>
      <span style="font-weight: 700; font-size: 1.25rem; color: var(--primary-dark);">Wellora</span>
    </div>
    <nav style="flex: 1; padding: 20px 10px; display: flex; flex-direction: column; gap: 5px;">
      <a href="dashboard.html" style="padding: 12px 16px; border-radius: 8px; color: var(--primary-dark); font-weight: 500; background: rgba(45, 212, 191, 0.1); display: flex; align-items: center; gap: 10px;">
        <i class="ph ph-house"></i> Home
      </a>
      <a href="analysis.html" style="padding: 12px 16px; border-radius: 8px; color: var(--text-gray); font-weight: 500; transition: all 0.2s; display: flex; align-items: center; gap: 10px;" onmouseover="this.style.color='var(--primary-dark)'; this.style.background='rgba(0,0,0,0.02)'" onmouseout="this.style.color='var(--text-gray)'; this.style.background='transparent'">
        <i class="ph ph-chart-line-up"></i> Analysis
      </a>
    </nav>
    <div style="padding: 20px; border-top: 1px solid var(--border-light);">
      <button id="logoutBtnSidebar" class="btn btn-outline" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 10px;">
        <i class="ph ph-sign-out"></i> Logout
      </button>
    </div>
  </aside>

  <!-- Mobile Topbar -->
  <div class="d-md-none" style="background: var(--white); padding: 15px 20px; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
    <a href="dashboard.html" style="font-weight: 700; font-size: 1.2rem; color: var(--primary-dark); display: flex; align-items: center; gap: 8px;">
      <div class="logo-icon" style="width: 28px; height: 28px; background: var(--accent-teal); color: white; display: flex; justify-content: center; align-items: center; border-radius: 6px;"><i class="ph ph-heartbeat"></i></div>
      Wellora
    </a>
    <div style="display: flex; gap: 15px;">
      <a href="analysis.html" style="color: var(--text-gray);"><i class="ph ph-chart-line-up" style="font-size: 24px;"></i></a>
      <button id="logoutBtnMobile" style="background: none; border: none; color: var(--text-gray); cursor: pointer;"><i class="ph ph-sign-out" style="font-size: 24px;"></i></button>
    </div>
  </div>

  <!-- Main Content -->
  <main style="flex: 1; background: var(--bg-light); height: 100vh; overflow-y: auto;">
"""

text = re.sub(r'<body>.*?<div class="dashboard-container">', sidebar_html + '\n<div class="dashboard-container">', text, flags=re.DOTALL)
text = text.replace('</body>', '\n  </main>\n</div>\n<script>document.getElementById("logoutBtnSidebar")?.addEventListener("click", () => { localStorage.removeItem("token"); localStorage.removeItem("user"); window.location.href="login.html"; }); document.getElementById("logoutBtnMobile")?.addEventListener("click", () => { localStorage.removeItem("token"); localStorage.removeItem("user"); window.location.href="login.html"; });</script>\n</body>')

with open('/Users/akarshaksingh/Desktop/Wellora/client/dashboard.html', 'w') as f:
    f.write(text)
