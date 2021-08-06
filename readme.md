# Python 简易验证码识别

## 依赖库
- tesseract 
- tesserocr [tesserocr安装](https://zhuanlan.zhihu.com/p/339208771)
- PIL

## 核心逻辑
- 移除无用的干扰线段 + 移除无用噪点
- 二值化 + ocr

## 核心代码
- [verify_code_ocr](./verify_code_ocr.py)
- []()

## 尚未解决
- 识别率大概是80%左右，部分连起来的字符会被识别错误
- 需要切割字符后再识别
- 降噪算法只适用于当前图片，其他场景需要自行适配