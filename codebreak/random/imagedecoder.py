import cv2

def decode(image):
    print(image)


if __name__ == '__main__':
    fd = cv2.imread('letsplay.jpg')
    result = decode(fd)
