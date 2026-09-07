cmake_minimum_required(VERSION 3.8)
project(msgpkg)
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Status.msg"
  "srv/AddTwoInts.srv"
  "action/CountDown.action"
)
ament_package()
