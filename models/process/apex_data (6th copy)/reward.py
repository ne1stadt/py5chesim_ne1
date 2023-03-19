# open a file and read the data, only keep the rows that has 'eMBB-0' in the second column

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator

string = "['Video', 0.0, 0.0, 0.7, 339]['URLLC', 0.0, 0.0, 1.0, 497]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.0, 0.0, 1.0, 514]['URLLC', 0.0, 0.0, 1.0, 832]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.0, 0.0, 1.0, 576]['URLLC', 0.0, 0.0, 1.0, 780]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.2, 0.2, 1.0, 460]['URLLC', 0.2, 0.2, 1.0, 777]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 327]['URLLC', 1.0, 1.0, 1.0, 743]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.9, 1.0, 0.9, 19]['URLLC', 1.0, 1.0, 1.0, 497]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.6, 1.0, 0.6, 11]['URLLC', 0.9, 1.0, 0.9, 269]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.6, 1.0, 0.6, 13]['URLLC', 0.7, 1.0, 0.7, 14]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.7, 1.0, 0.7, 10]['URLLC', 0.5, 1.0, 0.5, 15]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 8]['URLLC', 0.6, 1.0, 0.6, 19]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 129]['URLLC', 0.7, 1.0, 0.7, 14]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.18000000000000002, 0.2, 0.9, 22]['URLLC', 0.7, 1.0, 0.7, 12]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 10]['URLLC', 0.8, 1.0, 0.8, 32]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 110]['URLLC', 1.0, 1.0, 1.0, 53]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.18000000000000002, 0.2, 0.9, 8]['URLLC', 0.8, 1.0, 0.8, 47]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 7]['URLLC', 1.0, 1.0, 1.0, 70]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 125]['URLLC', 0.8, 1.0, 0.8, 89]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.18000000000000002, 0.2, 0.9, 14]['URLLC', 0.7, 1.0, 0.7, 15]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 8]['URLLC', 0.7, 1.0, 0.7, 11]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 104]['URLLC', 0.8, 1.0, 0.8, 37]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.16000000000000003, 0.2, 0.8, 11]['URLLC', 1.0, 1.0, 1.0, 79]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 10]['URLLC', 0.8, 1.0, 0.8, 103]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 124]['URLLC', 0.7, 1.0, 0.7, 16]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.18000000000000002, 0.2, 0.9, 25]['URLLC', 0.7, 1.0, 0.7, 17]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 14]['URLLC', 0.8, 1.0, 0.8, 32]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.8, 1.0, 0.8, 129]['URLLC', 1.0, 1.0, 1.0, 52]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.2, 0.2, 1.0, 103]['URLLC', 0.8, 1.0, 0.8, 55]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.6, 1.0, 0.6, 65]['URLLC', 0.7, 1.0, 0.7, 17]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.5, 1.0, 0.5, 8]['URLLC', 0.7, 1.0, 0.7, 11]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.5, 1.0, 0.5, 7]['URLLC', 0.8, 1.0, 0.8, 50]['VoLTE', 1, 0.0, 1.0, 0]['Video', 0.6, 1.0, 0.6, 13]['URLLC', 0.7, 1.0, 0.7, 12]['VoLTE', 0, 0.0, 1.0, 471]['Video', 0.6, 1.0, 0.6, 11]['URLLC', 0.7, 1.0, 0.7, 16]['VoLTE', 0.0, 0.0, 1.0, 495]['Video', 0.7, 1.0, 0.7, 13]['URLLC', 0.8, 1.0, 0.8, 44]['VoLTE', 0.0, 0.0, 1.0, 469]['Video', 0.8, 1.0, 0.8, 12]['URLLC', 1.0, 1.0, 1.0, 63]['VoLTE', 0.2, 0.2, 1.0, 495]['Video', 0.8, 1.0, 0.8, 112]['URLLC', 0.8, 1.0, 0.8, 105]['VoLTE', 0.0, 0.0, 1.0, 466]['Video', 0.18000000000000002, 0.2, 0.9, 15]['URLLC', 0.7, 1.0, 0.7, 14]['VoLTE', 0.2, 0.2, 1.0, 496]['Video', 0.8, 1.0, 0.8, 15]['URLLC', 0.7, 1.0, 0.7, 14]['VoLTE', 0.0, 0.0, 1.0, 463]['Video', 0.8, 1.0, 0.8, 127]['URLLC', 0.8, 1.0, 0.8, 46]['VoLTE', 0.2, 0.2, 1.0, 403]['Video', 0.18000000000000002, 0.2, 0.9, 11]['URLLC', 1.0, 1.0, 1.0, 68]['VoLTE', 0.2, 0.2, 1.0, 384]['Video', 0.8, 1.0, 0.8, 8]['URLLC', 0.8, 1.0, 0.8, 81]['VoLTE', 1.0, 1.0, 1.0, 384]['Video', 0.9, 1.0, 0.9, 144]['URLLC', 0.7, 1.0, 0.7, 13]['VoLTE', 1.0, 1.0, 1.0, 280]['Video', 0.18000000000000002, 0.2, 0.9, 25]['URLLC', 0.7, 1.0, 0.7, 14]['VoLTE', 1.0, 1.0, 1.0, 173]['Video', 0.8, 1.0, 0.8, 8]['URLLC', 0.8, 1.0, 0.8, 57]['VoLTE', 0.9, 1.0, 0.9, 51]['Video', 0.8, 1.0, 0.8, 138]['URLLC', 0.7, 1.0, 0.7, 15]['VoLTE', 0.8, 1.0, 0.8, 11]['Video', 0.18000000000000002, 0.2, 0.9, 30]['URLLC', 0.7, 1.0, 0.7, 15]['VoLTE', 0.8, 1.0, 0.8, 12]['Video', 0.8, 1.0, 0.8, 156]['URLLC', 0.8, 1.0, 0.8, 21]['VoLTE', 0.8, 1.0, 0.8, 10]['Video', 0.18000000000000002, 0.2, 0.9, 35]['URLLC', 0.9, 1.0, 0.9, 27]['VoLTE', 0.8, 1.0, 0.8, 13]['Video', 0.8, 1.0, 0.8, 133]['URLLC', 1.0, 1.0, 1.0, 35]['VoLTE', 0.9, 1.0, 0.9, 43]['Video', 0.18000000000000002, 0.2, 0.9, 25]['URLLC', 0.9, 1.0, 0.9, 294]['VoLTE', 1.0, 1.0, 1.0, 40]['Video', 0.8, 1.0, 0.8, 14]['URLLC', 0.2, 0.2, 1.0, 302]['VoLTE', 1.0, 1.0, 1.0, 59]['Video', 0.8, 1.0, 0.8, 133]['URLLC', 0.8, 1.0, 0.8, 319]['VoLTE', 0.9, 1.0, 0.9, 81]['Video', 0.18000000000000002, 0.2, 0.9, 24]['URLLC', 0.9, 1.0, 0.9, 92]['VoLTE', 0.9, 1.0, 0.9, 10]['Video', 0.8, 1.0, 0.8, 12]['URLLC', 0.6, 1.0, 0.6, 14]['VoLTE', 0.9, 1.0, 0.9, 13]['Video', 0.8, 1.0, 0.8, 103]['URLLC', 0.6, 1.0, 0.6, 16]['VoLTE', 0.9, 1.0, 0.9, 32]['Video', 0.18000000000000002, 0.2, 0.9, 11]['URLLC', 0.6, 1.0, 0.6, 8]['VoLTE', 1.0, 1.0, 1.0, 80]['Video', 0.8, 1.0, 0.8, 11]['URLLC', 0.7, 1.0, 0.7, 11]['VoLTE', 1.0, 1.0, 1.0, 14]['Video', 0.8, 1.0, 0.8, 123]['URLLC', 0.8, 1.0, 0.8, 35]['VoLTE', 0.9, 1.0, 0.9, 25]['Video', 0.18000000000000002, 0.2, 0.9, 13]['URLLC', 1.0, 1.0, 1.0, 62]['VoLTE', 1.0, 1.0, 1.0, 49]['Video', 0.8, 1.0, 0.8, 10]['URLLC', 0.8, 1.0, 0.8, 78]['VoLTE', 1.0, 1.0, 1.0, 14]['Video', 0.8, 1.0, 0.8, 130]['URLLC', 0.7, 1.0, 0.7, 12]['VoLTE', 0.9, 1.0, 0.9, 18]['Video', 0.18000000000000002, 0.2, 0.9, 16]['URLLC', 0.7, 1.0, 0.7, 17]['VoLTE', 1.0, 1.0, 1.0, 41]['Video', 0.8, 1.0, 0.8, 15]['URLLC', 0.8, 1.0, 0.8, 37]['VoLTE', 1.0, 1.0, 1.0, 54]['Video', 0.8, 1.0, 0.8, 136]['URLLC', 1.0, 1.0, 1.0, 56]['VoLTE', 1.0, 1.0, 1.0, 72]['Video', 0.18000000000000002, 0.2, 0.9, 39]['URLLC', 0.8, 1.0, 0.8, 93]['VoLTE', 0.9, 1.0, 0.9, 14]['Video', 0.8, 1.0, 0.8, 171]['URLLC', 0.8, 1.0, 0.8, 14]['VoLTE', 0.8, 1.0, 0.8, 11]['Video', 0.18000000000000002, 0.2, 0.9, 54]['URLLC', 0.7, 1.0, 0.7, 24]['VoLTE', 0.9, 1.0, 0.9, 42]['Video', 0.8, 1.0, 0.8, 173]['URLLC', 0.8, 1.0, 0.8, 43]['VoLTE', 1.0, 1.0, 1.0, 51]['Video', 0.18000000000000002, 0.2, 0.9, 53]['URLLC', 1.0, 1.0, 1.0, 47]['VoLTE', 1.0, 1.0, 1.0, 12]['Video', 0.8, 1.0, 0.8, 162]['URLLC', 0.8, 1.0, 0.8, 289]['VoLTE', 0.9, 1.0, 0.9, 26]['Video', 0.18000000000000002, 0.2, 0.9, 37]['URLLC', 0.2, 0.2, 1.0, 315]['VoLTE', 1.0, 1.0, 1.0, 55]['Video', 0.8, 1.0, 0.8, 127]['URLLC', 0.8, 1.0, 0.8, 339]['VoLTE', 0.9, 1.0, 0.9, 13]['Video', 0.18000000000000002, 0.2, 0.9, 11]['URLLC', 0.9, 1.0, 0.9, 98]['VoLTE', 0.9, 1.0, 0.9, 29]['Video', 0.8, 1.0, 0.8, 12]['URLLC', 0.6, 1.0, 0.6, 14]['VoLTE', 1.0, 1.0, 1.0, 60]['Video', 0.8, 1.0, 0.8, 142]['URLLC', 0.6, 1.0, 0.6, 15]['VoLTE', 1.0, 1.0, 1.0, 16]['Video', 0.18000000000000002, 0.2, 0.9, 41]['URLLC', 0, 1.0, 0.6, 0]['VoLTE', 0.9, 1.0, 0.9, 36]['Video', 0.8, 1.0, 0.8, 163]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 53]['Video', 0.18000000000000002, 0.2, 0.9, 46]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 12]['Video', 0.8, 1.0, 0.8, 180]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 36]['Video', 0.18000000000000002, 0.2, 0.9, 38]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 56]['Video', 0.8, 1.0, 0.8, 149]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 16]['Video', 0.18000000000000002, 0.2, 0.9, 33]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 35]['Video', 0.8, 1.0, 0.8, 168]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 52]['Video', 0.18000000000000002, 0.2, 0.9, 35]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 12]['Video', 0.8, 1.0, 0.8, 146]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 18]['Video', 0.18000000000000002, 0.2, 0.9, 32]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 42]['Video', 0.8, 1.0, 0.8, 165]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 69]['Video', 0.18000000000000002, 0.2, 0.9, 38]['URLLC', 0, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 67]['Video', 0.8, 1.0, 0.8, 170]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 12]['Video', 0.2, 0.2, 1.0, 74]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 0.8, 1.0, 0.8, 11]['Video', 0.7, 1.0, 0.7, 13]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 27]['Video', 0.6, 1.0, 0.6, 11]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 42]['Video', 0.7, 1.0, 0.7, 10]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 52]['Video', 0.8, 1.0, 0.8, 14]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 72]['Video', 0.8, 1.0, 0.8, 128]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 1.0, 1.0, 1.0, 15]['Video', 0.18000000000000002, 0.2, 0.9, 11]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 0.8, 1.0, 0.8, 10]['Video', 0.8, 1.0, 0.8, 13]['URLLC', 1, 0.0, 1.0, 0]['VoLTE', 0.9, 1.0, 0.9, 46]"


sublists = eval("[" + string.replace("][", "], [") + "]")


rewardvideo = []
rewardurllc = []
rewardtel = []

for row in sublists:
    if row[0] == 'Video':
        rewardvideo.append(row[1])
    elif row[0] == 'URLLC':
        rewardurllc.append(row[1])
    elif row[0] == 'VoLTE':
        rewardtel.append(row[1])
print('len2, ', len(rewardtel))

x=[]
for i in range(60, 6000, 60):
     x.append(i)

rewardvideo = rewardvideo[:80]
rewardurllc = rewardurllc[:80]
rewardtel = rewardtel[:80]
x = x[:80]


# plots y_pcktstel, y_pcktsvolte, y_pcktsvideo vs x, put labels, legend, etc and make it look nice and smooth the graph
lineWidth = 0.5


plt.plot(x, rewardurllc, label = "eMBB-0", linewidth=lineWidth)
plt.plot(x, rewardvideo, label = "eMBB-1", linewidth=lineWidth)
plt.plot(x, rewardtel, label = "eMBB-2", linewidth=lineWidth)
plt.xlabel('Tiempo (ms)')
plt.ylabel('Reward')

ax = plt.gca()

plt.autoscale()
ax.xaxis.set_major_locator(MultipleLocator(500))

lettersize = 12

plt.legend( prop={"size": lettersize}, fancybox=True)

sns.despine()
#plt.legend(loc='center right')
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
ax.grid(which="major", color="#CCCCCC", linestyle="--")

# increase axis label font size
ax.xaxis.label.set_size(lettersize)
ax.yaxis.label.set_size(lettersize)

# increase tick label font size
ax.tick_params(axis='both', which='major', labelsize=10)


plt.savefig(
        'reward' + ".svg"
    )

plt.savefig(
        'reward' + ".pdf"
    )
plt.show()







































