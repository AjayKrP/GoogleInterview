def rotate_image_by_90_degree(image):
    m = len(image)
    n = len(image[0])

    for i in range(m//2):
        for j in range(i, n-1-i):
            pass