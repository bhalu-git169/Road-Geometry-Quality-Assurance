# 🚦 Road Geometry Quality Assurance
### 📌 Overview
This project focuses on validating road network data by detecting invalid road geometries before they are used in analytics or AI systems.

Road datasets often contain errors such as zero-length roads or invalid coordinates. These issues can break routing, distort analysis, and reduce model reliability. Our solution performs rule-based quality checks to identify such issues efficiently.

## 🧩 Problem Statement
 - Given a dataset of road geometries represented as LINESTRING objects, the task is to:

 - Detect invalid road segments

 - Identify the reason for invalidity

 - Produce structured outputs for further analysis

## 🛠️ Solution Approach
  We implemented a rule-based validation pipeline:

   - Read road geometries from the dataset

   - Parse coordinates from each LINESTRING
  
   - Apply validation rules:

   - Zero-length road detection
  
   - Coordinate range validation

   - Flag invalid roads with reasons
  
   - Generate structured output for analysis

## 🔁 Flowchart
  Below is the flowchart representing the validation logic:
  
<img width="600" height="785" alt="Screenshot 2026-02-07 153937" src="https://github.com/user-attachments/assets/3c23f5f0-5b3e-4290-bca2-9c88b3b02891" />

## ⚙️ Technical Implementation
Language: Python

Libraries:

 - Python Standard Library

- pandas (for structured reporting)

 Key checks implemented:

- All points identical → Zero-length road

- Coordinates outside allowed bounds → Invalid geometry

 - Malformed entries → Safely handled

## 📊 Example Errors Detected

Zero-Length Road: LINESTRING (10 10, 10 10, 10 10)  <br/>
Out-of-Range Coordinates: LINESTRING (500 500, 12000 300) <br/>
Single-Point Road: LINESTRING (200 300)

## 📈 Output & Results

- Invalid road geometries are printed with reasons

- Results are stored in a structured CSV format

  ### 📷  output screenshots

<img width="400" height="340" alt="image" src="https://github.com/user-attachments/assets/cb0e1b78-d2a8-4dbf-804b-01736ebe5c9f" /> <br/>

Output In CSV File: <br/>

<img width="400" height="340" alt="image" src="https://github.com/user-attachments/assets/a04fae56-1b3a-4678-a5a8-3c6b805458e6" />


## 🧪 Validation & Testing
- Tested using known invalid geometries

- Verified edge cases such as identical points and invalid coordinates

- Ensured the script runs without crashing on malformed data

  ## 🚀 Real-World Use Cases
- Data quality checks before GIS analysis

- Preprocessing step for ML models using spatial data

- Validation during map data ingestion pipelines


## ⚠️ Limitations
- Rule-based validation only

- Supports LINESTRING geometries

- No automatic correction or visualization

## 🔮 Future Improvements
- ML-based anomaly detection

- Support for more geometry types

- Map-based visualization

- Auto-correction suggestions

## ▶️ How to Run
``` 
pip install -r requirements.txt
python validate_roads.py
```

## 📂 Project Structure
```
validate_roads.py
requirements.txt
README.md
outputs/
```

### 📜 Declaration
We confirm that this submission is our own work and was developed during the hackathon period.
