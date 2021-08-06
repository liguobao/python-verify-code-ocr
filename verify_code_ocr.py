from PIL import Image
import tesserocr
from loguru import logger


class VerfyCodeOCR():
    def __init__(self) -> None:
        pass

    def ocr(self, img):
        """ 验证码OCR

        Args:
            img (img): imgObject/imgPath

        Returns:
            [string]: 识别结果
        """
        img_obj = Image.open(img) if type(img) == str else img
        self._remove_pil(img_obj)
        verify_code = tesserocr.image_to_text(img_obj)
        return verify_code.replace("\n", "").strip()

    def _get_p_black_count(self, img: Image, _w: int, _h: int):
        """ 获取当前位置周围像素点中黑色元素的个数

        Args:
            img (img): 图像信息
            _w (int): w坐标
            _h (int): h坐标

        Returns:
            int: 个数
        """
        w, h = img.size
        p_round_items = []
        # 超过了横纵坐标
        if _w == 0 or _w == w-1 or 0 == _h or _h == h-1:
            return 0
        p_round_items = [img.getpixel(
            (_w, _h-1)), img.getpixel((_w, _h+1)), img.getpixel((_w-1, _h)), img.getpixel((_w+1, _h))]
        p_black_count = 0
        for p_item in p_round_items:
            if p_item == (0, 0, 0):
                p_black_count = p_black_count+1
        return p_black_count

    def _remove_pil(self, img: Image):
        """清理干扰识别的线条和噪点

        Args:
            img (img): 图像对象

        Returns:
            [img]: 被清理过的图像对象
        """
        w, h = img.size
        for _w in range(w):
            for _h in range(h):
                o_pixel = img.getpixel((_w, _h))
                # 当前像素点是红色(线段) 或者 绿色（噪点）
                if o_pixel == (255, 0, 0) or o_pixel == (0, 0, 255):
                    # 周围黑色数量大于2，则把当前像素点填成黑色；否则用白色覆盖
                    p_black_count = self._get_p_black_count(img, _w, _h)
                    if p_black_count >= 2:
                        img.putpixel((_w, _h), (0, 0, 0))
                    else:
                        img.putpixel((_w, _h), (255, 255, 255))

        logger.info(f"_remove_pil finish.")
        # img.show()
        return img


if __name__ == '__main__':
    verfyCodeOCR = VerfyCodeOCR()
    img_path = "./imgs/51.png"
    img= Image.open(img_path)
    img.show()
    ocr_result = verfyCodeOCR.ocr(img)
    img.show()
    logger.info(ocr_result)
    
    
    
