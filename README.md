# 💕 Valentine's Day Website

A playful and romantic Valentine's Day website where the "No" button runs away when you try to click it, and the "Yes" button plays a special video!

## Features

✨ **Interactive Elements:**
- Floating heart animations in the background
- "Yes" button that plays a romantic video when clicked
- "No" button that dodges away when you try to hover/click on it
- The "Yes" button grows bigger each time you avoid the "No" button
- Celebration effect when "Yes" is clicked

🎨 **Beautiful Design:**
- Gradient purple background
- Smooth animations and transitions
- Responsive design that works on mobile and desktop
- Custom fonts (Pacifico & Quicksand)

## How to Run

### Option 1: Using Python Flask Server

1. Make sure you have Python installed
2. Install Flask:
   ```bash
   pip install flask
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. Open your browser and go to: `http://localhost:5000`

### Option 2: Direct HTML (Simple)

Just open `valentine.html` directly in your web browser by double-clicking the file!

## Customization

### Change the Video

In `valentine.html`, find this line (around line 213):
```html
src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"
```

Replace the video ID (`dQw4w9WgXcQ`) with your preferred YouTube video ID.

### Change the Question

Find this line in `valentine.html`:
```html
Will you be my Valentine? 🌹
```

Change it to whatever question you want!

### Modify Colors

The main gradient colors are defined in the CSS:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change these hex color codes to your preferred colors!

## Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python Flask (optional)
- **Fonts:** Google Fonts (Pacifico, Quicksand)
- **Video:** YouTube embed

## Browser Compatibility

Works on all modern browsers:
- Chrome
- Firefox
- Safari
- Edge

## License

Feel free to use this for your Valentine! 💝

---

Made with ❤️ for Valentine's Day
# valentine
