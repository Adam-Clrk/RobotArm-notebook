import cv2 as cv
import numpy as np

def imagesToHtmlPage(filename, image_uris, image_width="8cm", image_margins="1cm"):
    data = '''
<!DOCTYPE html>
<html>
<head>
<style>
img {
    image-rendering: crisp-edges;
'''
    data += f'    width: {image_width};'
    data += f'    margin: {image_margins};'
    data += '''
}
html {
    background: gray;
}
body {
    position: absolute;
    background: white;
}
html, body {
    margin: 0;
    padding: 0;
    text-align: center;
}
*, *:before, *:after {
    box-sizing: inherit;
    font-family: inherit;
}
@page {
    size: A4 portrait;
    margin: 0;
}
@media screen {
    html, body {
        width: 210mm;
        /*height: 297mm;*/
    }
}
</style>
</head>
<body>
'''
    for image_uri in image_uris:
        data += f'<img src="{image_uri}">'
    data += '</body></html>'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def get_calibration(filename, new=None):
    camera_params = cv.FileStorage(filename, cv.FileStorage_READ)
    camera_matrix_node = camera_params.getNode('camera_matrix').getNode('data')
    distortion_coefficients_node = camera_params.getNode('distortion_coefficients').getNode('data')
    camera_matrix = np.array([[camera_matrix_node.at((3*j)+i).real() for i in range(3)] for j in range(3)])
    distortion_coefficients = np.array([distortion_coefficients_node.at(i).real() for i in range(5)])
    w = int(camera_params.getNode('image_width').real())
    h = int(camera_params.getNode('image_height').real())
    if new != None:
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w,h), 1, new)
    else:
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w,h), 1, (w,h))
    return (camera_matrix,distortion_coefficients,newcameramtx,roi)


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    d = np.dot(v1_u, v2_u)
    return np.arccos(np.clip(d, -1.0, 1.0))