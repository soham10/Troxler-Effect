# Troxler Effect Timing

A web-based experiment to measure and collect **Troxler's Fading** data, the perceptual phenomenon where fixating on a central point causes peripheral stimuli to fade from awareness.

Built for **PH314 Optics** by Soham Sahasrabuddhe.

---

## What is Troxler's Fading?

Troxler's fading (or Troxler's effect) is a phenomenon in which a stimulus that is unchanging in the peripheral visual field gradually fades and disappears when one fixates on a central point. This app provides a controlled environment to measure the time it takes for peripheral spots to vanish under different parameters.

---

## Features

- **Interactive canvas** with configurable fixation cross and fuzzy peripheral spots
- **Adjustable parameters** — cross size and spot size with multiple levels
- **Precision timer** using `performance.now()` for accurate sub-second measurements
- **Automatic data saving** to a local SQLite database
- **Results dashboard** with summary statistics, sortable table, search filtering, and CSV export
- **Keyboard shortcuts** for hands-free experiment control
- **Instructions overlay** on first load to guide participants

---

## Project Structure

```
troxler/
├── app.py                  # Flask backend (API + routing)
├── requirements.txt        # Python dependencies
├── troxler_results.db      # SQLite database (auto-created)
└── templates/
    ├── index.html           # Experiment interface
    └── results.html         # Results dashboard
```

---

## Setup & Installation

### Prerequisites

- Python 3.7+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/soham10/Troxler-Effect.git
   cd Troxler-Effect
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

The SQLite database (`troxler_results.db`) is created automatically on first run.

---

## How to Use

### Running the Experiment

1. **Enter your name** in the Participant field on the right panel.
2. **Adjust parameters** — use the +/− buttons or arrow keys to set the Cross Size and Spot Size.
3. **Start the timer** — click Start Timer (or press `Space`) and immediately fix your gaze on the central cross. Do not move your eyes.
4. **Record the vanish** — when the surrounding spots appear to fade or disappear, click Record Vanish (or press `T`). Your time is saved automatically.
5. **Reset and repeat** — press Reset (or `R`) to run another trial.

### Keyboard Shortcuts

| Key        | Action            |
|------------|-------------------|
| `↑` / `↓`  | Adjust cross size |
| `←` / `→`  | Adjust spot size  |
| `Space`    | Start timer       |
| `T`        | Record vanish     |
| `R`        | Reset timer       |

### Viewing Results

Navigate to **View Results →** (top-right) or go to `http://localhost:5000/results` to see:

- **Summary stats** — total trials, mean vanish time, fastest, slowest
- **Sortable table** — click any column header to sort
- **Search** — filter results by participant name
- **Export** — download all data as a CSV file
- **Delete** — remove individual records

---

## API Endpoints

| Method   | Endpoint              | Description                  |
|----------|-----------------------|------------------------------|
| `GET`    | `/`                   | Experiment interface         |
| `GET`    | `/results`            | Results dashboard            |
| `POST`   | `/api/submit`         | Submit a trial result        |
| `GET`    | `/api/results`        | Fetch all results as JSON    |
| `DELETE` | `/api/delete/<id>`    | Delete a specific record     |

### Submit Payload

```json
{
  "name": "Participant Name",
  "cross_size": 25,
  "spot_size": 30,
  "vanish_time": 4.523
}
```

---

## Configuration

Default experiment parameters can be modified in `templates/index.html`:

| Parameter      | Default                 | Description                          |
|----------------|-------------------------|--------------------------------------|
| `CROSS_LEVELS` | `[10, 25, 40, 55, 70]` | Available cross sizes (px)           |
| `SPOT_LEVELS`  | `[20, 30, 40, 50, 60]` | Available spot sizes (px)            |
| `NUM_SPOTS`    | `12`                    | Number of peripheral spots           |
| `RADIUS`       | `210`                   | Distance of spots from center (px)   |
| `SPOT_COLOR`   | `[140, 210, 210]`      | RGB color of spots (pastel teal)     |
| `BG_COLOR`     | `#c8c8c8`              | Canvas background (grey)             |
| `CROSS_COLOR`  | `#323232`              | Fixation cross color (dark grey)     |

---

## License

© 2026 Soham Sahasrabuddhe — Made for PH314 (Course on Optics)
