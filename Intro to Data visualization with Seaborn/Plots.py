# making scatter plot with lists.......................................................

# Import Matplotlib and Seaborn using the standard naming convention.

import matplotlib.pyplot as plt 
import seaborn as sns

# Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x= gdp, y= phones )

# Show plot
plt.show()

# Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()
