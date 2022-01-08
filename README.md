![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=abedinsherifi&show_icons=true)
![Your Repository's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=abedinsherifi&theme=blue-green)
![](https://komarev.com/ghpvc/?username=abedinsherifi)

<p align="center">
  <a href="https://github.com/prespafree1/Harris-Corner-Detector">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/prespafree1/Harris-Corner-Detector.svg">
  </a>
  <a href="https://github.com/prespafree1/Harris-Corner-Detector">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/prespafree1/Harris-Corner-Detector.svg">
  </a>
    <a href="https://github.com/prespafree1/Harris-Corner-Detector/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/prespafree1/Harris-Corner-Detector" /></a>
</p>

# Harris Corner Detector Algorithm
## Introduction
The Harris Corner Detector algorithm was applied to a picture. A brief overview of the steps involved in this algorithm is given below: <br>
→ First the input image was read and was converted from RGB to Gray. <br>
→ Gaussian filter was applied with a 9x9 kernel and sigmax/sigmay of 3. <br>
→ X and Y gradients were computed using the sobel filter with kernel size of 9x9. <br>
→ The components of the matrix M were calculated. These component are Ix^2, Iy^2, and IxIy. <br>
→ The corner response function is calculated. <br>
→ The last step of the algorithm is the execution of non-maximum suppression. This is the step were had to empirically choose a threshold value above which a corner is detected. <br>

OpenCV libraries were used throughout the code. Lastly, a corner count is displayed on the image. <br>
The output file from running the Harris Code Detector is shown below: <br>


## ORB Detector
One of the first algorithms used was the ORB detector. One of the tasks within SLAM is the localization of landmarks in our environment. The ORB detector is a very good detector in localizing such landmarks. The ORB detector is a very fast and accurate detector which is based out of the FAST algorithm for keypoint detection and on the BRIEF algorithm for calculation of descriptors. Once keypoints are located on a frame, descriptors are matched from the current frame
to the previous frame using the Brute Force matcher. <br>

## Point Cloud
I also presented the camera positions and the landmarks in a point cloud. What is a point cloud? A point cloud is a set of data points in 3D space. The 3D point cloud will consist of landmark data points as well as camera position points. Multiple frames are run in order to get depth information in 2D which assists in displaying the point cloud in 3D. <br>

## Camera Position
One of the main tasks in Mono SLAM is to figure out the camera position. The camera angle could change frame to frame. One of the ways to figure this out is through the fundamental matrix. The fundamental matrix is used for uncalibrated cameras. The essential matrix is essentially the same thing but is used for calibrated cameras. The fundamental matrix is calculated through the use of the 8-point algorithm. The 8-point algorithm as the name suggests takes in 8 correspondence points and outputs a homogeneous linear equation. The fundamental matrix was computed through
cv2.findFundamentalMat function of opencv. <br>

## Camera Info
Camera has two characteristics. It has intrinsic and extrinsic parameters. One of the main matrices is the intrinsic matrix. The intrinsic matrix is made of the image size and the focal length of the camera. My camera focal length is equal to 339. The extrinsic matrix consists of the rotation matrix and the translation vector. The camera matrix is the multiplication of the intrinsic matrix and the extrinsic matrix. The rotation and translation matrices are calculated through the use of the recoverPose function in opencv. Initially we are going to get 2D points. In order to go from 2D point to 3D point, we need to multiple the camera matrix with the 2D point at time t. <br>

## Results
A snapshot of the 3D point cloud of landmarks and camera positions as well as ORB detector keypoints on the video capture and camera position points are given in the image below. <br>
![](images/MonoSLAMCamPos.png) <br>

![](images/MonoSLAM1.png) <br>

![](images/MonoSLAMCloud.png) <br>

https://abedinsherifi.github.io/Mono-SLAM/
