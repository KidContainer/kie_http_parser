cmake_minimum_required(VERSION 3.15)
project(http1 CXX)

aux_source_directory(src SOURCE)

add_library(http1 ${SOURCE})
target_include_directories(http1 PUBLIC include)

if(ENABLE_HTTP1_TEST)
    add_compile_options(-fsanitize=address -g --coverage)
    add_link_options(-fsanitize=address --coverage)
    add_subdirectory(test)
endif()