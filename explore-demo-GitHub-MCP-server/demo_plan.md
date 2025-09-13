# 📋 GitHub MCP Server Demo – Final Integrated Plan (25 Tools)

## 🎯 Objective

* Showcase the **25 most useful GitHub MCP Server tools**.
* Use **1 main demo repo** (and optionally a fork) to keep setup simple.
* Flow naturally through the developer lifecycle:
  **Repo → Branches → PRs → Issues → Notifications → Security → Collaboration**.
* Provide **ready-to-use code/config** so the demo produces visible results in GitHub UI + via MCP commands.

---

## 🛠 Demo Environment

### Repo A (Main Demo Repo)

* Created live using `create_repository`.
* Includes:

  ```plaintext
  demo-repo/
   ├─ app.js               # simple hello world with unsafe code
   ├─ package.json         # vulnerable dependency (lodash@4.17.19)
   ├─ .env                 # dummy AWS secret for secret scanning
   ├─ README.md
   └─ .github/
       ├─ workflows/
       │   ├─ ci.yml       # basic CI for PRs
       │   └─ codeql.yml   # CodeQL analysis
       └─ dependabot.yml   # daily dependency check
  ```

### Repo B (Optional Fork)

* Created using `fork_repository`.
* Used to demo external collaboration (optional).

---

## 🚀 Demo Flow (with Tools)

### **Stage 1 – Repo & Branch Setup**

1. **create\_repository** → create demo repo.
2. **create\_branch** → make `feature-1` branch.
3. **list\_branches** → confirm branches.
4. **create\_or\_update\_file** → add `app.js`.
5. **push\_files** → commit multiple files (`package.json`, workflows).
6. **delete\_file** → remove a file (demo cleanup).

---

### **Stage 2 – Pull Requests & Reviews**

7. **create\_pull\_request** → open PR from `feature-1`.
8. **get\_pull\_request\_diff** → show code changes.
9. **get\_pull\_request\_files** → list files changed.
10. **create\_and\_submit\_pull\_request\_review** → add review notes.
11. **request\_copilot\_review** → AI-assisted code review.
12. **merge\_pull\_request** → merge into `main`.

---

### **Stage 3 – Issues & Collaboration**

13. **create\_issue** → open bug issue.
14. **update\_issue** → edit issue details.
15. **add\_issue\_comment** → add follow-up comment.
16. **assign\_copilot\_to\_issue** → assign Copilot for assistance.

---

### **Stage 4 – Notifications & Productivity**

17. **list\_notifications** → show all notifications.
18. **dismiss\_notification** → dismiss one notification.
19. **mark\_all\_notifications\_read** → clear all at once.
20. **manage\_repository\_notification\_subscription** → watch/unwatch repo programmatically.

---

### **Stage 5 – Security & Code Insights (Expanded Security Story)**

**(Core highlight of the demo – full flow)**

#### Part 1 – Static Analysis (CodeQL)

21. **list\_code\_scanning\_alerts** → list CodeQL alerts.
22. **get\_code\_scanning\_alert** → drill into one alert.

#### Part 2 – Secrets Detection

23. **list\_secret\_scanning\_alerts** → show leaked secret alerts.
24. **get\_secret\_scanning\_alert** → inspect one secret alert.

#### Part 3 – Proactive Code Search

25. **search\_code** → scan repo for insecure patterns (e.g., `eval(`, `API_KEY`).

#### Part 4 – Dependency Security (Dependabot)

* `.github/dependabot.yml` + vulnerable `lodash@4.17.19`.
* GitHub triggers **Dependabot alert + auto-PR**.

---

### **Stage 6 – Fork & Cross-Repo Work (Optional)**

* **fork\_repository** → fork repo into Repo B.
* Show PRs/issues across repos.

---

## 🔄 Flow Summary

1. **Start with repo creation** (Stage 1).
2. **Show PR workflow** (Stage 2).
3. **Add issues/comments for collaboration** (Stage 3).
4. **Manage notifications** (Stage 4).
5. **Dive into security story** (Stage 5: static analysis → secrets → proactive search → dependency updates).
6. **Optionally demo collaboration via fork** (Stage 6).

---

## 📦 Deliverables to Prepare

* **Repo bootstrap files** (`app.js`, `package.json`, `.env`, workflows, dependabot config).
* **Sample MCP commands** for each feature.
* **Expected outputs** (alerts, PRs, notifications, reviews).
* **Troubleshooting notes** (Dependabot delays, CodeQL scan timing, secret scanning restrictions).

---

✅ This way, all 25 features are covered in a **single narrative** inside one repo, and the **Security & Code Insights block** stands out as the “wow” section.

