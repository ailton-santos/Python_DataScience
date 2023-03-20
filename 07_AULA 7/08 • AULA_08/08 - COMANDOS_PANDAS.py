import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2.csv")

air_quality.head()

print(air_quality)

air_quality.plot()

plt.show()




# import module
import pandas as pd
import numpy as np
  
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                            
                          'Age': [30, 35, 37, 33, 34, 30],
                            
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                            
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
  
# filter dataframe                                   
filtered_values = np.where((dataFrame['Salary']>=100000) &
(dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
display(dataFrame.loc[filtered_values])