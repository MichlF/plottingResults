import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import platform
import numpy as np

# Set paths and load experiment 1 data
# Get Dropbox path irrespective of OS
if platform.system() == "Windows":
    projectFolder = 'F:/Dropbox/Work/Data/behavioral/attention/SpatialProb/IndividualPriorityMaps/Experiment4'
else:
    projectFolder = '/Users/michlf/Dropbox/Work/Data/behavioral/attention/SpatialProb/IndividualPriorityMaps/Experiment4'
analysisFolder = projectFolder+'/figures/'
if not os.path.exists(analysisFolder):
    os.makedirs(analysisFolder)
dataFile = '/Data/finalAnalysis/SpatProbExp1_final.xlsx'
data = pd.read_excel(projectFolder+dataFile, sheet_name=0)

# Styles & color paletts

# Styles
vioLw = 3
vioSat = .25
vioCut = 0
swaCol = (1, 1, 1)
swaAlp = .5
# Color palletts
# Standard matplotlib colors
#1f77b4 blue
#ff7f0e orange
#2ca02c green
#d62728 red
#9467bd purple
#8c564b brown
#e377c2 pink
#7f7f7f dark gray
#bcbd22 dirty yellow
#17becf cyan
pTarLoc = {"lowProb": "#1f77b4", "highProbColor1": "#2ca02c", "highProbColor2": "#d62728"}
#palettTarLoc = {cond_tarLocation: "r" if cond_tarLocation == "lowProb" else "b" for cond_tarLocation in dataM.cond_tarLocation.unique()}
pTarLocGrad = {"Dis-0": "#1f77b4", "Dis-1": "#2ca02c", "Dis-2": "#d62728", "Dis-3": "#d62728", "Dis-4": "#d62728"}
pDisLoc = {"lowProb": "#1f77b4", "highProb": "#2ca02c", "highProbOther": "#d62728"}
pDisLocGrad = {"Dis-0": "#1f77b4", "Dis-1": "#2ca02c", "Dis-2": "#d62728", "Dis-3": "#d62728", "Dis-4": "#d62728"}

### Figure 1

# Data selection
dataTarLoc = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0) & (data.correct == 1)],
                            values='responseTime', index='subject_nr', columns='cond_tarLocation')
# dataDisLoc = pd.melt(dataDisLoc)  #if columns is a list (i.e. for e.g. 2 x 2 ANOVAs)
dataTarLoc = pd.melt(
    dataTarLoc.reset_index(),
    id_vars='subject_nr',
    var_name='cond_tarLocation',
    value_vars=['highProbColor1', 'highProbColor2', 'lowProb'],
    value_name='responseTime')

# Descriptives
means = dataTarLoc.groupby(['cond_tarLocation'])['responseTime'].mean().values
#mobs = dataTarLoc['cond_tarLocation'].value_counts().values
#pos = range(len(mobs))

# Plotting
#fig1, (ax) = plt.subplots(1, 1, figsize=(4, 6), dpi=100)
fig1 = plt.figure()

ax1 = plt.subplot2grid((4,3), (1,0), rowspan=3, colspan=3)
sns.violinplot(x='cond_tarLocation', y='responseTime', data=dataTarLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLoc)
sns.swarmplot(x="cond_tarLocation", y="responseTime", data=dataTarLoc, color=swaCol, alpha=swaAlp)
ax1.plot([0, 1, 2], [means[0], means[1], means[2]], color=(.85, 0, 0), marker='s', markersize=7,
        markeredgecolor=(0, 0, 0), markeredgewidth=1.5, linewidth=3, linestyle='dashed', dashes=(0.75, 0.75))
ax1.set_xlabel("Target Location")
ax1.set_ylabel("Response Time [ms]")
#ax2 = plt.axes([0, 0, 1, 0.1])
#ax2 = sns.violinplot(x='cond_tarLocation', y='responseTime', data=dataTarLoc, cut=0, saturation=.2, palette=pTarLoc)
# Each condition in violin plot corresponds to 1 px, so use floats because scaling is all messed up.
#for tick, label in zip(pos, ax.get_xticklabels()):
    #ax.plot([pos[tick]-0.1, pos[tick]+0.1], [means[tick], means[tick]], color='red', alpha=.75, linewidth=3)  #linestyle='dashed', dashes=(0.75, 0.75))
ax2 = plt.subplot2grid((4,3), (3,0), colspan=3)
values = np.cumsum(np.random.randn(1000, 1))
#plt.plot(values)
sns.violinplot(x='cond_tarLocation', y='responseTime', data=dataTarLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLoc)
ax2.yaxis.set_label_position("right")
h = plt.ylabel('Error Rate')
h.set_rotation(270)
sns.despine(offset=10, trim=True)
plt.show()

### Figure 2
dataTarLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns='TarDistanceFromColor1')
dataTarLocGrad = pd.melt(
    dataTarLocGrad.reset_index(),
    id_vars='subject_nr',
    var_name='TarDistanceFromColor1',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='responseTime')

# Descriptives
means = dataTarLocGrad.groupby(['TarDistanceFromColor1'])['responseTime'].mean().values

# Plotting
fig2, (ax) = plt.subplots(1, 1, figsize=(6, 6), dpi=100)
sns.violinplot(x='TarDistanceFromColor1', y='responseTime', data=dataTarLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLocGrad)
sns.swarmplot(x="TarDistanceFromColor1", y="responseTime", data=dataTarLocGrad, color=swaCol, alpha=swaAlp)
ax.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=(.85, 0, 0), marker='s', markersize=7,
        markeredgecolor=(0, 0, 0), markeredgewidth=1.5, linewidth=3, linestyle='dashed', dashes=(0.75, 0.75))
sns.despine(offset=10, trim=True)
plt.show()

### Figure 3
dataDisLoc = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['cond_disLocation'])
dataDisLoc = pd.melt(
    dataDisLoc.reset_index(),
    id_vars='subject_nr',
    var_name='cond_disLocation',
    value_vars=['highProb', 'highProbOther', 'lowProb'],
    value_name='responseTime')
# Descriptives
means = dataDisLoc.groupby(['cond_disLocation'])['responseTime'].mean().values
# Plotting
fig3, (ax) = plt.subplots(1, 1, figsize=(4, 6), dpi=100)
sns.violinplot(x='cond_disLocation', y='responseTime', data=dataDisLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLoc)
sns.swarmplot(x="cond_disLocation", y="responseTime", data=dataDisLoc, color=swaCol, alpha=swaAlp)
ax.plot(range(len(means)), [means[0], means[1], means[2]], color=(.85, 0, 0), marker='s', markersize=7,
        markeredgecolor=(0, 0, 0), markeredgewidth=1.5, linewidth=3, linestyle='dashed', dashes=(0.75, 0.75))
sns.despine(offset=10, trim=True)
plt.show()

### Figure 4
dataDisLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['DisDistance'])
dataDisLocGrad = pd.melt(
    dataDisLocGrad.reset_index(),
    id_vars='subject_nr',
    var_name='DisDistance',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='responseTime')
# Descriptives
means = dataDisLocGrad.groupby(['DisDistance'])['responseTime'].mean().values

# Plotting
fig4, (ax) = plt.subplots(1, 1, figsize=(6, 6), dpi=100)
sns.violinplot(x='DisDistance', y='responseTime', data=dataDisLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLocGrad)
sns.swarmplot(x="DisDistance", y="responseTime", data=dataDisLocGrad, color=swaCol, alpha=swaAlp)
ax.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=(.85, 0, 0), marker='s', markersize=7,
        markeredgecolor=(0, 0, 0), markeredgewidth=1.5, linewidth=3, linestyle='dashed', dashes=(0.75, 0.75))
sns.despine(offset=10, trim=True)
plt.show()

# Save
fig1.savefig(analysisFolder+'figure1.svg', bbox_inches='tight')
fig2.savefig(analysisFolder+'figure2.svg', bbox_inches='tight')
fig3.savefig(analysisFolder+'figure3.svg', bbox_inches='tight')
fig4.savefig(analysisFolder+'figure4.svg', bbox_inches='tight')
