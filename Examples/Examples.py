import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))

# Load data
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# Do plotting
#sns.stripplot(x="day", y="total_bill", data=tips)
#plt.show()

## Boxplots
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
plt.show()
tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.boxplot(x="day", y="total_bill", hue="weekend", data=tips, dodge=False)
plt.show()

# Violinplots
sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
plt.show()
sns.violinplot(x="total_bill", y="day", hue="time", data=tips,
               bw=.1, scale="count", scale_hue=False)
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
sns.swarmplot(x="day", y="total_bill", data=tips, color="w", alpha=.5)
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
sns.stripplot(x="day", y="total_bill", data=tips, color="w", alpha=.5, jitter=True)
plt.show()
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
plt.show()
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips,
               split=True, inner="stick", palette="Set3")
plt.show()

print(tips, np.shape(tips), type(tips))
