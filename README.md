# AC Tesla Report Folder Create

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **AC Tesla Report Folder Create** tool! This internal tool is designed to help you create new report folders in your NAS with the proper naming conventions effortlessly. Whether you're dealing with IRTS, DGA, PQA, or PD reports, this tool streamlines the process and ensures consistency.

## Features

- **User-Friendly Interface**: Easy-to-use web interface for folder creation.
- **Automatic Naming Convention**: Generates folder names based on report type, date, and other parameters.
- **File Upload**: Supports uploading multiple files to the newly created folders.
- **Error Handling**: Validates inputs and provides meaningful error messages.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Werkzeug
- Web Browser

## Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/dumdles/IRTS-Rename.git   
2. **Install Dependencies**  
```pip install -r requirements.txt```

3. **Run the Flask Server**  
```python backend.py```

4. **Access the Application**  
Open your web browser and go to http://localhost:5000.

5. **Usage**  
   - Open the Application  
   - Open your web browser and navigate to http://localhost:5000.  
   - Fill in the Form  
   - Select the report type (IRTS, DGA, PQA, PD).  
   - Select files to upload (optional).  
   - Choose the company initials.  
   - Enter the report count.  
   - Enter the customer name (letters and numbers only).  
   - Select the inspection start date and end date (if applicable).  
   - Create the Folder  

   - Click the "Create Folder" button. The tool will create the folder with the specified naming convention and upload the files if provided.  

## API Endpoints
**Create Folders**  
URL: /create-folders  
Method: POST  
Description: Creates a new folder and uploads files based on the provided form data.  
Request Data:  
```report_type```: The type of the report (IRTS, DGA, PQA, PD).
```files```: The files to be uploaded (optional).  
```company_initials```: The initials of the company.  
```report_count```: The report count for the month.  
```customer_name```: The name of the customer (letters and numbers only).  
```inspection_start_date```: The start date of the inspection.  
```inspection_end_date```: The end date of the inspection (optional).  
```Response```:  
```message```: A success or error message.  
```new_folder_path```: The path of the newly created folder (on success).

## Contributing
We welcome contributions! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed by Dylan Chong (dumdles).