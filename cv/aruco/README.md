```sh
wget https://github.com/opencv/opencv_contrib/blob/master/modules/aruco/samples/calibrate_camera_charuco.cpp
wget https://github.com/opencv/opencv_contrib/blob/master/modules/aruco/samples/create_board_charuco.cpp

cmake .
make
```

```sh
# display [0,1,2,3] on screen
./GenerateDiamond 0 1 2 3

# encode [0,1,2,3] and save in out.jpg
./GenerateDiamond 0 1 2 3 out.jpg

```

```sh
./create_board_charuco -d=0 -h=5 -w=7 --ml=24 --sl=40 out.jpg

./calibrate_camera_charuco -d=0 -h=5 -w=7 --ml=0.024 --sl=0.04 out.yaml
```