import pandas as pd
import matplotlib.pyplot as plt

# import BCCDC data
df = pd.read_excel (r'BCCDC_COVID19_Dashboard_Case_Details.xlsx')
print (df)
#view last few rows of dataset
df.tail()
groupByDate = df.groupby("Reported_Date")["Sex"].count().reset_index(name = "count")
print (groupByDate)
plt.plot(groupByDate["Reported_Date"], groupByDate["count"])
plt.xlabel("Reported Date")
plt.ylabel("Number of COVID-19 Cases")

# can hide the axis 
#frame = plt.gca()
#frame.axes.xaxis.set_ticklabels([])

plt.show()
