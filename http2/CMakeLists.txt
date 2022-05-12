cmake_minimum_required(VERSION 3.15)
project(http2 CXX)

aux_source_directory(src SOURCE)

add_library(http2 ${SOURCE})
target_include_directories(http2 PUBLIC include)