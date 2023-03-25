def qr_from_img(image):
    import cv2
    img = cv2.imread(image)
    was_detected, decoded_info, _ , _ = cv2.QRCodeDetector().detectAndDecodeMulti(img)

    if was_detected:
        return decoded_info
    else:
        # print('Sorry, QR code was not detected. Please try again or another image.')
        return 'Sorry, QR code was not detected. Please try again or another image.'