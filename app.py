from flask import Flask, request, send_file
from flask_cors import CORS
import os

from ppt_generator import create_ppt

app = Flask(__name__)
CORS(app, origins=["https://papaya-donut-9b9b21.netlify.app/"])

@app.route("/")
def home():
    return "Flask Backend Running"

@app.route("/generate-ppt", methods=["POST"])
def generate_ppt():

    report_data = request.json

    print("Received Data:")
    print(report_data)

    ppt_path = create_ppt(report_data)

    return send_file(
        ppt_path,
        as_attachment=True,
        download_name="Demand_Planning_Report.pptx"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)