# A number of medical equation functions for use with python programming
from math import sqrt

#Metric formula for bmi given height in cm converts to m^2
def bmi_calc (w, h): 
    bmi = w / (h / 100)**2
    return round(bmi)

#Metric formula for bmi given height in cm and weight in kg
def bsa_calc (h, w):
    bsa = sqrt((h * w) / 3600)
    return round(bsa, 2)

#James formula for lean body weight in kg
def lbm_calc(g, w, h): 
    if g == 'm':
        lbm = 1.1 * w - 128 * (w / h)**2
    elif g == 'f':
        lbm = 1.07 * w - 148 * (w / h)**2
    return round(lbm)

#Metric ideal body weight calculation with height in cm and output in kg
def ibw_calc(g, h): 
    if g == 'm':
        ibw = (50 + (0.91 * (h - 152.4)))
    elif g == 'f':
        ibw = 45.5 + (0.91 * (h - 152.4))
    return round(ibw)

#Using modified Nadler equation from 1962 we calculate estimated blood volume from gender and weight in kg
#True Nadler equations below:
# Men: Blood Volume = (0.3669 × H^3) + (0.03219 × W) + 0.6041
# Women: Blood Volume = (0.3561 × H^3) + (0.03308 × W) +0.1833
def ebv_calc(g, w): 
    if g == 'm':
        ebv = w * 75
        
    elif g == 'f':
        ebv = w * 65
    return round(ebv)

#Allowable blood loss based on initial hematocrit and modified nadler estimated blood volume
def abl_calc(ebv, h0, hf):
    hgb0 = h0 / 3
    abl = ebv * (h0 - hf) / h0
    return round(abl), round (hgb0)     

#Calculate mean arterial blood pressure from given systolic and diastolic pressures
def map_calc(sbp, dbp):
    map = ((2 * dbp) + sbp) / 3
    return round(map)

#Calculate cardiac output using cvp and svr with a given map
def co_calc(map, cvp, svr):
    co = ((map - cvp) / svr) * 80
    return round(co, 2)

#Fick equation for cardiac output assuming VO2 = 125 * Body surface area (110 if age > 70 years), Arterial oxygen saturation from abg, venous oxygen saturation from mixed venous, and hgb. 
def co_fick_calc(age, bsa, SaO2, SvO2, hgb):
    if age > 70:
        co_fick = (110 * bsa) / (((SaO2 / 100) - (SvO2 / 100)) * hgb * 1.34 * 10)
    else:
        co_fick = (125 * bsa) / (((SaO2 / 100) - (SvO2 / 100)) * hgb * 1.34 * 10)
    return round(co_fick, 2)

#Systemic Vascular resistance calculation based on map, cvp, co
def svr_calc(map, cvp, co):
    svr = ((map - cvp) / co) * 80
    return round(svr)

#Cardiac index calculation
def ci_calc(co, bsa):
    ci = co / bsa
    return round(ci, 2)

#Stroke Volume calculation based on co and hr
def sv_calc(co, hr):
    sv = (co / hr) * 1000 
    return round(sv) 

#Stroke Volume index calculation
def svri_calc(svr, bsa):
    svri = svr / bsa
    return round(svri)