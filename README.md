参考にしたURL http://gori-naru.blogspot.com/2012/11/blog-post_21.html
このURLでガンマ補正の式を参考にした。具体的には以下の部分。
uchar lut[256];
    double gm = 1.0 / gamma;
    for (int i = 0; i < 256; i++)
        lut[i] = pow(1.0*i/255, gm) * 255;
