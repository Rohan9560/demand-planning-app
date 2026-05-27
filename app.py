from flask import Flask, request, send_file
from flask_cors import CORS

from ppt_generator import create_ppt

app = Flask(__name__)
CORS(app)

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
    app.run(debug=True, port=5000)