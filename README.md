# rempolcal
## 残留分極値計算ツール
1. このツールはmatplotlib, numpy, pandas, scipyライブラリをインストールする必要があるので、
   pip3 install matplotlib, numpy, pandasとコマンドプロンプトに入力してインストール。
2. rempolcal.pyを開き、filename="filename.csv"の""の中をデータファイル名に置き換える。
   データファイルの中の1列目は時間、2列目はCH1の電圧、3列目はCH2の電圧となっていなければいけない。
3. python rempolcal.pyとするとP-Eグラフがpdfファイルとして出力される。
4. makecsv = Trueとすると、電界に対する分極値がcsvファイルとして出力される。

currcal.pyによりI-E曲線の導出が可能である。こちらもpython currcal.pyで実行できる。

計算方法や回路については、sawyer_tower_manual.pdfを参照すること。
