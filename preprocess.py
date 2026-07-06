import cv2


def preprocess(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray,
        180,
        255,
        cv2.THRESH_BINARY_INV
    )

    coords = cv2.findNonZero(thresh)

    x, y, w, h = cv2.boundingRect(coords)

    crop = image[y:y+h, x:x+w]

    crop = cv2.copyMakeBorder(
        crop,
        40,
        40,
        40,
        40,
        cv2.BORDER_CONSTANT,
        value=(255,255,255)
    )

    output = image_path.replace(".jpg","_crop.jpg").replace(".png","_crop.png")

    cv2.imwrite(output,crop)

    return output