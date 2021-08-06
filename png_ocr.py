from PIL import Image
import tesserocr


#tesserocr识别图片的2种方法

img = Image.open("./imgs/98.png")
img.show()
w, h = img.size


def get_p_black_count(img, _w, _h):
    w, h = img.size
    p_round_items = []
    if _w == 0 or _w == w-1 or 0 == _h or _h == h-1:
        return 0
    p_round_items = [img.getpixel(
        (_w, _h-1)), img.getpixel((_w, _h+1)), img.getpixel((_w-1, _h)), img.getpixel((_w+1, _h))]
    p_black_count = 0
    for p_item in p_round_items:
        if p_item == (0, 0, 0):
            p_black_count = p_black_count+1
    return p_black_count


for _w in range(w):
    for _h in range(h):
        o_pixel = img.getpixel((_w, _h))
        if o_pixel == (255, 0, 0) or o_pixel == (0, 0, 255):
            # 周围有黑色
            p_black_count = get_p_black_count(img, _w, _h)
            if p_black_count >= 2:
                img.putpixel((_w, _h), (0, 0, 0))
            else:
                img.putpixel((_w, _h), (255, 255, 255))
img.show()
img_l = img.convert("L")
img_l.show()
verify_code1 = tesserocr.image_to_text(img)
verify_code2 = tesserocr.image_to_text(img_l)
print(f"verify_code1:{verify_code1}")
print(f"verify_code2:{verify_code2}")
