# 🌟 TikFinity Overlay Editor — Overlayed

A powerful, flexible, and fully customizable overlay editor designed for **TikTok LIVE creators**.  
Manage multiple **TikFinity widgets**, create stunning layouts, save presets, and export clean overlay URLs for OBS or TikTok LIVE Studio.

---
Link: [Overlayed](https://overlayed.rf.gd/)

## 🚀 Highlights
- 🎨 Photoshop‑style controls (drag, resize, rotation, borders)
- 📐 Resolution guides (720p, 1080p, 1440p, 4K)
- 🔍 Canvas zoom (25%–200%)
- 🔒 Lock/unlock system
- 💾 Presets + Auto-save + JSON import/export
- 🔗 Clean external overlay URLs
- 🖱️ Interactive iframe mode
- ⌨️ Keyboard shortcuts
- 🧩 Built-in TikFinity templates

---

## 📸 Preview
> *(Add your own screenshot or GIF here)*  
Example:  
```
[ Your overlay editor preview goes here ]
```

---

## 🧰 Features in Detail

### 🎨 Widget Customization
- Opacity / Transparency  
- Zoom (10%–300%)  
- Rotation (0–360°)  
- Position (X/Y)  
- Custom width/height  
- Layer system (z-index)  
- Border radius, thickness, color, styles  

### 🖼️ Canvas Tools
- Resolution overlays (720p/1080p/1440p/4K)  
- Snap-free resizing  
- Canvas zoom 25–200%  
- Gray contrast background  

### 🧱 Widget Management
- Multi-iframe support  
- Add/Remove widgets  
- Lock individual/all widgets  
- Drag-and-drop movement  
- Photoshop-style resize handles  

---

## 🔗 External Overlay Links
Three ways to generate stream-ready overlay URLs:

### ✔ 1. Preset Mode *(Recommended)*
```
view.html?preset=MyOverlay
```
Updates automatically when the preset changes.

### ✔ 2. Encoded Configuration  
Exports full layout inside the URL (static layout).

### ✔ 3. Auto-save Mode  
Automatically loads your latest layout.

Use in:
- OBS → Browser Source  
- TikTok LIVE Studio → Link Source  

---

## 📁 Project Structure
```
/
├── index.html      # Main editor UI  
├── view.html       # Clean view for streaming  
├── server.py       # Python web server  
├── replit.md       # Documentation  
└── README.md       # Main project README
```

---

## 🖥️ Setup & Run

### ▶ Run Locally
```
python server.py
```

Server runs on:
```
http://localhost:5000
```

### ✔ Requirements
- Python 3.11+
- No external dependencies

---

## 🔧 Technical Notes
- Uses **LocalStorage** to store presets  
- Clean “view mode” removes all UI elements  
- Compatible with OBS, TikTok LIVE Studio, Streamlabs Desktop  

---

## 🎯 TikFinity Integration
- Widgets: https://tikfinity.zerody.one/  
- Gift Overlays: https://tikfinity.zerody.one/tiktok/giftoverlays  
- OBS Overlays: https://tikfinity.zerody.one/tiktok/obsoverlays  

---

## 📝 Changelog
### v1.2
- Resolution guides  
- Canvas zoom  
- Gray background  

### v1.1
- External overlay links  

### v1.0
- Multi-widget editor with presets  

---

## 💬 Support
If you need help with TikFinity widgets, visit the official docs.

---

## 👤 Author
Created by **Felipe Fernandes (BadWise)**  
Designed for professional **TikTok LIVE streamers**.
