add_executable(http1_test http1_test.cpp)
target_link_libraries(http1_test PUBLIC http1)
add_test(http1_test http1_test)