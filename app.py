from flask import Flask, render_template
import os

app = Flask(__name__)

# Ensure the output directory exists
output_dir = "static_site"
os.makedirs(output_dir, exist_ok=True)

# Use the application context to render the template
with app.app_context():
    html = render_template("index.html")
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(html)

print(f"✅ Static site generated at {output_dir}/index.html")
