cmake_minimum_required(VERSION 3.15)
project(kie_http_parser CXX)

set(CMAKE_CXX_STANDARD 20)

option(BUILD_HTTP1 "If http1 component should be built" ON)
option(BUILD_HTTP2 "If http2 component should be built" ON)

if(BUILD_HTTP1)
    add_subdirectory(http1)
    add_library(kie_http_parser::http1 ALIAS http1)
endif()

if(BUILD_HTTP2)
    add_subdirectory(http2)
    add_library(kie_http_parser::http2 ALIAS http2)
endif()

