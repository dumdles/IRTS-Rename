from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import shutil

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/rename-folders', methods=['POST'])
def rename_folders():
    data = request.json
    folder_path = data['folder_path']
    company_initials = data['company_initials']
    report_count = data['report_count']

    current_date = datetime.now()
    year = current_date.strftime("%y")
    month = current_date.strftime("%m")
    report_number = str(report_count).zfill(2)

    new_folder_name = f"IRTS-{year}{month}-{report_number}-{company_initials}"
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)

    try:
        os.rename(folder_path, new_folder_path)
        return jsonify({"message": "Folder renamed successfully", "new_folder_path": new_folder_path})
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True)