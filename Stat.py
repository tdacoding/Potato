import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_and_soil.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))
var = db['Intraday_mean'].loc[(db.index.month == 6)]
print(var.mean())
var.hist(bins='auto', density=1, alpha=0.8, color='g',edgecolor="b")
var = db['Intraday_mean'].loc[(db.index.month == 7)]
print(var.mean())
var.hist(bins='auto', density=1, alpha=0.8, color='r',edgecolor="b")
var = db['Intraday_mean'].loc[(db.index.month == 8)]
print(var.mean())
var.hist(bins='auto', density=1, alpha=0.8, color='y',edgecolor="b")

#var.plot()
plt.show()
# # Plot the histogram.
#plt.hist(var, bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")
#
# # Plot the PDF.
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = stats.norm.pdf(x, mu, std)
# plt.plot(x, p, 'k', linewidth=2)
#title = r"Variance: n = %.0f,  m = %.0f, k = %.0f" % (1000, 1000, 1000)
#plt.text(0.11,35,r'$\mathrm{S}^2_U=\overline{U^2}-{\overline{U}}^2$', fontsize=20)
#plt.text(0.11,30,r'$\sqrt{\frac{n\mathrm{S}^2_U}{\sum_{j=1}^n\eta_j^2g(\mu_j)^2}}$', fontsize=20)
# plt.text(0.025,22,r'Shapiro: p='+str(shapiro_results[1]))
#plt.title(title)
