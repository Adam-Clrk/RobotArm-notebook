cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable( GenerateDiamond GenerateDiamond.cpp )
target_link_libraries( GenerateDiamond ${OpenCV_LIBS} )

add_executable( calibrate_camera_charuco calibrate_camera_charuco.cpp )
target_link_libraries( calibrate_camera_charuco ${OpenCV_LIBS} )

add_executable( create_board_charuco create_board_charuco.cpp )
target_link_libraries( create_board_charuco ${OpenCV_LIBS} )