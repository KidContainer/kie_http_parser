add_executable(http2_test http2_test.cpp)
target_link_libraries(http2_test PUBLIC http2)
add_test(http2_test http2_test)