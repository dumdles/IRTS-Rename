from flask import Flask, request, jsonify
import os
from datetime import datetime
import shutil

app = Flask(__name__)

@app.route('/rename-folders', method=['POST'])
def rename_folders():
    data = request.json
    folder_path = data['folder_path']
    company_initials = data['company_initials']
    report_count = data['report_count']

    current_date = datetime.now()
    year = current_date.stfrtime("%y")
    month = current_date.stfrtime("%m")
    report_number = str(report_count).zfill(2)

    new_folder_name = f"IRTS-{year}{month}-{report_number}-{company_initials}"
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)

    try:
        os.rename(folder_path, new_folder_path)
        return jsonify({"message": "Folder renamed successfully", "new_folder_path": new_folder_path})
    except Exception as e:
        return jsonify({"message": stre(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True)