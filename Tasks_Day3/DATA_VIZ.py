# import libararies fist 
import seaborn as sns
import matplotlib.pyplot as plt

# Set theme of plot 
sns.set_theme(style="ticks",color_codes=True)

# load data set from dataset 
kashti=sns.load_dataset('titanic')

# # plot data on basic graph with one variable
# p=sns.countplot(x="sex",data=kashti)

# # plot data on basic graph with two variable
# p=sns.countplot(x="sex",data=kashti,hue="class")

# plot data on basic graph with two variable
p=sns.countplot(x="sex",data=kashti,hue="class")
p.set_title("AFTAB HUSSAIN SHAR")

# Print the plot 
plt.show()