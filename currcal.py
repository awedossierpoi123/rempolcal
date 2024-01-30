from matplotlib import pyplot as plt
from pandas import read_csv, DataFrame
import numpy as np
from scipy.signal import savgol_filter

#データファイル名
filename = "filename.csv"

#グラフだけでなく、CSVファイルとして分極値を出力したいときは、
#ここをTrueにすること
makecsv = True

#分極電流がノイズなどでよく見えない場合、
#この数字を大きくすること。
#3より大きい奇数でなければならない。
window_length = 1001

#線の幅を太くしたい場合、
#この数字を大きくすること。
linewidth=0.05

#レファレンスキャパシタの静電容量 F
C = 100 * 1e-9

#サンプルの膜厚 nm
d = 300

#サンプルの電極半径 mm
r = 0.5

#真空の誘電率
epsilon_0 = 8.85e-12

#電気素量
e = 1.60e-19

#サンプルの電極の面積 m^2
S = np.power(r*0.1/100,2)*np.pi

df = read_csv(filename, delimiter=",", header=0)

t = df.iloc[:,0].to_numpy()
x = df.iloc[:,1].to_numpy()
y = df.iloc[:,2].to_numpy()

delta_t = np.average(np.abs(np.diff(t)))

#サンプルの電荷
Q = C * y

#V/m
E = (x-y) / (d*1e-9)

E_MV_cm = E * 1e-6/1e2

#DS=Q D=Q/S
D = Q / S

#P=D-eE C/m^2
P = D - epsilon_0*E

#convert to micro C/cm^2
P_microC_cm2 = P * 1e6/1e4

font_label_size=18
font_tick_size=13

plt.xlabel("E [MV/cm]", fontsize=font_label_size)
plt.ylabel("A [$A/cm^{2}$]", fontsize=font_label_size)
plt.tick_params(labelsize=font_tick_size)

I_A_cm2 = np.gradient(P_microC_cm2*10**(-6), delta_t)
I_A_cm2_smoothed = savgol_filter(I_A_cm2, window_length=window_length, polyorder=2)

plt.plot(E_MV_cm, I_A_cm2_smoothed, linewidth=linewidth)

plt.vlines(x=0, ymin=plt.ylim()[0], ymax=plt.ylim()[1], linestyles="dashed", colors="black")
plt.hlines(y=0, xmin=plt.xlim()[0], xmax=plt.xlim()[1], linestyles="dashed", colors="black")
plt.tight_layout()
plt.savefig("{0}.pdf".format(filename))
plt.show()

if makecsv:
    df = DataFrame(
        {'E [MV/cm]': E_MV_cm, 
         'P [microC/cm2]' : P_microC_cm2,
         'I [A/cm2]' : I_A_cm2,
         'I_smoothed [A/cm2]' : I_A_cm2_smoothed
         })
    df.to_csv("{0}.csv".format(filename), index=False)