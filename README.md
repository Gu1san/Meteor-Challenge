# Pixel Analysis

## 🖼️ Overview  
**Pixel Analysis** is a Python script that processes an image to detect and analyze specific elements: stars, meteors, and water. By identifying and counting these elements, the script determines how many meteors fall into water and extracts relevant pixel coordinates.

## ✨ Features  
- **Star and Meteor Detection**  
  - Identifies stars and meteors based on predefined colors.  
  - Counts the total number of detected stars and meteors.
  
- **Water Level Analysis**  
  - Determines the water level in the image.  
  - Identifies which columns contain water.
  
- **Impact Calculation**  
  - Checks which meteors are aligned with water columns.  
  - Counts the number of meteors that fall into water.

## 🔧 Technologies Used  
- **Python** for scripting and automation.  
- **Pillow (PIL)** for image processing.  

## 📜 Code Structure  
The script follows these steps:
1. **Load Image**: Opens and processes the image in RGB format.  
2. **Identify Elements**: Iterates through pixels to detect stars, meteors, and water.  
3. **Determine Water Level**: Scans for the first water pixel in each column.  
4. **Analyze Impact**: Checks which meteors are positioned above water columns.  
5. **Output Results**: Displays the number of detected elements and meteors that land in water.  

## 🚀 Running the Script  
To run the script, ensure you have Python installed along with the Pillow library:
```bash
pip install pillow
```
Then, execute the script with an image file named `img.png`:
```bash
python script.py
```

## 📊 Example Output  
```
Stars: 42
Meteors: 15
Meteors falling into water: 5
```

## 💡 Learnings and Insights  
- Gained experience in **image processing** using Python.  
- Learned how to analyze pixel data efficiently.  
- Developed logic to track object interactions within an image.  

