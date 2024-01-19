# rempolcal
## 残留分極値計算ツール
1. このツールはmatplotlib, numpy, pandasライブラリをインストールする必要があるので、
   pip3 install matplotlib, numpy, pandasとコマンドプロンプトに入力してインストール。
2. rempolcal.pyを開き、filename="100OHM.CSV"の""の中をデータファイル名に置き換える。
   データファイルの中の1列目は時間、2列目はCH1の電圧、3列目はCH2の電圧となっていなければいけない。
3. python rempolcal.pyとするとP-Eグラフがpdfファイルとして出力される。

計算方法や回路については、sawyer_tower_manual.pdfを参照すること。
