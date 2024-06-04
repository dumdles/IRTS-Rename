from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/create-folders', methods=['POST'])
def create_folders():
    data = request.json
    report_type = data['report_type']
    company_initials = data['company_initials']
    report_count = data['report_count']
    customer_name = data['customer_name']

    current_date = datetime.now()
    year = current_date.strftime("%Y")
    month = current_date.strftime("%m")
    report_number = str(report_count).zfill(2)

    # Update base folder path based on report type
    base_folder_path = os.path.normpath("F:/Reports2")
    if report_type == "IRTS":
        folder_path = os.path.join(base_folder_path, report_type, year)
        report_folder_name = f"{report_type}-{year[2:]}{month}-{report_number}"
    elif report_type == "DGA":
        folder_path = os.path.join(base_folder_path, report_type, year)
        report_folder_name = f"{report_type}-{year[2:]}{month}-{report_number}"
    elif report_type == "PQA":
        folder_path = os.path.join(base_folder_path, report_type, year)
        report_folder_name = f"{report_type}-{year[2:]}{month}-{report_number}"
    else:
        return jsonify({"message": "Invalid report type", "error": True}), 400

    new_folder_name = f"{report_folder_name}-{company_initials} @ {customer_name}"
    final_folder_path = os.path.join(folder_path, new_folder_name)

    try:
        os.makedirs(os.path.dirname(final_folder_path), exist_ok=True)
        os.makedirs(final_folder_path, exist_ok=True)
        return jsonify({"message": "Folder created successfully", "new_folder_path": final_folder_path})
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)