# 🌟 TikFinity Overlay Editor — Overlayed

A powerful, flexible, and fully customizable overlay editor designed for **TikTok LIVE creators**.  
Manage multiple **TikFinity widgets**, create stunning layouts, save presets, and export clean overlay URLs for OBS or TikTok LIVE Studio.

---
Link: [Overlayed](https://overlayed.stromsv.xyz/)

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
<img width="1902" height="882" alt="{BBC038FD-DED7-4AAB-9F18-49888A50D9E3}" src="https://github.com/user-attachments/assets/64c05b49-3f49-4748-bf25-d4c6b862a266" />
<img width="1859" height="932" alt="{ADC79752-20F4-42FF-8838-CEFDFDDEB7AA}" src="https://github.com/user-attachments/assets/4732be8a-44bd-4e1f-99d9-7b60ce1b48ef" />
<img width="821" height="777" alt="{1898C8C2-CD7A-4B38-BEE2-C63C917D1189}" src="https://github.com/user-attachments/assets/8c687ee1-1d18-46f8-babf-d8804b75e1cb" />
<img width="585" height="418" alt="{54493857-9AD6-45A1-8904-CE5347B61358}" src="https://github.com/user-attachments/assets/f42cabac-e4d0-4f3e-94fd-7ceb6af64b36" />


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
