# CNN_Exercise
```
20180504
今天花了點時間摸了一下CNN(convolution neural network)，主要針對CNN的設計方式進行相關research 
比較對象為mnist_exercise.py與neural_art.py，之前在碩班課餘時間有針對neural art進行實做，當然之後很久沒碰了
，直到最近在接觸才發現，自己對於CNN的基礎知識還嫌薄弱，對於如何設計CNN十分困惑，因此動起想研究CNN的念頭
首先
mnist_exercise.py這支code,是針對mnist資料集進行分類預測的程式，是一個經典範例
neural_art.py這支code,是將畫風移轉到一張圖的程式
詳細內容，可參考https://github.com/anishathalye/neural-style

透過今天練習還有一推閱讀，還有比較這兩支code之後，大概可以發現一些概念
1.建立relu的方式都一樣都是Wn+B ; W is weight, B is Bias
2.CNN建立目的在於找出當前最好的W還有B
3.CNN 是基本CNN的深度延伸
3.每一層都是影像特徵，越往下越重要

```
