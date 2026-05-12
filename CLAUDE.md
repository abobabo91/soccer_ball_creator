# soccer_ball_creator

Single-page in-browser tool that maps an uploaded image onto a 3D soccer-ball sphere (WebGL, vanilla JS). Deployed to GitHub Pages at `https://abobabo91.github.io/soccer_ball_creator/`.

## Critical rules

- NEVER introduce a build step, bundler, or dependency. The project is **intentionally single-file** (`index.html`) with zero build pipeline — that's the design.
- All JS, CSS, and shaders live inline in `index.html`. Don't extract to a shared `.js` / `.css` file without a strong reason.
- Pages are deployed as-is via GitHub Pages on push to `main` — no CI, no build artifacts. Anything that touches Pages config affects the live URL.

## Stack & run

- Pure HTML + WebGL + vanilla JS — no framework, no bundler
- Run locally: open `index.html` directly in a browser (no server needed)
- Deploy: push to `main` → GitHub Pages serves from repo root

## Where things live

- `index.html` — the entire app (left pane: 2D canvas image uploader with pan/zoom; right pane: WebGL textured sphere)
- `screenshots/` — README images

## Gotchas

- All assets load directly from the repo root via GitHub Pages — paths must be relative, not absolute.
- The fragment shader tiles the texture with a mirrored-coordinate function (`mc`) — that's deliberate, it's what produces the symmetric ball-panel look. Don't "fix" it.
- `Sides` (default 4) controls horizontal tile count; `Hemisphere Mirror` doubles vertical tiling. Both are uniforms hot-swapped without rebuilding the mesh.
- WebGL is required. If `gl` is null the script alerts and exits.
