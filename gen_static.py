from flask import render_template
import os

# Ensure the output directory exists
output_dir = "static_site"
os.makedirs(output_dir, exist_ok=True)

# Render and save the index.html file
html = render_template("index.html")
with open(os.path.join(output_dir, "index.html"), "w") as f:
    f.write(html)

print(f"✅ Static site generated at {output_dir}/index.html")
