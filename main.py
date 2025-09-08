import cv2
import sys

# 讀取圖片
# cv2.imread() 的第二個參數 cv2.IMREAD_GRAYSCALE 會直接將圖片讀取為灰階
image_path = "image/google_account_avatar.jpg"
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 檢查圖片是否成功讀取
if grayscale_image is None:
    print(f"錯誤: 無法讀取圖片 {image_path}")
    sys.exit(1)

# 顯示灰階圖片
cv2.imshow("Grayscale Image", grayscale_image)

# 等待使用者按下任意鍵
cv2.waitKey(0)

# 銷毀所有視窗
cv2.destroyAllWindows()

print("圖片已顯示，請關閉視窗。")