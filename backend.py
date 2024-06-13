from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import re
from shutil import copy2
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/create-folders', methods=['POST'])
def create_folders():
    data = request.form # Access form data, including files
    files = request.files.getlist('files') # Get a list of uploaded files

    report_type = data['report_type']
    company_initials = data['company_initials']
    report_count = data['report_count']
    customer_name = data['customer_name']

    inspection_start_date = data.get('inspection_start_date')
    inspection_end_date = data.get('inspection_end_date')
        
    # Continue with folder creation logic
    current_date = datetime.now()
    year = current_date.strftime("%Y")
    month = current_date.strftime("%m")
    report_number = str(report_count).zfill(2)

    # Check for missing or empty customer_name
    if 'customer_name' not in data or not data['customer_name'].strip():
      return jsonify({"message": "Customer name is required!", "error": True}), 400

    # Validate customer name for alphanumeric characters only
    if not re.match(r"^[a-zA-Z0-9]+$", customer_name):
        return jsonify({"message": "Customer name must contain only alphanumeric characters!", "error": True}), 400
    
    # Validate Dates
    if inspection_start_date:
        start_date_obj = datetime.strptime(inspection_start_date, "%Y-%m-%d")
    else:
        return jsonify({"message": "Inspection start date is required!", "error": True}), 400
    
    if inspection_end_date:
        end_date_obj = datetime.strptime(inspection_end_date, "%Y-%m-%d")
        if end_date_obj < start_date_obj:
            return jsonify({"message": "Inspection end date cannot be before the inspection start date!", "error": True}), 400

    # Update base folder path based on report type
    base_folder_path = os.path.normpath("F:/Reports2")  # Change folder location here, if needed
    if report_type in ["IRTS", "PQA", "ELP", "PD", "DGA"]:
        folder_path = os.path.join(base_folder_path, report_type, year)
        report_folder_name = f"{report_type}-{year[2:]}{month}-{report_number}"
    else:
        return jsonify({"message": "Invalid report type", "error": True}), 400
    
    # Format inspection dates
    def format_date(date_str):
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%d.%m.%y")
        return ""
    
    formatted_start_date = format_date(inspection_start_date)
    formatted_end_date = format_date(inspection_end_date)

    new_folder_name = f"{report_folder_name}-{company_initials} @ "
    if formatted_start_date:
        new_folder_name += f"{formatted_start_date}"
        if formatted_end_date:
            new_folder_name += f" to {formatted_end_date}"
    else:
        new_folder_name += ""
        pass
    new_folder_name += f"_{customer_name}"
    final_folder_path = os.path.join(folder_path, new_folder_name)

    try:
        os.makedirs(os.path.dirname(final_folder_path), exist_ok=True)
        os.makedirs(final_folder_path, exist_ok=True)

        # Process uploaded files only if there are files to upload
        if files:
            for file in files:
                if file.filename:  # Ensure the filename is not empty
                    filename = secure_filename(file.filename)
                    destination_path = os.path.join(final_folder_path, filename)
                    try:
                        file.save(destination_path)  # Save the file to the destination path
                    except Exception as e:
                        return jsonify({"message": f"Error copying file {filename}: {str(e)}", "error": True}), 400

        return jsonify({"message": "Folder created and files uploaded successfully!", "new_folder_path": final_folder_path})
    except Exception as e:
        return jsonify({"message": f"Folder creation failed: {str(e)}", "error": True}), 400

if __name__ == "__main__":
    cert_path = r'C:\Program Files\OpenSSL-Win64\bin\PEM\cert.pem'
    key_path = r'C:\Program Files\OpenSSL-Win64\bin\PEM\key.pem'
    
    if os.path.exists(cert_path) and os.path.exists(key_path):
        print(f"Using SSL cert: {cert_path} and key: {key_path}")
    else:
        print(f"SSL cert or key not found at paths: {cert_path}, {key_path}")
    
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context=(cert_path, key_path))