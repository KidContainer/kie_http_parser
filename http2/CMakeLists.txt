cmake_minimum_required(VERSION 3.15)
project(http2 CXX)

aux_source_directory(src SOURCE)

add_library(http2 ${SOURCE})
target_include_directories(http2 PUBLIC include)

if(ENABLE_HTTP2_TEST)
    add_compile_options(-fsanitize=address -g --coverage)
    add_link_options(-fsanitize=address --coverage)
    add_subdirectory(test)
endif()

install(TARGETS http2)
install(DIRECTORY include/ DESTINATION include/http2)