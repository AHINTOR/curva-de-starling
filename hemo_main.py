import patient_equations as eq
import matplotlib.pyplot as plt 

#Variables for equations
age = 75
sbp = 92
dbp = 58
bsa = 1.7
SaO2 = 100
SvO2 = 65
hgb = 8.5
ef = 55
hr = 80 

co = (eq.co_fick_calc(age, bsa, SaO2, SvO2, hgb))
lvedp = ((0.54 * eq.map_calc(sbp, dbp)) * (ef / 100)) - 2.23
sv = eq.sv_calc(co, hr)


def main():
    x = [0, 8, 10, 15, 20, 25, 25.2, 30, 35] #normal starling curve estimated by comparing multiple graphs found in textbooks
    y = [0, 50, 60, 80, 90, 91, 90, 88, 84]

    plt.plot(x, y)
    plt.scatter(lvedp, sv, color ="red") #emphasis patient point
    plt.xlabel("LVEDP via equation")  #  X-axis label 
    plt.ylabel("Stroke Volume")  #  Y-axis label 
    plt.title("Starling Curve ")  #  title 
    plt.show()

if __name__== "__main__":
    main()
