# soccer_ball_creator

Generates 3D soccer-ball textures from a flat image. Two surfaces:
- `soccer_ball_creator.py` — Python + matplotlib scripted visualization
- `soccer_ball_standalone_v8.html` — single-file interactive 3D preview in the browser

## Critical rules

- The HTML version is **intentionally single-file** (`soccer_ball_standalone_v8.html`). No build, no dependencies. Don't split it into modules.
- The two surfaces (Python + HTML) are independent. Don't try to share logic between them — different rendering pipelines.
- The version suffix in the HTML filename (`v8`) suggests there have been iterations. If you make a substantive change, bump the version OR replace in-place if it's a bugfix — match the existing naming intent.

## Stack & run

- **Python**: `pip install pillow numpy matplotlib && python soccer_ball_creator.py`
- **HTML**: open `soccer_ball_standalone_v8.html` directly in a browser (no server, no build)

## Where things live

- Python entry: `soccer_ball_creator.py`
- HTML entry: `soccer_ball_standalone_v8.html` (current version)
- Sample images / reference: `images/`
- License: `LICENSE`

## Gotchas

- The Python version uses **mirrored spherical projection** — it deliberately mirrors the texture for visual symmetry. If you change the projection math, document why.
- HTML 3D rendering likely uses three.js or canvas (verify by reading the file). Browser WebGL support is required.
- Triangle subdivision count + pixel density are tunable in the Python script — defaults are calibrated for visual clarity, not performance.
