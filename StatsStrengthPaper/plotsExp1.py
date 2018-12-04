import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import platform
import numpy as np

# Set paths and load experiment 1 data
# Get Dropbox path irrespective of OS
if platform.system() == "Windows":
    projectFolder = 'F:\Dropbox\Work\Data\Behavioral\Attention\StatisticalRegularities\Salience\Exp1'
else:
    projectFolder = '/Users/michlf/Dropbox/Work/Data/Behavioral/Attention/StatisticalRegularities/Salience/Exp1'
analysisFolder = projectFolder+'/figures/'
if not os.path.exists(analysisFolder):
    os.makedirs(analysisFolder)
dataFile = '/Beh/Analysis/AnalysisSAL1.xlsx'
data = pd.read_excel(projectFolder+dataFile, sheet_name=0)

# Styles & color paletts & other parameters
# Params
ci = 95  # for SD = sd, for SEM = 68, for 95% ci = 95
# Styles
vioLw = 3
vioSat = .5
vioCut = .25
swaCol = (.7, .7, .7)
swaColE = (0, 0, 0)
swaLwE = .5
swaAlp = 1
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
pTarLoc = {"lowProb": "#ffffff", "highProbColor1": "#ff7f0e", "highProbColor2": "#1f77b4"}
#palettTarLoc = {cond_tarLocation: "r" if cond_tarLocation == "lowProb" else "b" for cond_tarLocation in dataM.cond_tarLocation.unique()}
pTarLocGrad = {"Dis-0": "#ff7f0e", "Dis-1": "#ffc999", "Dis-2": "#ffffff", "Dis-3": "#92c7ed", "Dis-4": "#1f77b4"}
pDisLoc = {"lowProb": "#ffffff", "highProb": "#2ca02c", "highProbOther": "#d62728"}
pDisLocGrad = {"Dis-0": "#d62728", "Dis-1": "#eb9393", "Dis-2": "#ffffff", "Dis-3": "#9be49b", "Dis-4": "#2ca02c"}

### Figure 1 ###

# Data selection: RT
dataTarLoc = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data['Search RT > 200'] == 1) & (data.correct == 1)],
                            values='responseTime', index='subject_nr', columns='cond_tarLocation')
# dataDisLoc = pd.melt(dataDisLoc)  #if columns is a list (i.e. for e.g. 2 x 2 ANOVAs)
dataTarLoc = pd.melt(
    dataTarLoc.reset_index(),
    id_vars='subject_nr',
    var_name='cond_tarLocation',
    value_vars=['highProbColor1', 'highProbColor2', 'lowProb'],
    value_name='responseTime')
# Data selection: ER
dataTarLocER = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data['Search RT > 200'] == 1)],
                            values='correct', index='subject_nr', columns='cond_tarLocation')
dataTarLocER = pd.melt(
    dataTarLocER.reset_index(),
    id_vars='subject_nr',
    var_name='cond_tarLocation',
    value_vars=['highProbColor1', 'highProbColor2', 'lowProb'],
    value_name='accuracy')
# Descriptives
means = dataTarLoc.groupby(['cond_tarLocation'])['responseTime'].mean().values
dataTarLocER.accuracy = (1-dataTarLocER.accuracy)*100  # make accuracy error rate
#mobs = dataTarLoc['cond_tarLocation'].value_counts().values
#pos = range(len(mobs))

# Plotting
fig1 = plt.figure(figsize=(4.75, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='cond_tarLocation', y='responseTime', data=dataTarLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLoc)
sns.swarmplot(x="cond_tarLocation", y="responseTime", data=dataTarLoc, color=swaCol, alpha=swaAlp, linewidth=swaLwE, edgecolor=swaColE)
ax1.plot(range(len(means)), [means[0], means[1], means[2]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs, zorder=3)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [in ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='cond_tarLocation', y='accuracy', data=dataTarLocER, color=lpColor, markers=lpMarker, ci=ci)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(4, 12, 2))
plt.ylabel('Error Rate\n [in %]')
sns.despine(offset=10, trim=True)
plt.show()

###  Figure 2 ###

# # Data selection: RT
# dataTarLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0) & (data.correct == 1)],
#                                 values='responseTime', index='subject_nr', columns='TarDistanceFromColor1')
# dataTarLocGrad = pd.melt(
#     dataTarLocGrad.reset_index(),
#     id_vars='subject_nr',
#     var_name='TarDistanceFromColor1',
#     value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
#     value_name='responseTime')
# # Data selection: ER
# dataTarLocGradER = pd.pivot_table(data[(data.cond_disPresent == 'absent') & (data.RTquicker200 == 0)],
#                             values='correct', index='subject_nr', columns='TarDistanceFromColor1')
# dataTarLocGradER = pd.melt(
#     dataTarLocGradER.reset_index(),
#     id_vars='subject_nr',
#     var_name='TarDistanceFromColor1',
#     value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
#     value_name='accuracy')
# # Descriptives
# means = dataTarLocGrad.groupby(['TarDistanceFromColor1'])['responseTime'].mean().values
# dataTarLocGradER.accuracy = (1-dataTarLocGradER.accuracy)*100  # make accuracy error rate

# # Plotting
# fig2 = plt.figure(figsize=(5.75, 6), dpi=100)
# ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
# sns.violinplot(x='TarDistanceFromColor1', y='responseTime', data=dataTarLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pTarLocGrad)
# sns.swarmplot(x="TarDistanceFromColor1", y="responseTime", data=dataTarLocGrad, color=swaCol, alpha=swaAlp, linewidth=swaLwE, edgecolor=swaColE)
# ax1.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
#         markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs, zorder=3)#, dashes=(0.75, 0.75))
# ax1.set_xlabel('')
# ax1.set_ylabel("Response Time [in ms]")
# ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
# sns.pointplot(x='TarDistanceFromColor1', y='accuracy', data=dataTarLocGradER, color=lpColor, markers=lpMarker, ci=ci)
# ax2.axes.get_xaxis().set_visible(False)
# ax2.axes.get_xaxis().set_ticks([])
# ax2.yaxis.set_ticks(np.arange(4, 12, 2))
# plt.ylabel('Error Rate\n [in %]')
# sns.despine(offset=10, trim=True)
# plt.show()

### Figure 3 ###

# Data selection: RT
dataDisLoc = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data['Search RT > 200'] == 1) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['cond_disLocation'])
dataDisLoc = pd.melt(
    dataDisLoc.reset_index(),
    id_vars='subject_nr',
    var_name='cond_disLocation',
    value_vars=['highProb', 'highProbOther', 'lowProb'],
    value_name='responseTime')
# Data selection: ER
dataDisLocER = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data['Search RT > 200'] == 1)],
                            values='correct', index='subject_nr', columns='cond_disLocation')
dataDisLocER = pd.melt(
    dataDisLocER.reset_index(),
    id_vars='subject_nr',
    var_name='cond_disLocation',
    value_vars=['highProb', 'highProbOther', 'lowProb'],
    value_name='accuracy')
# Descriptives
means = dataDisLoc.groupby(['cond_disLocation'])['responseTime'].mean().values
dataDisLocER.accuracy = (1-dataDisLocER.accuracy)*100  # make accuracy error rate

# Plotting
fig3 = plt.figure(figsize=(4.75, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='cond_disLocation', y='responseTime', data=dataDisLoc, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLoc)
sns.swarmplot(x="cond_disLocation", y="responseTime", data=dataDisLoc, color=swaCol, alpha=swaAlp, linewidth=swaLwE, edgecolor=swaColE)
ax1.plot(range(len(means)), [means[0], means[1], means[2]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs, zorder=3)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [in ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='cond_disLocation', y='accuracy', data=dataDisLocER, color=lpColor, markers=lpMarker, ci=ci)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(5, 13, 2))
plt.ylabel('Error Rate\n [in %]')
sns.despine(offset=10, trim=True)
plt.show()

### Figure 4 ###

# Data selection: RT
dataDisLocGrad = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data['Search RT > 200'] == 1) & (data.correct == 1)],
                                values='responseTime', index='subject_nr', columns=['DisDistance'])
dataDisLocGrad = pd.melt(
    dataDisLocGrad.reset_index(),
    id_vars='subject_nr',
    var_name='DisDistance',
    value_vars=['Dis-0', 'Dis-1', 'Dis-2', 'Dis-3', 'Dis-4'],
    value_name='responseTime')
# Data selection: ER
dataDisLocGradER = pd.pivot_table(data[(data.cond_disPresent == 'present') & (data['Search RT > 200'] == 1)],
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
fig4 = plt.figure(figsize=(5.75, 6), dpi=100)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
sns.violinplot(x='DisDistance', y='responseTime', data=dataDisLocGrad, cut=vioCut, saturation=vioSat, linewidth=vioLw, palette=pDisLocGrad)
sns.swarmplot(x="DisDistance", y="responseTime", data=dataDisLocGrad, color=swaCol, alpha=swaAlp, linewidth=swaLwE, edgecolor=swaColE)
ax1.plot(range(len(means)), [means[0], means[1], means[2], means[3], means[4]], color=lpColor, marker=lpMarker, markersize=lpMarkerS,
        markeredgecolor=lpMarkerEC, markeredgewidth=lpMarkerEW, lw=lpLw, ls=lpLs, zorder=3)#, dashes=(0.75, 0.75))
ax1.set_xlabel('')
ax1.set_ylabel("Response Time [in ms]")
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
sns.pointplot(x='DisDistance', y='accuracy', data=dataDisLocGradER, color=lpColor, markers=lpMarker, ci=ci)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_ticks([])
ax2.yaxis.set_ticks(np.arange(5, 13, 2))
plt.ylabel('Error Rate\n [in %]')
sns.despine(offset=10, trim=True)
plt.show()

### Save ###

fig1.savefig(analysisFolder+'figure1.svg', bbox_inches='tight')
#fig2.savefig(analysisFolder+'figure2.svg', bbox_inches='tight')
fig3.savefig(analysisFolder+'figure3.svg', bbox_inches='tight')
fig4.savefig(analysisFolder+'figure4.svg', bbox_inches='tight')
