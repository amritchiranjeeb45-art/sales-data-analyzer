# Sales Data Analyzer

Simple beginner Python project for Business Analytics practice.

**What it does**
- Loads sales data from `sample_data.csv`
- Calculates KPIs: total sales, average order value, top-selling product, monthly totals
- Saves a line plot of monthly sales to `monthly_sales.png`
- Exports a summary CSV `summary.csv`

**Run locally**
1. Create a Python 3.8+ virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows PowerShell
   ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run:
   ```
   python main.py
   ```

**Files**
- `main.py` — main script
- `sample_data.csv` — example sales data
- `summary.csv` — output summary (generated)
- `monthly_sales.png` — output plot (generated)

