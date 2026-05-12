# ⚽ Soccer Ball Creator

Map any image onto a 3D soccer-ball surface. Two implementations:

- **`soccer_ball_creator.py`** — Python script using `matplotlib` to render a mirrored 3D soccer ball. Adjustable triangle sides + pixel density.

  ```bash
  pip install pillow numpy matplotlib
  python soccer_ball_creator.py
  ```

- **`soccer_ball_standalone_v8.html`** — single-file browser app with a live interactive 3D preview (Three.js-style canvas, dual-pane layout). Open the HTML file directly in any modern browser — no server, no build step.

## Where it lives

- **Repo**: https://github.com/abobabo91/soccer_ball_creator (private)
- **Deployment**: not deployed. The HTML is runnable locally only — open the file in a browser. (Sibling repo `soccer_free_kick` is published on GitHub Pages; this one isn't.)
