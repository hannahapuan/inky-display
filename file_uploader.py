import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from PIL import Image
from inky.auto import auto

app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = "uploads"
THUMBNAIL_FOLDER = "uploads/thumbnails"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["THUMBNAIL_FOLDER"] = THUMBNAIL_FOLDER

# Detect and initialize the Inky Impression 7.3"
inky = auto(ask_user=True, verbose=True)
target_width, target_height = 800, 480  # Inky Impression resolution

def create_thumbnail(image_path):
    """Creates a thumbnail of the uploaded image."""
    img = Image.open(image_path)
    img.thumbnail((150, 150))  # Resize to 150x150 for thumbnails
    thumbnail_path = os.path.join(THUMBNAIL_FOLDER, os.path.basename(image_path))
    img.save(thumbnail_path)
    return thumbnail_path

@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = None

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                # Create thumbnail
                create_thumbnail(filepath)

                message = "File uploaded successfully!"

    # Get list of uploaded images
    images = os.listdir(app.config["UPLOAD_FOLDER"])
    images = [img for img in images if img.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif"))]

    return render_template("index.html", message=message, images=images)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/uploads/thumbnails/<filename>")
def thumbnail_file(filename):
    return send_from_directory(app.config["THUMBNAIL_FOLDER"], filename)

@app.route("/set-image/<filename>")
def set_image(filename):
    """Sets the selected image on the Inky display."""
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if os.path.exists(filepath):
        img = Image.open(filepath)

        # Rotate if needed
        if img.height > img.width:
            img = img.rotate(90, expand=True)

        # Convert and resize
        img = img.convert("RGB")
        img = img.resize((target_width, target_height), Image.LANCZOS)

        try:
            inky.set_image(img, saturation=1)
        except TypeError:
            inky.set_image(img)

        inky.show()
    
    return redirect(url_for("upload_file"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


