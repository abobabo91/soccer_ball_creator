# ⚽ Soccer Ball Creator

A small project for generating and visualizing 3D soccer ball textures from any image.

You can either:
- Run the **Python version** for a scripted, `matplotlib`-based visualization, or
- Open the **HTML version** for an interactive, real-time 3D preview in your browser.

---

## 🧩 Files

### `soccer_ball_creator.py`
A simple Python script that maps a flat image onto a mirrored spherical surface.

**Features**
- Uses `matplotlib` to render a mirrored 3D soccer ball.  
- Adjustable triangle sides and pixel density.  
- Great for testing texture layouts.

**Usage**
```bash
pip install pillow numpy matplotlib
python soccer_ball_creator.py
