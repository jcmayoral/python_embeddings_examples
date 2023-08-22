cmake_minimum_required(VERSION 3.22)
project(python_embeddings)
find_package(Python3 REQUIRED COMPONENTS Development)


add_executable(output main.cpp)
include_directories(output ${Python3_INCLUDE_DIRS})

add_executable(function_call function_call.cpp)
include_directories(function_call ${Python3_INCLUDE_DIRS})


target_link_libraries(output PRIVATE 
    ${Python3_LIBRARIES})

target_link_libraries(function_call PRIVATE 
    ${Python3_LIBRARIES})   

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/func.py
     DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

