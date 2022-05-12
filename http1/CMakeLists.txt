cmake_minimum_required(VERSION 3.15)
project(http1 CXX)

aux_source_directory(src SOURCE)

add_library(http1 ${SOURCE})
target_include_directories(http1 PUBLIC include)