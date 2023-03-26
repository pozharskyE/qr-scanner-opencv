def qr_from_live_video(cam_id =0, write_qr_arr =False, delay =1):
    import cv2
    cap = cv2.VideoCapture(cam_id)
    
    while True:
        _ , frame = cap.read()
        was_detected, decoded_info, _ , qr_array = cv2.QRCodeDetector().detectAndDecodeMulti(frame)
        cv2.imshow('QR scanner', frame)
        
        if was_detected:
            cv2.destroyWindow('QR scanner')

            if write_qr_arr:
                return decoded_info, qr_array
            else:
                return decoded_info
            
        
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyWindow('QR scanner')