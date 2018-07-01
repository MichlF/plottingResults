import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import platform
import numpy as np

# Set paths and load experiment 1 data
# Get Dropbox path irrespective of OS
if platform.system() == "Windows":
    projectFolder = 'F:/Dropbox/Work/Data/behavioral/attention/SpatialProb/IndividualPriorityMaps/Experiment2'
else:
    projectFolder = '/Users/michlf/Dropbox/Work/Data/behavioral/attention/SpatialProb/IndividualPriorityMaps/Experiment2'
analysisFolder = projectFolder+'/figures/'
if not os.path.exists(analysisFolder):
    os.makedirs(analysisFolder)
dataFile = '/Data/finalAnalysis/SpatProbExp2_final.xlsx'
data = pd.read_excel(projectFolder+dataFile, sheet_name=0)

# Styles & color paletts
# Styles
vioLw = 3
vioSat = .25
vioCut = 0
swaCol = (1, 1, 1)
swaAlp = .5
lpColor = (.85, 0, 0)
lpMarker = 's'
lpMarkerS = 7
lpMarkerEC = (0, 0, 0)
lpMarkerEW = 1.5
lpLw = 3
lpLs = '-'
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
pTarLoc = {"lowProb": "#1f77b4", "highProbColor": "#2ca02c", "highProbShape": "#d62728"}
#palettTarLoc = {cond_tarLocation: "r" if cond_tarLocation == "lowProb" else "b" for cond_tarLocation in dataM.cond_tarLocation.unique()}
pTarLocGrad = {"Dis-0": "#1f77b4", "Dis-1": "#2ca02c", "Dis-2": "#d62728", "Dis-3": "#d62728", "Dis-4": "#d62728"}
pDisLoc = {"lowProb": "#1f77b4", "highProb": "#2ca02c", "highProbOther": "#d62728"}
pDisLocGrad = {"Dis-0": "#1f77b4", "Dis-1": "#2ca02c", "Dis-2": "#d62728", "Dis-3": "#d62728", "Dis-4": "#d62728"}

### Figure 1 ###

# Data selection: RT
dataTarLoc = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0)],
                            values='responseTime', index='subject_nr', columns='cond_tarLocation')
# dataDisLoc = pd.melt(dataDisLoc)  #if columns is a list (i.e. for e.g. 2 x 2 ANOVAs)
dataTarLoc = pd.melt(
    dataTarLoc.reset_index(),
    id_vars='subject_nr',
    var_name='cond_tarLocation',
    value_vars=['highProbColor', 'highProbShape', 'lowProb'],
    value_name='responseTime')
# Data selection: ER
dataTarLocER = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0)],
                            values='correct', index='subject_nr', columns='cond_tarLocation')
dataTarLocER = pd.melt(
    dataTarLocER.reset_index(),
    id_vars='subject_nr',
    var_name='cond_tarLocation',
    value_vars=['highProbColor', 'highProbShape', 'lowProb'],
    value_name='accuracy')
# Descriptives
means = dataTarLoc.groupby(['cond_tarLocation'])['responseTime'].mean().values
dataTarLocER.accuracy = (1-dataTarLocER.accuracy)*100  # make accuracy error rate
#mobs = dataTarLoc['cond_tarLocation'].value_counts().values
#pos = range(len(mobs))

# Plotting
fig1 = plt.figure(figsize=(3.25, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='cond_tarLocation', y='responseTime', data=dataTarLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLoc)
sns.swarmplot(x="cond_tarLocation", y="responseTime", data=dataTarLoc, color=swaCol, alpha=swaAlp)
ax1.plot(range(len(means)), [means[0], means[1], means[2]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='cond_tarLocation', y='accuracy', data=dataTarLocER, color=lpColor, markers=lpMarker, ci=68)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(3, 11, 2))
plt.ylabel('Error Rate')
sns.despine(offset=10, trim=True)
plt.show()

###  Figure 2 ###

# Data selection: RT
dataTarLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0)],
                                values='responseTime', index='subject_nr', columns='TarDistanceFromColor')
dataTarLocGrad = pd.melt(
    dataTarLocGrad.reset_index(),
    id_vars='subject_nr',
    var_name='TarDistanceFromColor',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='responseTime')
# Data selection: ER
dataTarLocGradER = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0)],
                            values='correct', index='subject_nr', columns='TarDistanceFromColor')
dataTarLocGradER = pd.melt(
    dataTarLocGradER.reset_index(),
    id_vars='subject_nr',
    var_name='TarDistanceFromColor',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='accuracy')
# Descriptives
means = dataTarLocGrad.groupby(['TarDistanceFromColor'])['responseTime'].mean().values
dataTarLocGradER.accuracy = (1-dataTarLocGradER.accuracy)*100  # make accuracy error rate

# Plotting
fig2 = plt.figure(figsize=(4.5, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='TarDistanceFromColor', y='responseTime', data=dataTarLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLocGrad)
sns.swarmplot(x="TarDistanceFromColor", y="responseTime", data=dataTarLocGrad, color=swaCol, alpha=swaAlp)
ax1.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='TarDistanceFromColor', y='accuracy', data=dataTarLocGradER, color=lpColor, markers=lpMarker, ci=68)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(3, 11, 2))
plt.ylabel('Error Rate')
sns.despine(offset=10, trim=True)
plt.show()

### Figure 3 ###

# Data selection: RT
dataDisLoc = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['probabilityCorrection_short'])
dataDisLoc = pd.melt(
    dataDisLoc.reset_index(),
    id_vars='subject_nr',
    var_name='probabilityCorrection_short',
    value_vars=['highProb', 'highProbOther', 'lowProb'],
    value_name='responseTime')
# Data selection: ER
dataDisLocER = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0)],
                            values='correct', index='subject_nr', columns='probabilityCorrection_short')
dataDisLocER = pd.melt(
    dataDisLocER.reset_index(),
    id_vars='subject_nr',
    var_name='probabilityCorrection_short',
    value_vars=['highProb', 'highProbOther', 'lowProb'],
    value_name='accuracy')
# Descriptives
means = dataDisLoc.groupby(['probabilityCorrection_short'])['responseTime'].mean().values
dataDisLocER.accuracy = (1-dataDisLocER.accuracy)*100  # make accuracy error rate

# Plotting
fig3 = plt.figure(figsize=(3.25, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='probabilityCorrection_short', y='responseTime', data=dataDisLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLoc)
sns.swarmplot(x="probabilityCorrection_short", y="responseTime", data=dataDisLoc, color=swaCol, alpha=swaAlp)
ax1.plot(range(len(means)), [means[0], means[1], means[2]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='probabilityCorrection_short', y='accuracy', data=dataDisLocER, color=lpColor, markers=lpMarker, ci=68)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(4, 10, 2))
plt.ylabel('Error Rate')
sns.despine(offset=10, trim=True)
plt.show()

### Figure 4 ###

# Data selection: RT
dataDisLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['DisDistance'])
dataDisLocGrad = pd.melt(
    dataDisLocGrad.reset_index(),
    id_vars='subject_nr',
    var_name='DisDistance',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='responseTime')
# Data selection: ER
dataDisLocGradER = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data.RTquicker200 == 0)],
                            values='correct', index='subject_nr', columns='DisDistance')
dataDisLocGradER = pd.melt(
    dataDisLocGradER.reset_index(),
    id_vars='subject_nr',
    var_name='DisDistance',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='accuracy')
# Descriptives
means = dataDisLocGrad.groupby(['DisDistance'])['responseTime'].mean().values
dataDisLocGradER.accuracy = (1-dataDisLocGradER.accuracy)*100  # make accuracy error rate

# Plotting
fig4 = plt.figure(figsize=(4.5, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='DisDistance', y='responseTime', data=dataDisLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLocGrad)
sns.swarmplot(x="DisDistance", y="responseTime", data=dataDisLocGrad, color=swaCol, alpha=swaAlp)
ax1.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='DisDistance', y='accuracy', data=dataDisLocGradER, color=lpColor, markers=lpMarker, ci=68)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(4, 10, 2))
plt.ylabel('Error Rate')
sns.despine(offset=10, trim=True)
plt.show()

# Save

fig1.savefig(analysisFolder+'figure1.svg', bbox_inches='tight')
fig2.savefig(analysisFolder+'figure2.svg', bbox_inches='tight')
fig3.savefig(analysisFolder+'figure3.svg', bbox_inches='tight')
fig4.savefig(analysisFolder+'figure4.svg', bbox_inches='tight')
