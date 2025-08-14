# 🧮 STATISTICS Answer Checker (React + FastAPI)

🎯 **Project Overview**  
STATISTICS Answer Checker is a full-stack web application designed to calculate and visualize basic statistics. Users input a list of numbers in the React frontend, which communicates with a FastAPI backend to return sorted values, median, quartiles, IQR, and outlier fences. Perfect for students, educators, or anyone analyzing small datasets interactively.

---

## 🌟 Key Features
- **Interactive UI** – Real-time input of numbers and immediate statistical output.  
- **Full Statistics Calculation** – Length, min, max, range, most frequent number, median, Q1, Q3, IQR, upper/lower fences.  
- **Sorting Algorithm** – Demonstrates insertion sort visually and numerically.  
- **Frontend/Backend Communication** – React sends data to FastAPI; CORS enabled for development.  
- **Responsive Design** – Works on both desktop and mobile devices.  

---

## 🏗️ Architecture & Tech Stack
### 🛠️ Core Technologies
- **Frontend:** React, Vite, Axios, CSS  
- **Backend:** FastAPI, Python 3.10+  
- **Other Tools:** Node.js, npm, Git  

---

## 📂 Repository Structure
```
STATISTICS-Answer-checker/
  ├─ my-react-app/
  │  ├─ backend/
  │  │  ├─ main.py                  # FastAPI app with /calculate
  │  │  └─ requirements.txt         # fastapi, uvicorn
  │  ├─ src/
  │  │  ├─ components/
  │  │  │  └─ StatsCalculator.jsx   # Main UI component
  │  │  ├─ styles/
  │  │  │  └─ StatsCalculator.css   # Component styles
  │  │  ├─ App.jsx                  # Renders StatsCalculator
  │  │  ├─ main.jsx                 # App entry point
  │  │  ├─ index.css                # Global styles (import in main.jsx)
  │  │  └─ assets/                  # Optional images (background, etc.)
  │  ├─ public/                     # Static assets (served at /)
  │  ├─ package.json                # React/Vite scripts and deps
  │  └─ vite.config.js
  └─ LICENSE
```

## ⚡Backend Setup (FastAPI)
1) Open a terminal:
```
cd my-react-app/backend
python -m venv .venv
# Windows PowerShell
. .venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Backend runs at `http://127.0.0.1:8000`.

### ⚡API
- POST `/calculate`
- Request JSON:
```json
{ "numbers": [5, 2, 9, 1, 5, 6] }
```
- Response JSON:
```json
{
  "length": 6,
  "before": [5,2,9,1,5,6],
  "after": [1,2,5,5,6,9],
  "max": 9,
  "min": 1,
  "range": 8,
  "mostFrequent": 5,
  "median": 5,
  "Q1": 2,
  "Q3": 6,
  "IQR": 4,
  "upperFence": 12,
  "lowerFence": -4
}
```

## ⚡ Frontend Setup (React + Vite)
1) In another terminal:
```
cd my-react-app
npm i
npm i axios
npm run dev
```
2) Open the dev server URL printed in the terminal (typically `http://localhost:5173`).

If global styles aren’t applying, ensure `index.css` is imported in `src/main.jsx`:
```js
import "./index.css";
```
## ⚠️ Common Troubleshooting
- Vite import error (Failed to resolve import):
  - Prefer src‑relative imports like `import X from "./components/X.jsx";`
  - Restart the dev server and hard refresh the browser (Ctrl+F5).
- Windows PowerShell command chaining:
  - `&&` may not work; run commands on separate lines or use `;`.
- Node engine warnings:
  - Vite 7 prefers Node 20.19+. Upgrading removes warnings.
- CORS errors:
  - Backend currently allows all origins for dev. In production, set `allow_origins=["http://your-frontend"]`.
- CSS changes not taking effect:
  - Ensure `import "./index.css";` exists in `src/main.jsx`.
  - Clear Vite cache (`node_modules/.vite`) and restart `npm run dev` if needed.

## 🧪 Scripts
From `my-react-app`:
- `npm run dev` – start dev server
- `npm run build` – production build
- `npm run preview` – preview build

## 📝 License
Open‑source under MIT. Built with ❤️ by Ruchira Tharupathi.  
 

 
