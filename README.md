# CS50P_Final_Project: Starling Curve Visualization

#### Video Demo:  <URL HERE>
## Description:

This Python script calculates stroke volume (SV), cardiac output (CO) and left ventricular end diastolic pressure (LVEDP) and plots it on a Starling curve graph. The Starling curve represents the relationship between LVEDP and SV. The curve was generated using an array of points extrapolated from mulitple textbook sources. The starling curve is an approximation of muscle fiber shortening and elongating in response to changes in preload entering the heart. It is difficult to measure all of these values directly without invasive monitors placing a patient at risk. This python script attempts to use the least invasive testing possible and extrapolate a point along the starling curve for the patient at that time. This should help the clinician guide resusicitation measures. 

## Usage

1. Ensure you have Python 3 installed on your machine.

2. Install the required libraries using pip:
   ```bash
   pip install matplotlib

3. Run the script:
   ```bash
   python project.py

## Python Script Breakdown
The script uses predefined variables for age, systolic blood pressure (sbp), diastolic blood pressure (dbp), body surface area (bsa), oxygen saturation (SaO2), mixed venous oxygen saturation (SvO2), hemoglobin (hgb), ejection fraction (ef), and heart rate (hr) to calculate mean arterial pressure (MAP), cardiac output (CO) using the modified Fick method, SV, and LVEDP. Some variables are calcuated using separate functions which are defined below. The rest are constants and can be changed from the script. The script then generates a plot of the normal Starling curve and highlights a specific point representing the calculated SV and LVEDP for the provided patient.

### map_calc():
Calculates MAP based on systolic and diastolic blood pressure using the common formula.

### co_fick_calc():
Calculates CO using the modified Fick method. This requires the patient age, bsa, SaO2, SvO2, and hgb. These values should be drawn from an arterial sample and from a pulmonary artery catheter sample. Age and bsa create the Vo2 max variable while the rest of the parameters make up the arterial and venous oxygen capacity. 

### sv_calc():
Calculates SV based on the CO obtained in the above function and HR which is supplied. SV is in ml so take care to input the correct CO, and HR so the equation and convert for you. 

### Patient Specific Point
This point in red on the plot shows the patients approximate position on the starling curve. Refer to the graphic below to help with interpretation. The example reference shows the patient to be requiring some fluid and some inotropic support. This point required an LVEDP calculation since we are striving for limiting invasive procedures. The equation was found in Abd-El-Aziz TA. Noninvasive prediction of left ventricular end-diastolic pressure in patients with coronary artery disease and preserved ejection fraction. Can J Cardiol. 2012 Jan-Feb;28(1):80-6. doi: 10.1016/j.cjca.2011.02.001. Epub 2011 Jul 2. PMID: 21723693. The equation is as follows: LVEDP = [0.54 MABP × (1 - EF)] - 2.23. This was the best of three equations defined in the paper above and had an r value of approximately 0.8.
[https://en.wikipedia.org/wiki/Frank%E2%80%93Starling_law](images/image.png)

## Example Output
[example output](images/starling.png)
## Future Updates
Creating an exe, with GUI and modifiable variables possibly with sliders to illustrate how certain changes will impact the patient. 

## License
This project is licensed under the MIT License


