#include <stdio.h>
#include "opencv2/opencv.hpp"
// #include "opencv2/opencv.hpp"
#include "opencv2/aruco.hpp"
#include "opencv2/aruco/charuco.hpp"

using namespace std;
using namespace cv;

int main(int argc, char *argv[])
{
	if (argc < 1+4)
	{
		return 1;
	}
	Mat diamondImage;
	Vec4i v = Vec4i(stoi(argv[1]),stoi(argv[2]),stoi(argv[3]),stoi(argv[4]));
	Ptr<aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_4X4_50);
	aruco::drawCharucoDiamond(dictionary, v, 200, 120, diamondImage);
	if (argc > 5)
	{
		cout << argv[5];
		imwrite(argv[5],diamondImage);
	}
	else
	{
		namedWindow("Display Image", WINDOW_AUTOSIZE );
		imshow("Display Image", diamondImage);
		waitKey(0);
	}
	return 0;
}
