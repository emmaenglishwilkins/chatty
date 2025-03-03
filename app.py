from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Generate static file
    output_dir = "static_site"
    os.makedirs(output_dir, exist_ok=True)

    html = render_template("index.html")
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(html)

    print(f"✅ Static site generated at {output_dir}/index.html")
