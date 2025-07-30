# spacebar-counter

A simple Python CLI tool to count your spacebar presses per day and visualize your stats!

## Installation

Install from PyPI:
```bash
pip install spacebar-counter
```

Or install the latest version from GitHub:
```bash
pip install git+https://github.com/<your-username>/<your-repo>.git
```

## Usage

Start tracking your spacebar presses:
```bash
spacebar-counter start
```
- This will count your spacebar presses for the current day.
- The count resets automatically at midnight.

Generate a dashboard:
```bash
spacebar-counter dashboard
```
- This creates `spacebar_dashboard.html` in your project directory.
- Open it in your browser to see your daily spacebar stats as a dot plot.

## Data Storage

- Your stats are stored in a local file called `spacebar_stats.json` in the same directory as the tool.
- For each day, it stores:
  - The date
  - The total count
  - The first and last time you pressed the spacebar that day

## Requirements

- Python 3.7+
- `pynput`
- `plotly`
- `typer`

## License

MIT

---

**Tip:**  
- Add a "Features" section if you want to highlight more.
- Add a "Contributing" section if you want others to help improve your tool.

---

Would you like me to update your README.md for you? If so, let me know your GitHub username and repo name, or I can leave placeholders for you to fill in!