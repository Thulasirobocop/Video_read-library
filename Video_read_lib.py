def Video_read(src,length,width):
    import cv2
    cap = cv2.VideoCapture(src)
    success, img = cap.read()
    while (success):
        #success, img = cap.read()
        img=cv2.resize(img,(length,width))
        cv2.imshow('img',img)
        # read next frame
        success, img = cap.read()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
