OpenCV等でカメラ画像を取得して処理する
・トーンカーブでコントラスト変更
コントラストの変更にはガンマ補正を用いた。コード中のvの値が0の時、計算が行えずエラーが生じるため、vの値を0.01に変更する処理を加えている。トラックバーを操作することにより、ガンマ値を0.01〜1.00まで変更することが可能。
参考にしたURL http://gori-naru.blogspot.com/2012/11/blog-post_21.html
このURLでガンマ補正の式を参考にした。具体的には以下の部分。
uchar lut[256];
    double gm = 1.0 / gamma;
    for (int i = 0; i < 256; i++)
        lut[i] = pow(1.0*i/255, gm) * 255;

・カラー（色調）を変更
red、green、blueの三つのトラックバーがそれぞれ赤、緑、青の色に対応しており、トラックバーを動かすことでR、G、Bの値を変更することができる。
全てのトラックバーの値を100にすると元々の画像を表示し、全て0にすると画像が黒になる。

・フィルタリング
グラディエントフィルタを用いて画像のフィルタリングを行なった。トラックバーの値は、実際の値を10分の1倍した、0〜1の範囲の値が入る。
参考にしたURL https://qiita.com/hitomatagi/items/93e01ef22e46b14a60a9
このURLでグラディエントフィルタの式を参考にした。具体的には以下の部分。
kernel_gradient_3x3 = np.array([
                            [ 1,  1,  1],
                            [ 0,  0,  0],
                            [-1, -1, -1]
                            ], np.float32)
img_gradient_3x3 = cv2.filter2D(img_gray, -1, kernel_gradient_3x3)
cv2.imwrite(FILE_GRADIENT_3x3, img_gradient_3x3)
