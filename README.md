# Inky Impression 7.3" Flask Image Uploader

This project provides a Flask-based web interface for uploading and selecting images to display on a **Pimoroni Inky Impression 7.3" e-paper display**. It allows users to:
- Upload images via a web interface.
- View a gallery of previously uploaded images.
- Click an image thumbnail to set it as the active display on the Inky Impression.

## Features
✅ Upload images through a web interface.  
✅ Generate thumbnails for easy selection.  
✅ Auto-rotate images if necessary.  
✅ Web-based control for selecting images.  

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/hannahapuan/inky-display.git
cd inky-image-uploader
```

### 2. Install Dependencies
Ensure you have Python 3 installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Create Upload Folders
```bash
mkdir -p uploads/thumbnails
```

### 4. (Optional) Add to startup script (this specifies the impression7.3 inky screen)
Create/edit `/etc/rc.local`
```bash

```

## Usage
### 1. Run the Flask App
```bash
python app.py
```

### 2. Access the Web Interface
Once the server is running, open a browser and go to:
```
http://<YOUR_RASPBERRY_PI_IP>:8080
```
Example:
```
http://192.168.1.100:8080
```

### 3. Upload an Image
1. Select an image from your computer.
2. Click **Upload**.
3. The image will be stored in the `uploads/` folder, and a thumbnail will be generated.

### 4. Select an Image to Display
- Click on any **thumbnail** from the gallery.
- The selected image will be **resized and displayed** on the Inky Impression.

## Project Structure
```
inky-image-uploader/
│── static/                  # CSS and other static assets
│── templates/
│   ├── index.html           # Web interface
│── uploads/                 # Stores uploaded images
│── uploads/thumbnails/      # Stores generated thumbnails
│── app.py                   # Flask application
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

## Troubleshooting
### 1. Flask App Not Running?
- Ensure all dependencies are installed:  
  ```bash
  pip install -r requirements.txt
  ```
- Try running Flask with `sudo` if permissions are an issue.

### 2. No Images Appearing in the Gallery?
- Make sure images are stored in `uploads/`.
- Restart the Flask app.

### 3. Image Not Displaying on Inky?
- Ensure the **Inky Impression is properly connected**.
- Try running:
  ```bash
  python -c "from inky.auto import auto; inky = auto(ask_user=True, verbose=True); inky.show()"
  ```
  This will confirm if the display is working.

### 4. Find Your Raspberry Pi's IP
Run:
```bash
hostname -I
```
Or check your router's admin panel.

## Future Enhancements
- 🔄 **Auto-refresh gallery** after an upload.
- 🛠️ **Delete uploaded images** from the web UI.
- 🌐 **Add support for remote image uploads.**

## License
This project is **open-source** under the MIT License.

Enjoy using your Inky Impression as a **dynamic e-paper display!** 🎉