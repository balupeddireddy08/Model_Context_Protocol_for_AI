# GitHub MCP Server Demo: End-to-End Workflow

This document provides a complete, step-by-step guide for demonstrating the capabilities of a GitHub MCP Server using VS Code and Copilot Chat in Agent mode. Each stage covers a different aspect of the software development lifecycle, from repository creation to security scanning and cross-repo collaboration.

## Table of Contents

- [Stage 1 — VS Code + GitHub MCP Server](#stage-1--vs-code--github-mcp-server)
- [Stage 2 — PR & Review Flow](#stage-2--pr--review-flow)
- [Stage 3 — Issues & Collaboration](#stage-3--issues--collaboration)
- [Stage 4 — Notifications & Productivity](#stage-4--notifications--productivity)
- [Stage 5 — Security & Code Insights](#stage-5--security--code-insights)
- [Stage 6 — Fork & Cross-Repo Collaboration](#stage-6--fork--cross-repo-collaboration)

---

# Stage 1 — VS Code + GitHub MCP Server

## What Stage 1 Delivers

* Create a **demo repo** and baseline **Streamlit** app entirely from **VS Code** using:

  * Copilot Chat in **Agent** mode (selecting **MCP Server: GitHub** tools) to call MCP tools:

    * `create_repository`, `create_branch`, `list_branches`, `create_or_update_file`, `push_files` (represented by commit+push), `delete_file`
  * Native VS Code Source Control and Git UI as the fallback, visual verification, and local editing
* Files you can paste into VS Code and commit from the editor
* Exact Copilot Chat prompts and the expected behavior/responses

---

## Preconditions (quick)

* VS Code (latest) installed.
* Git installed locally (for local commits).
* GitHub Copilot extension installed and signed in.
* The **GitHub MCP Server** is enabled/allowed in VS Code Copilot MCP settings (Agent mode).

  * To use MCP tools: open Copilot Chat → select **Agent** → click the **tools** icon → enable/select **MCP Server: GitHub**. ([GitHub Docs][1])

---

## Files for the repo (copy these into VS Code)

Project structure (Stage-1):

```
demo-streamlit/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ README.md
```

### `app.py` (paste into VS Code)

```python
# app.py - Streamlit starter for MCP Server demo (Stage 1)
import streamlit as st

st.set_page_config(page_title="MCP Demo Streamlit", page_icon="🚀", layout="centered")

st.title("MCP Server Demo — Stage 1")
st.markdown("This is a simple Streamlit app used as the demo repo baseline. We'll extend this app in later stages.")

st.sidebar.header("Demo controls (local)")
branch = st.sidebar.text_input("Branch name to create (local)", value="feature-1")
make_change = st.sidebar.button("Make a minor local change")

st.header("Hello, world")
st.write("This app will be extended across stages to demonstrate PRs, reviews, security scans, and automation via the GitHub MCP Server.")

if make_change:
    st.info("Made a small local change. Commit & push using the Source Control panel.")
```

### `requirements.txt`

```
streamlit>=1.0
```

### `.gitignore`

```
.env
__pycache__/
*.pyc
.vscode/
.DS_Store
```

### `README.md`

```markdown
# Demo Streamlit App (MCP Server Workshop - Stage 1)

This repository is the baseline for the MCP Server demo. It contains a minimal Streamlit app (`app.py`) that we'll extend in subsequent stages.

## Run locally
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. streamlit run app.py
```

---

## Exact Copilot Chat (Agent) prompts to call MCP tools

Open **Copilot Chat** in VS Code (title-bar icon) → **Agent** mode → click the **tools** icon and enable **MCP Server: GitHub**. Then paste these prompts one by one into the chat input (the Agent will show tool parameters for you to confirm). For best demo clarity, keep the prompts short and explicit — the Agent will ask for missing parameters if needed.

> Notes: when a tool needs parameters Copilot will show a GUI form (tool chooser) to fill values (e.g., repo name, visibility). Confirm those values and submit.

### 1) Create the repo (`create_repository`)

Copilot prompt:

```
Agent: Use the GitHub MCP Server to create a new repository named "demo-streamlit" with description "MCP Server demo - Stage 1" and make it public.
```

What to expect:

* Copilot will present the `create_repository` tool with fields (name, description, private/public). Confirm **public** and submit.
* The MCP server will create the repo and the Agent will show a success message and the repo URL.
* In VS Code you can open the repo URL (link shown in chat) to verify.

### 2) Create (local) `main` branch and add files (edit in VS Code)

This step is done in VS Code editor + Source Control UI (no tool call needed) — create files in the workspace and commit locally. (You'll later use the Agent to push files if you prefer.)

Suggested Copilot prompt (optional) — to have the Agent create files remotely instead of local editing:

```
Agent: Create a file at path "app.py" with the following content: <paste app.py content>. Put it on branch "main".
```

What to expect:

* The Agent will show the `create_or_update_file` tool with parameters (path, content, commit message, branch). Confirm and the file will be created in the GitHub repo on `main`.
* If you prefer local editing, just paste the files into your VS Code workspace and save them.

### 3) List branches (`list_branches`)

Copilot prompt:

```
Agent: List branches in the repository "demo-streamlit".
```

What to expect:

* Agent will call `list_branches` and return the branches (initially usually `main`). The chat will display the branch list.

### 4) Create a branch `feature-1` (`create_branch`)

Copilot prompt:

```
Agent: Create a branch named "feature-1" in repo "demo-streamlit", based on "main".
```

What to expect:

* Agent will call `create_branch` and confirm creation. The chat will show success and the new branch name.

### 5) Add or update files (`create_or_update_file`)

If you created files locally, use VS Code Source Control to commit and push; if you want the Agent to place files directly in GitHub:
Copilot prompt:

```
Agent: Add file "requirements.txt" with content "streamlit>=1.0" to branch "main" in "demo-streamlit".
```

Or to add `helpers.py` remotely:

```
Agent: Create file "helpers.py" on branch "main" with content:
def greet(name="world"):
    return f"Hello, {name}!"
```

What to expect:

* The Agent will present the `create_or_update_file` tool form with content preview → confirm → file created.

### 6) Push multiple files / commit equivalent (`push_files`)

If you committed locally and want the Agent to push, it will normally call `create_or_update_file` multiple times or use the git-data flow if available. Suggested prompt (Agent will present options):

```
Agent: Commit and push the current workspace files (app.py, requirements.txt, .gitignore, README.md) to branch "main" of "demo-streamlit" with commit message "Initial Streamlit app (Stage 1)".
```

What to expect:

* The Agent uses MCP file/commit tools to create the commit on GitHub and confirm the new commit SHA and repo state.

### 7) List branches again to confirm (`list_branches`)

Copilot prompt (same as step 3):

```
Agent: Show branches in demo-streamlit.
```

Expect to see both `main` and `feature-1`.

### 8) Delete a file remotely (`delete_file`)

Copilot prompt:

```
Agent: Delete file "helpers.py" from branch "main" in repo "demo-streamlit" with message "Delete helpers.py (demo)".
```

What to expect:

* Agent will run `delete_file` and confirm deletion. The chat will show success and updated file list.

---

## How to do the same actions with VS Code UI (fallback & visual verification)

If Agent tools are not available or you want to show manual Git UI:

1. Open your workspace in VS Code containing the files.
2. Use the **Source Control** view (left bar) to stage files, type the commit message, and click the checkmark to commit.
3. Click the three-dot menu → **Push** to push to remote (if remote already set) or choose **Publish Branch** to publish `main` or `feature-1`.
4. Use the **GitHub Repositories** / **GitHub Pull Requests** extension panes (if installed) to view branches, create PRs, open files on GitHub, and manage PRs.

Both approaches — Copilot Agent tool calls and the VS Code Git UI — are visible to the audience and demonstrate how MCP maps to developer actions.

---

## Verification checkpoints (what to show during demo)

* After `create_repository`: Open the repo URL shown by the Agent in the chat and show file list (should be empty until files added).
* After `create_or_update_file` / commit & push: Reload the repo page in the browser and show `app.py`, `requirements.txt`, `.gitignore`, `README.md`.
* After `create_branch`: In the GitHub repo UI show the branch selector → both `main` and `feature-1`.
* After `delete_file`: Show the file no longer present in the repo UI.
* Use Copilot Chat to `list_branches` and show the returned branch list in the chat window.

---

## Example Agent conversation transcript (what you'll actually type)

1. Type: `Agent: Create a repo named "demo-streamlit" with description "MCP Server demo - Stage 1" (public).` → confirm tool parameters → submit.
2. Type: `Agent: Create file "app.py" on branch "main" with the following content:` → paste `app.py` → confirm → submit.
3. Type: `Agent: Create file "requirements.txt" on branch "main" with content "streamlit>=1.0".` → submit.
4. Type: `Agent: Create branch "feature-1" based on "main".` → submit.
5. Type: `Agent: Show branches in demo-streamlit.` → observe the list in chat.
6. Type: `Agent: Delete file "helpers.py" from branch "main".` → submit.

The Agent will show confirmations and links to created resources; click them to open GitHub pages.

(If the Agent asks for missing details, fill the fields — this is part of the MCP elicitation flow.)


[1]: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server?utm_source=chatgpt.com "Using the GitHub MCP Server"
[2]: https://code.visualstudio.com/docs/copilot/customization/mcp-servers?utm_source=chatgpt.com "Use MCP servers in VS Code"
[3]: https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp?utm_source=chatgpt.com "Extending GitHub Copilot Chat with the Model Context Protocol (MCP)"
[4]: https://github.com/github/github-mcp-server?utm_source=chatgpt.com "GitHub's official MCP Server"



# Stage 2 — PR & Review Flow

## What We'll Do in Stage 2

1. Create a new branch `feature-text-analyzer`.
2. Make a meaningful change to the Streamlit app (introduce a **Text Analyzer** widget and helper function).
3. Commit the changes on the feature branch (using either the Agent `create_or_update_file` or VS Code local commit).
4. Create a Pull Request from `feature-text-analyzer` → `main` using the MCP tool `create_pull_request`.
5. Inspect the PR with `get_pull_request_diff` and `get_pull_request_files`.
6. Request a Copilot review using `request_copilot_review`.
7. Add a human-style review with `create_and_submit_pull_request_review` (e.g., request changes or comment).
8. Address minor changes if we want (optional), then **merge** the PR with `merge_pull_request`.

We'll use the `demo-streamlit` repo created in Stage 1 and the `main` branch as the target.

---

## 1) The code change (copy/paste ready)

We'll add a small text-analysis feature to `app.py`: a text area input that counts words, characters, and reports simple duplicate words — visible, demonstrable diff and easy to review.

**New/updated `app.py` content** (replace existing `app.py` on the feature branch):

```python
# app.py - Streamlit starter for MCP Server demo (Stage 2)
import streamlit as st
from collections import Counter
import re

st.set_page_config(page_title="MCP Demo Streamlit", page_icon="🚀", layout="centered")

st.title("MCP Server Demo — Stage 2")
st.markdown("This Streamlit app now includes a small Text Analyzer feature (for PR & review demos).")

st.sidebar.header("Demo controls (local)")
branch_local = st.sidebar.text_input("Branch name to create (local)", value="feature-text-analyzer")
make_change = st.sidebar.button("Make a minor local change")

st.header("Hello, world")
st.write("This app will be extended across stages to demonstrate PRs, reviews, security scans, and automation via the GitHub MCP Server.")

if make_change:
    st.info("Made a small local change. Commit & push using the Source Control panel.")

st.markdown("---")
st.subheader("Text Analyzer")
st.write("Paste or type text below and see basic metrics (word count, character count, most common words).")

text = st.text_area("Enter text to analyze", height=200, placeholder="Paste sample text here...")

def analyze_text(s: str):
    if not s:
        return {"chars": 0, "words": 0, "top_words": []}
    chars = len(s)
    # very small tokenizer: split on non-word chars
    tokens = re.findall(r"\w+", s.lower())
    words = len(tokens)
    freqs = Counter(tokens)
    top = freqs.most_common(5)
    return {"chars": chars, "words": words, "top_words": top}

result = analyze_text(text)

col1, col2 = st.columns(2)
col1.metric("Characters", result["chars"])
col2.metric("Words", result["words"])

st.write("Top words:")
if result["top_words"]:
    for w, c in result["top_words"]:
        st.write(f"- **{w}** — {c} occurrence(s)")
else:
    st.write("_No words yet — type some text above._")
```

> Commit message suggestion: `Add Text Analyzer widget (feature-text-analyzer)`

---

## 2) VS Code + Copilot Agent prompts — exact lines to paste

Open **Copilot Chat** → switch to **Agent mode** → verify **MCP Server: GitHub** tool is enabled (tools icon). Paste the prompts below one at a time and confirm the fields the Agent shows.

### A — Create a feature branch

Type into Agent:

```
Agent: Create a branch named "feature-text-analyzer" in repo "demo-streamlit", based on "main".
```

* The Agent will show a `create_branch` form (repo, base branch, new name). Confirm and submit.
* Expected: chat confirms creation and returns the new branch name.

### B — Add/update `app.py` on the feature branch

Type into Agent (large paste — paste the full `app.py` contents above):

```
Agent: Create or update file "app.py" on branch "feature-text-analyzer" in repo "demo-streamlit" with the following content:
<PASTE THE FULL app.py CONTENT HERE>
Commit message: "Add Text Analyzer widget (feature-text-analyzer)"
```

* The Agent will surface the `create_or_update_file` tool form (path, content preview, commit message, branch). Confirm and submit.
* Expected: Agent returns success with a commit SHA and link to the file on GitHub.

> Alternative: If you prefer local edits, paste the contents into VS Code, save, commit to the `feature-text-analyzer` branch (Source Control UI), and push — either approach is fine. The Agent method shows the MCP tool in action.

### C — Create the Pull Request

Type into Agent:

```
Agent: Create a pull request from branch "feature-text-analyzer" into "main" in repo "demo-streamlit". Title: "Add Text Analyzer widget". Body: "This PR adds a Text Analyzer widget to the Streamlit demo for Stage 2. It introduces a simple tokenizer, word/char counts, and top words display."
```

* The Agent will show the `create_pull_request` form (head, base, title, body). Confirm and submit.
* Expected: PR created, Agent returns PR number/URL.

---

## 3) Inspect the PR with MCP tools

Now we exercise `get_pull_request_diff` and `get_pull_request_files`.

### D — Get PR diff

Type into Agent (use the PR number or URL returned in previous step; Agent may populate it automatically):

```
Agent: Show the diff for pull request #<PR_NUMBER> in repo "demo-streamlit".
```

* The Agent calls `get_pull_request_diff` and should return the unified diff (or a summary) in chat.
* What to point out: the diff shows new/changed lines in `app.py`. This is a great place to demonstrate line-level review.

### E — List files changed in the PR

Type into Agent:

```
Agent: List the files changed in pull request #<PR_NUMBER> for repo "demo-streamlit".
```

* The Agent calls `get_pull_request_files` and returns the file list (e.g., `app.py`).
* Use this to show file-level changes and to pick files/lines for review.

---

## 4) Request Copilot review (AI-assisted) — `request_copilot_review`

This is the MCP tool that asks Copilot (AI) to review the PR and provide suggestions.

Type into Agent:

```
Agent: Request a Copilot review for pull request #<PR_NUMBER> in repo "demo-streamlit". Ask Copilot to focus on: (1) obvious security issues (no eval/use of unsafe functions), (2) clarity/readability of code, (3) simple performance or correctness problems. Return suggested changes and a short summary.
```

* The Agent will call `request_copilot_review`. Copilot will respond with a review report (summary + suggested edits).
* Example outputs you'll likely see: suggestions on tokenization, defensive checks for None, adding tests, or docstrings.

**How to use Copilot's suggestions**:

* You can either edit code locally / via Agent and push a new commit to the feature branch, or you can create inline review comments and request changes.

---

## 5) Create and submit a PR review (human-style) — `create_and_submit_pull_request_review`

We'll use a sample review: leave two comments and request changes (or approve). The Agent accepts a review body and event type (`COMMENT`, `APPROVE`, `REQUEST_CHANGES`). You can also instruct it to remark on specific file/line ranges.

Type into Agent (example that requests a small change):

```
Agent: Create and submit a pull request review for PR #<PR_NUMBER> in "demo-streamlit". 
Review event: REQUEST_CHANGES
Review body: "Thanks — this is a great start. Two small items before merging:
1) In app.py please add a small guard: if text is None: treat as empty string (to avoid errors).
2) In analyze_text, the tokenizer currently treats digits/underscores as words; please add a short comment explaining the tokenizer, and consider filtering stopwords for the top words list.

Please add review comments inline:
- app.py, near the analyze_text() function: 'Consider a guard here for None and add a docstring.'
- app.py, near the tokenizer regex: 'Add a short comment explaining this regex and why digits are included.'
"
```

* The Agent will call `create_and_submit_pull_request_review` and add the review (with inline comments if supported by the MCP tool UI you see).
* Expected: PR shows a "Changes requested" review in GitHub UI and inline comments on `app.py`.

> Tip: if MCP UI requires explicit file/line coordinates for inline comments, Copilot will ask for those — you can paste approximate line numbers or phrase like "near analyze\_text definition" and the Agent will map it.

---

## 6) Address review comments (optional quick fix)

You can either:

* Edit `app.py` locally in VS Code to add the requested guard and comments, commit to `feature-text-analyzer`, and push (Source Control UI); or
* Ask the Agent to patch the file:

Agent prompt to patch:

```
Agent: Update file "app.py" on branch "feature-text-analyzer" in repo "demo-streamlit" to:
1) Add a docstring to analyze_text explaining the tokenizer.
2) Add a guard: if s is None: s = "" at the start of analyze_text.
Commit message: "Fix: guard None in analyze_text + add docstring (per review)"
```

* The Agent will run `create_or_update_file` and create a new commit on the feature branch. The PR will update automatically.

---

## 7) Re-run Copilot review or add human approval

* Option A: Re-request Copilot review:

```
Agent: Re-run Copilot review for PR #<PR_NUMBER> focusing on the updated analyze_text changes.
```

* Option B: Submit an approving review (human):

```
Agent: Submit a review for PR #<PR_NUMBER> with event APPROVE and body "Changes addressed; approving for merge."
```

Either action will call the appropriate MCP tool and update PR status.

---

## 8) Merge the Pull Request — `merge_pull_request`

When PR is ready, merge it. Choose merge strategy (merge/squash/rebase) in the Agent prompt.

Agent prompt:

```
Agent: Merge pull request #<PR_NUMBER> in repo "demo-streamlit" into "main" using "squash" merge strategy. Commit message: "Add Text Analyzer — squash merge".
```

* The Agent calls `merge_pull_request`. Expected reply includes merge commit SHA and link to the merged commit.
* Verify by opening the `main` branch in the GitHub repo (via the link in the Agent chat) and show `app.py` now contains the merged changes.

---

## 9) Verification checklist (what to show to the audience)

* After branch creation: Copilot chat lists `feature-text-analyzer`. Show branch selector in GitHub UI too.
* After file commit: File view on GitHub shows the updated `app.py` on that branch.
* After PR creation: PR page (URL agent returned) shows PR title, description, and changed files tab.
* `get_pull_request_diff`: show the unified diff returned in chat (or open Files changed on PR).
* `get_pull_request_files`: confirm `app.py` appears.
* Copilot review: show the AI review text in chat.
* Human review: show "Changes requested" or "Approved" status on PR and inline comments.
* Merge: show merged commit on `main` and the final `app.py` content.

---

## 10) Troubleshooting & gotchas (Stage-2)

* **Agent asks for PR number but you only have PR URL**: paste the PR URL; Copilot will extract the number.
* **Inline comment location mapping**: sometimes Agent will ask for exact line numbers; open the PR Files changed tab and copy the line number displayed and paste it into the Agent when requested.
* **Race conditions**: if you commit locally AND via Agent to the same branch at the same time, you may get conflicts. Resolve in VS Code Source Control (merge or rebase).
* **Permissions**: ensure the MCP token configured in Copilot has repo write permissions to create branches, push commits, and create PRs. If you get permission denied, check Copilot/MCP settings.
* **Large diffs**: `get_pull_request_diff` may be truncated in chat if diff is huge — keep PR changes focused for the demo.
* **Merge protection**: if `main` has branch protection (required checks), `merge_pull_request` will fail until checks pass. For demo simplicity either skip protections or show how to run CI (we can add a tiny CI job in Stage 3 if you want).

---

## 11) Example Agent transcript (copyable)

1. `Agent: Create a branch named "feature-text-analyzer" in repo "demo-streamlit", based on "main".`
2. `Agent: Create or update file "app.py" on branch "feature-text-analyzer" in repo "demo-streamlit" with the following content:` *(paste full app.py)*
3. `Agent: Create a pull request from branch "feature-text-analyzer" into "main" in repo "demo-streamlit". Title: "Add Text Analyzer widget". Body: "This PR adds a Text Analyzer widget to the Streamlit demo for Stage 2..."`
4. `Agent: Show the diff for pull request #<PR_NUMBER> in repo "demo-streamlit".`
5. `Agent: List the files changed in pull request #<PR_NUMBER> for repo "demo-streamlit".`
6. `Agent: Request a Copilot review for pull request #<PR_NUMBER> in repo "demo-streamlit"...`
7. `Agent: Create and submit a pull request review for PR #<PR_NUMBER> with event REQUEST_CHANGES ...`
8. *(Optional) Agent: Update file "app.py" ... commit message: "Fix: guard None in analyze\_text + add docstring (per review)"}*
9. `Agent: Submit a review for PR #<PR_NUMBER> with event APPROVE and body "Changes addressed; approving for merge."`
10. `Agent: Merge pull request #<PR_NUMBER> in repo "demo-streamlit" into "main" using "squash" merge strategy.`

# Stage 3 — Issues & Collaboration

We'll implement the issue lifecycle for the `demo-streamlit` repo using **VS Code + Copilot Chat (Agent mode) → MCP: GitHub** tools only. This stage exercises these MCP tools:

* `create_issue`
* `update_issue`
* `add_issue_comment`
* `assign_copilot_to_issue`

Below is everything: ready-to-paste issue content, exact Agent prompts to run in Copilot Chat, VS Code UI fallback steps, expected results/verification, and troubleshooting.

---

## Goals for Stage 3

1. File a clear bug report for the Text Analyzer (introduced in Stage 2).
2. Update the issue with labels, priority, and milestone (use `update_issue`).
3. Add clarifying comments and triage notes (`add_issue_comment`).
4. Assign Copilot to the issue to request automated help / suggestions (`assign_copilot_to_issue`).
5. (Optional follow-up) Request Copilot produce a candidate patch/PR (we'll show prompts that call PR tools from later stages).

---

## 0) Preconditions (quick)

* Open the `demo-streamlit` workspace in VS Code.
* Copilot Chat open → **Agent** mode → enable **MCP Server: GitHub** in tools.
* You previously created `demo-streamlit` and have `main` and `feature-text-analyzer` branches (from Stage 1/2).
* Your Copilot/MCP token has permissions to create/update issues and assign tools.

---

## 1) Issue content (copy/paste ready)

**Title:** `Text Analyzer: handle None input and improve tokenizer stopword filtering`

**Body (markdown):**

```markdown
## Summary
The Text Analyzer widget sometimes treats `None` or empty inputs incorrectly and the current tokenizer counts digits/underscores as words which inflates results for certain inputs. We should:
- Guard `analyze_text()` against `None` inputs (treat as empty string).
- Document the tokenizer behavior and rationale.
- Add an optional stopword filter for top-words display (configurable).
- Add a unit test for `analyze_text()` covering edge cases.

## Steps to reproduce
1. Open the Streamlit app.
2. Paste nothing (empty), or programmatically send `None` to the text area.
3. Observe that word/char counts may be incorrect or UI behavior is inconsistent.

## Expected behavior
- Empty or `None` input should be handled gracefully (0 chars, 0 words).
- Tokenizer behavior should be documented and optionally filter common stopwords before computing top words.

## Acceptance criteria
- `analyze_text()` includes a guard and docstring.
- Tokenizer comment added and an optional `remove_stopwords=True` parameter available.
- Unit tests added (basic pytest).
- PR references this issue and includes "Fixes #<issue-number>" in the PR body.

## Priority
medium

## Notes
This is beginner-friendly. Copilot may be able to suggest the code changes and produce the unit tests.
```

---

## 2) Exact Copilot (Agent) prompts — create the issue

Open Copilot Chat → **Agent** → paste the prompt:

```
Agent: Create an issue in repo "demo-streamlit".
Title: "Text Analyzer: handle None input and improve tokenizer stopword filtering"
Body: <paste the exact markdown body above>
Labels: bug, enhancement, triage-needed
Assignees: none
Milestone: none
```

**What to expect (Agent UI):**

* Agent will show the `create_issue` tool form pre-filled. Confirm the labels and body, then submit.
* The chat will return issue number, URL, and created timestamp.

**What to show:** Click the issue URL in the chat to open the GitHub issue page and show the content.

---

## 3) Update the issue — add priority, milestone, and assignee (use `update_issue`)

After creating the issue you may want to update metadata. Example: set `priority: high`, add a milestone "v1.0", and assign yourself.

Agent prompt (paste):

```
Agent: Update the issue #<ISSUE_NUMBER> in repo "demo-streamlit".
Set labels: bug, enhancement, priority/high, ready
Set milestone: "v1.0"   # create the milestone if it does not exist
Assignees: <your-github-username>
Comment: "Triage: setting milestone v1.0 and assigning to <your-github-username> for initial patch. Copilot assigned to help next."
```

**Notes:**

* If the Agent asks whether to create the milestone, confirm yes — `update_issue` will add the milestone.
* If your org policies prevent autopopulating assignees, the Agent will report permission errors.

**What to show:** Issue page reflecting label/milestone/assignee updates.

---

## 4) Add clarifying comments (`add_issue_comment`)

Use `add_issue_comment` for discussion, reproduction logs, or to paste small code suggestions inline.

Agent prompt:

```
Agent: Add a comment to issue #<ISSUE_NUMBER> in repo "demo-streamlit" with this content:
"Thanks — I will triage this. Quick note: can you paste a small example string that triggers the tokenizer problem? Also, I plan to add a `remove_stopwords` flag defaulting to False so behavior is opt-in."
```

**What to expect:** The comment appears under the issue on GitHub and in the Agent chat.

---

## 5) Assign Copilot to the issue (`assign_copilot_to_issue`)

This unique MCP tool signals Copilot to take responsibility for assisting on the issue (suggesting patch, tests, or draft PR). The effect depends on MCP server integration and Copilot setup — typically Copilot will generate suggested changes or a patch when asked.

Agent prompt:

```
Agent: Assign Copilot to assist on issue #<ISSUE_NUMBER> in repo "demo-streamlit". 
Scope: propose code changes and unit tests.
Message for Copilot: "Please propose a patch for analyze_text() that:
- Adds a None guard (treat None as empty string)
- Adds a docstring explaining the tokenizer
- Adds an optional parameter remove_stopwords=False which will remove common English stopwords when True
- Produces a small pytest unit test file tests/test_analyze_text.py covering empty, normal, and stopword cases."
```

**What to expect:**

* Agent will call `assign_copilot_to_issue`. Copilot (the assistant) will reply in chat with a plan and likely a proposed patch (diff or suggested file edits). It may offer to create a branch and PR with those changes (see optional steps below).
* If your MCP configuration supports automated PR creation by Copilot, the Agent may provide an option to create a branch/PR. Confirm only if you want the code auto-created.

**If Copilot returns a patch**: It will usually appear as a code block or list of edits. You can (a) accept and ask the Agent to apply changes (calls `create_or_update_file`, `create_branch`, `create_pull_request`), or (b) copy-paste the patch into VS Code and apply manually.

---

## 6) Example Copilot-generated patch (illustrative)

If Copilot produces a patch, it will look like this. You can paste/confirm it with the Agent to apply.

**Patch suggestions (example) — update `app.py` analyze\_text**

```diff
@@
-def analyze_text(s: str):
-    if not s:
-        return {"chars": 0, "words": 0, "top_words": []}
-    chars = len(s)
-    # very small tokenizer: split on non-word chars
-    tokens = re.findall(r"\w+", s.lower())
-    words = len(tokens)
-    freqs = Counter(tokens)
-    top = freqs.most_common(5)
-    return {"chars": chars, "words": words, "top_words": top}
+def analyze_text(s: str, remove_stopwords: bool = False):
+    """
+    Tokenize and analyze input string.
+
+    Behavior:
+      - If s is None, treat as empty string.
+      - Tokenizer uses regex r"\w+" which captures letters, digits, and underscores.
+      - If remove_stopwords=True, common English stopwords are removed before computing top words.
+    """
+    if s is None:
+        s = ""
+    chars = len(s)
+    tokens = re.findall(r"\w+", s.lower())
+    if remove_stopwords:
+        STOPWORDS = {"the","and","is","in","it","of","to","a","an"}
+        tokens = [t for t in tokens if t not in STOPWORDS]
+    words = len(tokens)
+    freqs = Counter(tokens)
+    top = freqs.most_common(5)
+    return {"chars": chars, "words": words, "top_words": top}
```

**Example pytest (tests/test\_analyze\_text.py):**

```python
from demo_streamlit.app import analyze_text

def test_analyze_empty():
    res = analyze_text("", remove_stopwords=False)
    assert res["chars"] == 0
    assert res["words"] == 0

def test_analyze_none():
    res = analyze_text(None)
    assert res["chars"] == 0
    assert res["words"] == 0

def test_analyze_stopwords():
    res = analyze_text("the the cat", remove_stopwords=True)
    # "the" removed -> only "cat" remains
    assert res["words"] == 1
```

---

## 7) Ask Copilot to create a branch + PR (optional follow-up — uses Stage 1/2 tools)

If you want Copilot to implement the patch automatically and open a PR that references the issue:

Agent prompt (after Copilot produced patch and you accept it):

```
Agent: Create a new branch named "fix/analyze-text-None-guard" in repo "demo-streamlit" and apply the patch Copilot suggested to app.py and add tests/tests_analyze_text.py. Commit message: "Fix: None guard and optional stopword filter (fixes #<ISSUE_NUMBER>)". Then open a pull request into main with title "Fix analyze_text None guard and stopword filtering" and body "Fixes #<ISSUE_NUMBER>".
```

**What to expect:**

* Agent will sequence `create_branch` → `create_or_update_file` (for each file) → `create_pull_request`.
* PR will be created and will reference the issue with `Fixes #<ISSUE_NUMBER>` which closes the issue on merge.

> Note: This uses tools covered in earlier stages (create\_branch, create\_or\_update\_file, create\_pull\_request). If you want, we can do this in the demo after Copilot produces the patch.

---

## 8) Verification checklist (what to show the audience)

* Issue created: show the issue page (title, body, labels).
* Issue updated: show new labels, milestone, assignee.
* Issue comments: show the comment thread.
* Copilot assignment: show Copilot's chat response with the proposed patch or plan.
* (If applied) PR created: show PR that references the issue and includes "Fixes #X".

---

## 9) Example Agent transcripts (copyable)

**Create issue**

```
Agent: Create an issue in repo "demo-streamlit".
Title: "Text Analyzer: handle None input and improve tokenizer stopword filtering"
Body: <paste issue markdown>
Labels: bug, enhancement, triage-needed
```

**Update issue**

```
Agent: Update issue #12 in repo "demo-streamlit".
Set labels: bug, enhancement, priority/high, ready
Set milestone: "v1.0"
Assignees: my-github-username
Comment: "Triage: setting milestone v1.0 and assigning to <username>."
```

**Add comment**

```
Agent: Add a comment to issue #12 in repo "demo-streamlit" saying:
"Thanks — can you paste a small example string that triggers the tokenizer problem? I'll assign Copilot to propose a patch."
```

**Assign Copilot**

```
Agent: Assign Copilot to assist on issue #12 in repo "demo-streamlit".
Scope: propose code changes and unit tests.
Message: "Please propose a patch for analyze_text(): add a None guard, docstring, optional remove_stopwords param, and pytest tests."
```

---

## 10) Troubleshooting & gotchas (Stage-3)

* **Agent requests missing fields**: Agent will show forms for `create_issue` or `update_issue` — fill them. This is normal.
* **Permission denied on assignee**: Some repos restrict assignees to repo members; if you see an error, either ask to add yourself as a collaborator or skip assigning.
* **Milestone creation blocked**: Org policies may limit milestone creation; create manually in GitHub UI if needed.
* **Copilot not producing a patch**: If `assign_copilot_to_issue` returns only a plan not code, ask explicitly: `Agent: Produce the patch now as a diff for me to apply.`
* **Applying automated patch fails**: If you ask the Agent to create files/commits and it fails due to branch protection, either disable protection for demo or create the branch and open a PR for checks to run.
* **Conflicting local edits**: If you edit files locally and Copilot also edits them remotely, resolve conflicts in VS Code (Source Control UI) before merging.

---

## 11) Notes on pedagogical flow (how to demo live)

1. Create the issue in real-time from the Agent and open the issue page (show how minimal input produces a well-formed issue).
2. Demonstrate updating labels/milestone quickly (show `update_issue` effect in UI).
3. Add a clarifying comment (show conversation).
4. Assign Copilot and show the generated patch in chat — discuss the quality and where a human would refine.
5. Optionally accept the patch and let Copilot open a PR — then continue Stage 2 review/merge flow.

Awesome — moving on to **Stage 4: Notifications & Productivity**. Below is a complete, VS Code + Copilot (Agent) focused implementation that you can run live. It uses the MCP tools only (no `gh` CLI / REST in the demo). This stage exercises:

* `list_notifications`
* `dismiss_notification`
* `mark_all_notifications_read`
* `manage_repository_notification_subscription`

You'll get:

* Exact Copilot Agent prompts to call each tool.
* A short sequence to *generate* demo notifications (so you can show real data).
* VS Code UI fallback steps and visual verification points.
* Troubleshooting and demo tips.

---

# Stage 4 — Notifications & Productivity

## Goals for Stage 4

This stage shows how developers can view and manage their GitHub notifications programmatically via the MCP server and combine those actions with repo-level subscription controls.

The demo flow will cover:
1. Generating demo notifications.
2. Using `list_notifications` to fetch the user's notification list.
3. Using `dismiss_notification` to dismiss one notification.
4. Using `mark_all_notifications_read` to clear the inbox.
5. Using `manage_repository_notification_subscription` to toggle watch/unwatch for the demo repo.

## A — Prepare demo notifications (quick way to generate items)

If you've followed Stage 1–3 you probably already have PRs/issues. If not, create a few quick items using Copilot Agent (these are the actions that produce notifications for yourself or others):

1. Create a small PR (if not already created) — will generate a PR notification for reviewers.
2. Add a review request to someone (requesting your own user or a demo collaborator will create a notification).
3. Create an issue comment that mentions a user `@<your-username>` — this produces a notification for that user.

Exact Copilot prompts (Agent) to generate notifications:

* Create a tiny PR (if not already):

```
Agent: Create a branch "notif-demo-branch" on repo "demo-streamlit" from "main", add a one-line change to README.md ("notif demo"), commit with message "notif demo", and open a pull request into main titled "Notification demo PR".
```

* Request review from a user (replace `<reviewer>` with a GitHub username — for the demo you can request review from yourself or a demo collaborator):

```
Agent: For the pull request just created (#<PR_NUMBER>), request review from "<reviewer>".
```

* Create an issue comment that mentions you:

```
Agent: Create an issue in repo "demo-streamlit" titled "Notif mention test" with body "Tagging @<your-github-username> to generate a demo notification." and then add a comment that says "@<your-github-username> please review."
```

> Note: When you run these prompts, the Agent will create real GitHub objects that will generate notifications. Wait a few seconds for GitHub to push notifications to your account.

---

## B — List notifications (`list_notifications`)

**Agent prompt**

```
Agent: List my notifications. Return unread notifications first and show: repository, subject (type/title), reason (e.g., review_requested, mention), updated_at, and the notification ID.
```

**What the Agent will show**

* A compact list of notifications (unread first). Each entry should include:

  * `id` (unique notification id for later calls)
  * `repository` (e.g., demo-streamlit)
  * `subject.title` (e.g., "Notification demo PR")
  * `reason` (e.g., `review_requested`, `mention`, `subscribed`)
  * `updated_at` timestamp
  * A direct link to the subject (PR/issue) when available

**How to show to audience**

* Show the returned list in Copilot chat.
* Click the link(s) to open the PR/issue on GitHub and demonstrate the same item in the UI.

**Tips**

* Ask the Agent to limit results (e.g., only unread) if your inbox is large:

```
Agent: List my unread notifications for repo "demo-streamlit".
```

---

## C — Dismiss a single notification (`dismiss_notification`)

Pick one notification `id` from the list the Agent returned.

**Agent prompt**

```
Agent: Dismiss notification with id "<NOTIF_ID>".
```

**What to expect**

* Agent calls `dismiss_notification` and confirms success.
* The notification will become read/cleared in your GitHub UI and will no longer show as unread in a new `list_notifications` call.

**Verification**

1. Run `Agent: List my unread notifications` again — the dismissed ID should no longer appear.
2. Open the GitHub notifications UI ([https://github.com/notifications](https://github.com/notifications)) and show the same notification is marked read/archived.

**Demo tip**

* Dismiss a `mention` notification first so the audience sees an immediate effect. Then re-run the list to show the change.

---

## D — Mark all notifications read (`mark_all_notifications_read`)

**Agent prompt**

```
Agent: Mark all my notifications as read.
```

**What to expect**

* Agent calls `mark_all_notifications_read` and returns confirmation (timestamp when it marked read).
* Your GitHub notifications page will show an empty (or smaller) unread list.

**Verification**

* `Agent: List my unread notifications` should return an empty list (or only new ones created afterward).
* Show GitHub notifications page in browser to confirm "All caught up" or zero unread.

**Caution**

* This is destructive for the purpose of demo: it marks everything read. Use it when you want a clean slate. For presentations, do it at the end or explain you're clearing the inbox.

---

## E — Manage repository notification subscription (`manage_repository_notification_subscription`)

This toggles watching/unwatching a specific repo. Use it to demonstrate controlling future notifications.

**Agent prompt — set to watch**

```
Agent: Subscribe me to repository notifications for "demo-streamlit" (watch). I want to receive notifications for all conversations.
```

**Agent prompt — set to ignore/unwatch**

```
Agent: Unsubscribe or ignore notifications for repository "demo-streamlit".
```

**What to expect**

* Agent confirms the repo-level subscription status change and returns the new subscription state (`subscribed`, `ignored`, or `custom`).
* Future events in the repo will generate (or stop generating) notifications accordingly.

**Demo sequence idea**

1. Unsubscribe / ignore the repo.
2. Create a new PR or issue (via Agent) that would normally notify you.
3. Show that `list_notifications` no longer includes the new item (or it appears with a different `reason` like `manual`).
4. Then `subscribe` or `watch` the repo again and create another PR — show that the new notification arrives.

**Agent prompt to test the change**

* After unsubscribing:

```
Agent: Create an issue titled "Notification watch test" in "demo-streamlit" saying "Testing notification subscriptions". 
```

* Wait a few seconds and then:

```
Agent: List my unread notifications for repo "demo-streamlit".
```

* Show whether the new issue generated a notification.

---

## F — Example step-by-step demo script (concise)

1. (Optional) Generate a few notifications: create PR, request review, mention yourself in an issue comment (use the Agent prompts in **A**).
2. `Agent: List my notifications` → show the list.
3. `Agent: Dismiss notification with id "<first-id>"` → verify by listing notifications again.
4. `Agent: Mark all my notifications as read` → verify inbox cleared.
5. `Agent: Unsubscribe from repo "demo-streamlit"` → Agent confirms.
6. Create a new test issue: `Agent: Create an issue "watch test" ...` → `Agent: List my unread notifications` → verify no notification for that issue.
7. `Agent: Subscribe to repository "demo-streamlit"` → create another test issue → `Agent: List my unread notifications` → verify the new notification appears.

---

## G — VS Code UI fallback & where to show things

* VS Code Copilot chat shows returned notifications with links — click them to open GitHub.
* To show GitHub UI:

  * Open GitHub → top-right bell (Notifications) or visit `https://github.com/notifications`.
  * Use the Filter options to show unread or repo-specific notifications.
  * Open the repo page → Watch / Unwatch visible in repo header (use this to show what `manage_repository_notification_subscription` toggles).

---

## H — Troubleshooting & gotchas

* **No notifications appearing**: ensure the account used by Copilot/MCP is the same account you're checking. The MCP server calls the API as the authenticated user configured in Copilot.
* **Delays**: GitHub notifications may take a few seconds to populate after creating PRs/issues. Wait \~10–20s before listing notifications.
* **Permission/Org policies**: Some orgs route notifications differently (email-only or suppressed). If notifications don't arrive, check org settings or the account notification preferences in GitHub settings.
* **Subscription state confusion**: `subscribed` means you actively watch and get notifications; `ignored` means you won't get notifications. Repo header's Watch button reflects that state.
* **IDs vs URLs**: `dismiss_notification` requires the notification ID the Agent returns; paste it exactly. If Agent returns multiple formats, use the numeric/id format in the dismissal prompt.
* **Testing repeatedly**: If you frequently create test notifications, `mark_all_notifications_read` helps reset demo state.

---

## I — Demo polish tips (for presentation)

* Before demo: create a few notifications so `list_notifications` shows meaningful results quickly.
* Use descriptive PR/issue titles so output looks tidy in the chat list (e.g., `"Notif demo PR — please review @me"`).
* When demonstrating subscribe/unsubscribe, create *two* test items to clearly show the difference (one while unsubscribed, one while subscribed).
* At the end of the demo, run `Agent: Mark all my notifications as read` so your inbox is cleaned for the next run.

Great — Stage 5 (Security & Code Insights) implemented in full. Below you'll find everything you need to run the **4-part Security Story** in your single demo repo (`demo-streamlit`) using **VS Code + Copilot Agent (MCP: GitHub)** only. No `gh`/REST required — all MCP tool prompts are included.

I'll give you:

* The exact files to add (CodeQL workflow, Dependabot config, vulnerable `package.json`, dummy `.env`) — copy/paste ready.
* Step-by-step Agent prompts to create the files on a feature branch and push them (or you can edit locally and commit via VS Code).
* The Agent prompts to call the MCP tools for inspection: `list_code_scanning_alerts`, `get_code_scanning_alert`, `list_secret_scanning_alerts`, `get_secret_scanning_alert`, and `search_code`.
* Expected results, timing notes, and troubleshooting for each part.
* Short references to authoritative docs used (CodeQL, Dependabot, Secret Scanning, MCP usage, Code Search). ([GitHub Docs][1])

---

# Stage 5 — Security & Code Insights

## Goals for Stage 5

This stage covers four key areas of security and code analysis:
1. **Static Analysis (CodeQL)** — using `list_code_scanning_alerts` and `get_code_scanning_alert`.
2. **Secrets Detection** — using `list_secret_scanning_alerts` and `get_secret_scanning_alert`.
3. **Proactive Code Search** — using `search_code`.
4. **Dependency Security (Dependabot)** — covering Dependabot alerts and automated pull requests.

> Important: For each step below I give the **Copilot Agent** prompt to paste into Copilot Chat (Agent mode) — the Agent will present the MCP tool form; confirm fields and submit.

---

## A — Files to add to the repo (copy/paste)

Add these files in the repo root (or ask the Agent to create them). If you prefer local edits, paste into VS Code and commit; otherwise use the Agent `create_or_update_file` as documented in earlier stages.

### 1) `.github/workflows/codeql.yml` — CodeQL analysis (Python)

```yaml
name: "CodeQL"
on:
  push:
    branches: [ main ]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [ main ]
  schedule:
    - cron: '0 3 * * 0'  # weekly; change if you want more frequent scans

jobs:
  analyze:
    name: Analyze (CodeQL)
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    strategy:
      fail-fast: false
      matrix:
        language: [ 'python' ]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}

      - name: Autobuild (if needed)
        uses: github/codeql-action/autobuild@v2

      - name: Run CodeQL analysis
        uses: github/codeql-action/analyze@v2
```

Notes: default setup scans pushes and PRs; the schedule line controls periodic scans (default weekly). See CodeQL docs for customization. ([GitHub Docs][1])

---

### 2) `.github/dependabot.yml` — Dependabot (npm daily)

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    open-pull-requests-limit: 5
    labels:
      - "dependabot"
```

Notes: this enables Dependabot version/security updates for npm manifests in `/`. Dependabot will open PRs or create alerts based on found vulnerabilities. ([GitHub Docs][2])

---

### 3) `package.json` — deliberately vulnerable dependency (lodash)

```json
{
  "name": "demo-streamlit",
  "version": "0.1.0",
  "description": "Demo Streamlit app for MCP Server security stage",
  "dependencies": {
    "lodash": "4.17.19"
  }
}
```

Rationale: `lodash@4.17.19` is older than the patched `4.17.21` — Dependabot should detect and raise a security update PR/alert. (Dependabot behavior depends on the repo being scanned and schedule.) ([GitHub Docs][3])

---

### 4) `.env` — dummy leaked secret (for secret scanning demo)

> **Warning:** This is intentionally a fake secret that we commit for demo purposes. Do NOT use real credentials in demos. If you prefer, create the file in a throwaway public repo.

```
AWS_SECRET_ACCESS_KEY=ABCD1234EFGH5678IJKL
```

Secret scanning will detect this pattern if secret scanning is enabled for the repo. Public repos on GitHub.com have secret scanning available; org/private repos may require specific settings. ([GitHub Docs][4])

---

## B — Add files via Copilot Agent (recommended demo path)

Open Copilot Chat in VS Code → **Agent** → ensure **MCP Server: GitHub** tool is enabled. Then use these prompts (one-by-one). The Agent will show the tool form for `create_or_update_file` or `create_branch` and ask for confirmation.

### 1 — Create a feature branch for security staging

```
Agent: Create a branch named "stage5-security-setup" in repo "demo-streamlit" based on "main".
```

(Confirm the branch creation in the form.)

### 2 — Add CodeQL workflow on that branch

```
Agent: Create file ".github/workflows/codeql.yml" on branch "stage5-security-setup" with the following content: <paste codeql.yml content>
Commit message: "chore: add CodeQL workflow (stage5)"
```

### 3 — Add Dependabot config

```
Agent: Create file ".github/dependabot.yml" on branch "stage5-security-setup" with content: <paste dependabot.yml content>
Commit message: "chore: add dependabot config (stage5)"
```

### 4 — Add vulnerable package.json

```
Agent: Create file "package.json" on branch "stage5-security-setup" with content: <paste package.json content>
Commit message: "chore: add vulnerable package.json (lodash@4.17.19)"
```

### 5 — Add `.env` with dummy secret (for secret scanning demonstration)

```
Agent: Create file ".env" on branch "stage5-security-setup" with content: AWS_SECRET_ACCESS_KEY=ABCD1234EFGH5678IJKL
Commit message: "test: add dummy secret for secret scanning demo"
```

### 6 — Push all changes / open PR

```
Agent: Create a pull request from "stage5-security-setup" into "main" in repo "demo-streamlit".
Title: "chore: add security workflows and test artifacts (CodeQL, Dependabot, dummy secret)"
Body: "Add CodeQL workflow, Dependabot config, a vulnerable package.json and a dummy secret for Stage 5 Security demo."
```

> The Agent will call `create_pull_request`. Once PR created, CodeQL action will trigger on the PR and the new commits are present on that branch.

---

## C — Part 1: Static Analysis (CodeQL) — inspect alerts

**What to do next (Agent prompts):**

1. List CodeQL (code scanning) alerts:

```
Agent: List code scanning alerts in repo "demo-streamlit".
```

(This calls the `list_code_scanning_alerts` MCP tool.)

2. Inspect a specific alert (use alert ID returned by previous step):

```
Agent: Get details of code scanning alert with id "<ALERT_ID>" in "demo-streamlit".
```

(This calls `get_code_scanning_alert`.)

**What to expect & timing:**

* CodeQL runs are triggered on pushes & PRs. Small repos typically show results within a few minutes, but sometimes scans need several minutes depending on queue/backlog. The default configured schedule can also run weekly; our PR-triggered run is immediate on the PR push. See CodeQL docs for scheduling and advanced setup. ([GitHub Docs][1])

**Verification UI:**

* GitHub Security → Code scanning alerts will show the same findings the Agent lists. Use the Agent output to click links into the GitHub Security tab.

**Troubleshooting:**

* If `list_code_scanning_alerts` returns an empty list immediately, wait 2–10 minutes and retry; the action may still be queued. If still empty after \~15 minutes, open the Actions tab for the workflow run to check failure logs.

---

## D — Part 2: Secrets Detection — detect the dummy secret

**Agent prompts:**

1. List secret scanning alerts:

```
Agent: List secret scanning alerts in repo "demo-streamlit".
```

(Calls `list_secret_scanning_alerts`.)

2. Inspect a secret alert:

```
Agent: Get secret scanning alert details for alert id "<SECRET_ALERT_ID>" in "demo-streamlit".
```

(Calls `get_secret_scanning_alert`.)

**What to expect & timing:**

* Secret scanning runs over repository history and new pushes. For public repos, GitHub runs secret scanning and will usually show results within a few minutes for new commits. For private/org repos, secret scanning must be enabled in repo settings (Security → Code security and analysis → Secret scanning). ([GitHub Docs][4])

**Verification UI:**

* GitHub Security → Secret scanning alerts. The Agent output will include alert metadata and links to the location in the commit where the secret was found.

**Troubleshooting:**

* If secret scanning is not enabled for private repos, enable it in repo Settings → Code security and analysis. If your account lacks permissions, the Agent will return permission errors.

---

## E — Part 3: Proactive Code Search — hunt for risky patterns

**Useful Agent prompts (examples):**

* Search for the dummy secret pattern name:

```
Agent: Search code in repo "demo-streamlit" for the string "AWS_SECRET_ACCESS_KEY" and return file path(s) and line numbers.
```

(Calls `search_code` — helpful to locate secrets immediately.)

* Search for other risky patterns (e.g., `eval(` or `process.env`):

```
Agent: Search code in repo "demo-streamlit" for "eval(" and return file paths and brief snippets.
Agent: Search code in repo "demo-streamlit" for "process.env" and return matches.
```

**What to expect:**

* `search_code` will return matching files and lines; MCP server passes these queries to GitHub code search under the hood. GitHub code search is robust and supports repo-scoped queries. ([GitHub][5])

**How to use results:**

* Use search hits to add fix tasks to the issue tracker or create PRs to remove or refactor unsafe patterns.

---

## F — Part 4: Dependency Security (Dependabot)

**Agent prompts (after dependabot.yml + package.json are on the repo):**

* Ask the Agent to show Dependabot alerts:

```
Agent: Show Dependabot alerts for repo "demo-streamlit" (or list dependency security advisories).
```

(Dependabot-specific listing might be surfaced by `list_code_scanning_alerts` or by the MCP server exposing Dependabot endpoints — if the MCP server exposes a Dependabot tool, it will use that. Otherwise, you can inspect GitHub Security → Dependabot or use the Agent to open the repo Security page.)

* Show open Dependabot PRs:

```
Agent: List open pull requests in repo "demo-streamlit" with label "dependabot".
```

(Calls `list_pull_requests` filtered by label; depends on the MCP toolset available.)

**What to expect & timing:**

* Dependabot runs according to `.github/dependabot.yml` schedule. With `interval: daily`, Dependabot will check daily; however, for newly added vulnerable `package.json` it will often create a PR or an alert within a short time (minutes to several hours) depending on backend processing. If you want immediate demo PRs, you can:

  * Manually bump the version (to demonstrate a PR creation flow), or
  * Use the Agent to create a PR that updates the dependency (to show what Dependabot would do) — we'll show that patch flow if you want.
* See Dependabot docs for config options and private registry setup. ([GitHub Docs][2])

**Verification UI:**

* GitHub Security → Dependabot alerts and the Pull requests list (filter by label `dependabot`) will show Dependabot PRs.

---

## G — End-to-end: Close the loop (example demo sequence)

1. Create `stage5-security-setup` branch and push the files (use the Agent prompts in section B).
2. Open a PR (Agent prompt included). That PR triggers CodeQL analysis.
3. Immediately (or after a couple minutes) run:

   * `Agent: List code scanning alerts in repo "demo-streamlit"`.
   * `Agent: List secret scanning alerts in repo "demo-streamlit"`.
   * `Agent: Search code for "AWS_SECRET_ACCESS_KEY" in repo "demo-streamlit"`.
4. If CodeQL or secret scanning reports findings, `Agent: Get code scanning alert <ID>` or `Agent: Get secret scanning alert <ID>` to see details.
5. For Dependabot, either wait for its scheduled run or manually open a PR to bump `lodash` and then `Agent: List open pull requests with label "dependabot"` to show how Dependabot automates updates.

---

## H — Example Agent prompts (compact pasteable block)

```
Agent: Create a branch named "stage5-security-setup" in repo "demo-streamlit" based on "main".
Agent: Create file ".github/workflows/codeql.yml" on branch "stage5-security-setup" with content: <CODEQL YAML> Commit message: "chore: add CodeQL workflow (stage5)"
Agent: Create file ".github/dependabot.yml" on branch "stage5-security-setup" with content: <dependabot.yml> Commit message: "chore: add dependabot config (stage5)"
Agent: Create file "package.json" on branch "stage5-security-setup" with content: <package.json> Commit message: "chore: add vulnerable package.json (lodash@4.17.19)"
Agent: Create file ".env" on branch "stage5-security-setup" with content: AWS_SECRET_ACCESS_KEY=ABCD1234EFGH5678IJKL Commit message: "test: add dummy secret for secret scanning demo"
Agent: Create a pull request from "stage5-security-setup" into "main" with title "chore: add security workflows and test artifacts (CodeQL, Dependabot, dummy secret)"
(wait for CodeQL/action to run)
Agent: List code scanning alerts in repo "demo-streamlit"
Agent: Get code scanning alert with id "<ALERT_ID>" in "demo-streamlit"
Agent: List secret scanning alerts in repo "demo-streamlit"
Agent: Get secret scanning alert with id "<SECRET_ALERT_ID>" in "demo-streamlit"
Agent: Search code in repo "demo-streamlit" for "AWS_SECRET_ACCESS_KEY"
Agent: List open pull requests in repo "demo-streamlit" with label "dependabot"
```

---

## I — Expected timing & polite notes

* **CodeQL**: PR-triggered scans typically finish in a few minutes but can take longer depending on GH Actions queue. If you don't see alerts immediately, open the Actions tab for the CodeQL workflow run to inspect logs. ([GitHub Docs][1])
* **Secret scanning**: usually quick for new commits (minutes) in public repos; for private repos you may need to enable settings. ([GitHub Docs][4])
* **Dependabot**: schedule-driven — daily when configured as above. It may not create a PR instantly; expect minutes→hours depending on backend. You can also simulate the update with an Agent-created PR to demonstrate the remediative flow. ([GitHub Docs][2])

---

## J — Troubleshooting & common issues

* **No CodeQL run / scan failed** — Check the Actions tab for the CodeQL workflow run; fix errors shown (e.g., `autobuild` step failures for complex build setups). You may need to add build steps or language matrices for multi-language repos. ([GitHub Docs][6])
* **Secret scanning not reporting** — Ensure secret scanning is enabled for the repo (Settings → Code security and analysis → Secret scanning) if private/enterprise. Public repos have secret scanning available automatically for many secret types. ([GitHub Docs][7])
* **Dependabot not creating PRs quickly** — Confirm `dependabot.yml` location and syntax; check the Dependabot logs under Security → Dependabot. For private registries you must configure credentials. ([GitHub Docs][8])
* **MCP tool returns permission errors** — Copilot/MCP uses the token configured in VS Code; ensure it has repo write and security-event/code-scanning scopes where needed. The Agent will show permission errors and you can adjust settings in GitHub/Copilot. ([GitHub Docs][9])


Which would you like next?

[1]: https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql?utm_source=chatgpt.com "About code scanning with CodeQL - GitHub Docs"
[2]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates?utm_source=chatgpt.com "Configuring Dependabot version updates - GitHub Docs"
[3]: https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories?utm_source=chatgpt.com "Dependabot supported ecosystems and repositories - GitHub Docs"
[4]: https://docs.github.com/code-security/secret-scanning/about-secret-scanning?utm_source=chatgpt.com "About secret scanning - GitHub Docs"
[5]: https://github.com/features/code-search?utm_source=chatgpt.com "Code Search - GitHub"
[6]: https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages?utm_source=chatgpt.com "CodeQL code scanning for compiled languages - GitHub Docs"
[7]: https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-secret-scanning-for-your-repository?utm_source=chatgpt.com "Enabling secret scanning for your repository - GitHub Docs"
[8]: https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot?learn=dependency_version_updates&learnProduct=code-security&utm_source=chatgpt.com "Guidance for the configuration of private registries for Dependabot"
[9]: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server?utm_source=chatgpt.com "Using the GitHub MCP Server"


Great — moving on to **Stage 6: Fork & Cross-Repo Collaboration**.
Below is a complete, copy-paste friendly plan you can run in **VS Code + Copilot (Agent mode) → GitHub MCP Server**. It covers creating a fork, making changes in the fork, opening a PR from the fork to the upstream repo, inspecting the PR via MCP tools, and merging (or showing merge flow). All prompts are written for Copilot Agent; VS Code UI fallback steps are included.

---

# Stage 6 — Fork & Cross-Repo Collaboration

## Goals for Stage 6

* Demonstrate `fork_repository` to create Repo B (a fork of Repo A).
* Create a branch on the fork, make a change, and push it on the fork.
* Create a PR from the fork (`your-username/demo-streamlit`) into upstream (`upstream-owner/demo-streamlit`).
* Use MCP tools to inspect PR diffs and files (`get_pull_request_diff`, `get_pull_request_files`, `list_pull_requests`) and request a Copilot review.
* Demonstrate merging as the upstream maintainer and show how the fork PR closes and code lands in upstream.

---

## Tools we'll exercise (MCP names)

* `fork_repository`
* `create_branch` (on the fork)
* `create_or_update_file` (on the fork)
* `create_pull_request` (head: forkOwner\:branch, base: upstream main)
* `list_pull_requests` (on upstream, to find PRs from forks)
* `get_pull_request_files` / `get_pull_request_diff`
* `request_copilot_review` (optional)
* `merge_pull_request` (performed by upstream maintainer)

---

## Files / small change for this demo

We'll make a tiny contributor-friendly change in the fork to create a visible diff: add `CONTRIBUTING.md` with a 3-line contribution guideline, or add a badge / sentence in `README.md`. This keeps the PR small and easy to inspect.

**Sample `CONTRIBUTING.md`** (copy into the fork branch)

```markdown
# Contributing

Thanks for contributing! For this demo:
- Make a branch named `fix/*` or `feat/*`.
- Run `pytest` (if tests exist).
- Open a PR into upstream `main` and mention this issue if relevant.
```

---

## A — Preconditions / notes

* You must be signed into VS Code with the GitHub account that will create the fork. Copilot Agent must be configured to use the GitHub MCP Server (Agent → tools → MCP: GitHub).
* Upstream repo is `upstream_owner/demo-streamlit` (replace `upstream_owner` with the actual owner used in your demo — for a single-repo demo it may be your own repo; for a true fork demo you may fork your own repo into another account/org).
* If you want to demonstrate a fork from one account into another (e.g., from an org to your personal account), make sure you have permissions to fork to the target account/org.
* Branch protection on upstream may block merging; we'll call that out in troubleshooting.

---

## B — Exact Copilot (Agent) prompts (use these in VS Code Copilot Chat Agent)

> Tip: paste each prompt one at a time. The Agent will present a tool form to confirm parameters (owner, repo, branch names, file content). Confirm the form fields to execute.

### 1) Create the fork

```
Agent: Fork the repository "demo-streamlit" from owner "upstream_owner" into my account. Use the MCP tool fork_repository. Name the fork "demo-streamlit" (same name).
```

* Agent will call `fork_repository`. It returns the fork repo URL (e.g., `https://github.com/your-username/demo-streamlit`).
* **What to show:** click the returned fork URL in chat and show the fork page in browser.

### 2) Create a branch on the fork

```
Agent: In my fork "your-username/demo-streamlit", create a branch named "fix/add-contributing" based on "main".
```

* Agent calls `create_branch` on the fork repo. Confirm the branch creation.

### 3) Add `CONTRIBUTING.md` (or modify README) on the fork branch

```
Agent: Create file "CONTRIBUTING.md" on branch "fix/add-contributing" in repo "your-username/demo-streamlit" with the following content:
<PASTE CONTRIBUTING.md CONTENT>
Commit message: "Add contributing guidelines (demo)"
```

* Agent calls `create_or_update_file` on the fork. Confirm.

### 4) Open a PR from fork → upstream

```
Agent: Create a pull request from "your-username:fix/add-contributing" into "upstream_owner:main" on repo "demo-streamlit".
Title: "Add CONTRIBUTING.md (demo from fork)"
Body: "This PR adds a small CONTRIBUTING.md with simple contributor guidelines. Created from fork for Stage 6 demo."
```

* Agent calls `create_pull_request`. Confirm parameters: head should be `your-username:fix/add-contributing`, base `upstream_owner:main`.
* Agent returns PR number and URL on the upstream repo (e.g., `upstream_owner/demo-streamlit#34`).

**Note:** Most MCP servers and the GitHub API support creating PRs where head references a fork. The Agent UI will show the required fields.

---

## C — Inspect the fork PR via MCP tools

These are the MCP calls you'll run to demonstrate inspection & review.

### 5) List PRs on upstream and find the fork PR

```
Agent: List pull requests on upstream repo "upstream_owner/demo-streamlit". Filter or show PRs with head containing "your-username".
```

* The Agent will run `list_pull_requests` and return the PR(s). Show the PR URL and number.

### 6) Show changed files in the PR

```
Agent: List the files changed in pull request #<PR_NUMBER> for repo "upstream_owner/demo-streamlit".
```

* Agent calls `get_pull_request_files` and returns the changed file(s) (`CONTRIBUTING.md`).

### 7) Show the PR diff

```
Agent: Show the diff for pull request #<PR_NUMBER> in repo "upstream_owner/demo-streamlit".
```

* Agent calls `get_pull_request_diff` and returns the unified diff or a summarized version.

### 8) (Optional) Request Copilot review on the fork PR

```
Agent: Request a Copilot review for PR #<PR_NUMBER> on "upstream_owner/demo-streamlit". Ask Copilot to check:
- Clarity of the CONTRIBUTING doc
- If any point should be added for running local tests
Return suggested edits and a short summary.
```

* Agent calls `request_copilot_review` for upstream PR. Copilot will produce suggested edits/review comments.

---

## D — Merge flow & maintainers

Two scenarios:

### Scenario 1 — You are the upstream maintainer

If the account you use to run merge is the upstream repo maintainer, you can merge via MCP:

**Agent prompt to merge:**

```
Agent: Merge pull request #<PR_NUMBER> in "upstream_owner/demo-streamlit" into "main" using "squash" (or "merge") strategy. Commit message: "Add CONTRIBUTING.md (from fork)". 
```

* Agent calls `merge_pull_request` and (if allowed) it will merge PR and return commit SHA and merged URL.

**Verification:** open upstream `main` and show `CONTRIBUTING.md` now present.

### Scenario 2 — You are the contributor (only fork owner)

If you are not a maintainer, you cannot merge the PR yourself. Instead:

* Show PR on upstream; show maintainers how to review & merge (via Agent or GitHub UI).
* Maintainer (or demo lead) can run `merge_pull_request` as above.
* Optionally demonstrate "Allow edits by maintainers" — mention that when creating PR via GitHub web, there is a checkbox; when using MCP it may need maintainers to enable pushing to fork; otherwise the maintainer can request changes or push a change to the fork branch via the fork owner or create a new commit in the upstream repo.

**What to show:** PR status in GitHub UI (open → merged), changes landed in upstream.

---

## E — Additional cross-repo demo variations (optional)

* **Backport PR:** create PR from fork into an older branch (e.g., `release/1.x`) to demo backporting. Use `create_pull_request` with base `release/1.x`.
* **Multiple contributors:** Fork into two accounts and create competing PRs to demo conflict resolution.
* **Maintainer pushes to fork:** Show how maintainer can push a small fix branch to the fork if "allow edits by maintainers" is enabled or if the maintainer forks the contributor's fork locally.

---

## F — Verification checklist (what to show the audience)

* Copilot chat returned the fork URL after `fork_repository`. Open it.
* Branch `fix/add-contributing` exists in the fork (show branch selector on fork page).
* PR created in upstream: show PR page (title/body/head pointing to `your-username:fix/add-contributing`).
* `get_pull_request_files` output shows `CONTRIBUTING.md`.
* `get_pull_request_diff` shows the diff.
* After merging (by maintainer): upstream `main` shows `CONTRIBUTING.md`; PR is closed/merged.

---

## G — Troubleshooting & gotchas (fork PRs)

* **Fork creation timing:** Forks are usually immediate, but sometimes take a few seconds to appear in your account. Refresh the repo list if needed.
* **Head/branch naming mistakes:** When creating PR from fork, the head must be `forkOwner:branchName`. If you mistakenly set head to `upstream_owner:branchName` the PR will be invalid. Use the Agent form to ensure head is correct.
* **Permissions & "Allow edits by maintainers":** If maintainers need to push to the fork to make edits, ensure the PR was created with "allow edits from maintainers" (web UI) or coordinate with the maintainer. Some MCP server implementations let you set `maintainer_can_modify` when creating PR — if Agent asks, set it true.
* **Branch protection on upstream:** If upstream has required status checks or branch protection (e.g., required CI), the PR cannot be merged until checks pass. For demo simplicity either: (a) disable protections on the demo repo, or (b) run the CI actions or set checks to passing (or request a maintainer to merge despite checks if permitted).
* **Conflicting changes:** If upstream changed `main` between fork and PR, a maintainer may need to ask for a rebase. The contributor can rebase their fork branch and push an update—Agent can assist with creating the new commit on the fork.
* **Forks in orgs:** If you fork into an org, maintain membership/permission requirements may apply.

---

## H — Demonstration script (compact)

1. `Agent: Fork the repository "demo-streamlit" from owner "upstream_owner" into my account.`
2. `Agent: Create branch "fix/add-contributing" in my fork.`
3. `Agent: Add file "CONTRIBUTING.md" on that branch with the sample content.`
4. `Agent: Create a PR from "your-username:fix/add-contributing" into "upstream_owner:main".`
5. `Agent: List pull requests on "upstream_owner/demo-streamlit" and find the PR.`
6. `Agent: Show files changed in PR #<PR_NUMBER>.`
7. `Agent: Show the PR diff for #<PR_NUMBER>.`
8. `Agent: Request a Copilot review for PR #<PR_NUMBER>.`
   9a. If you are maintainer: `Agent: Merge pull request #<PR_NUMBER> using "squash".`
   9b. If you are contributor: show upstream maintainer the PR and explain merge steps.

---

