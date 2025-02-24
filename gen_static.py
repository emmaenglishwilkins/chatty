import os
from app import app

def save_static_html():
    pages = [""]  # Add more routes if needed

    os.makedirs("static_site", exist_ok=True)  # Create output folder

    with app.test_request_context():
        for page in pages:
            url = f"/{page}" if page else "/"
            file_name = "index.html" if not page else f"{page}.html"

            response = app.test_client().get(url)
            with open(f"static_site/{file_name}", "w", encoding="utf-8") as file:
                file.write(response.data.decode("utf-8"))
    
    print("Static site generated successfully!")

if __name__ == "__main__":
    save_static_html()
