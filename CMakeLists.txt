cmake_minimum_required(VERSION 3.14)
project(CExample LANGUAGES C)

# Enforce modern C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# Build the reusable function as a static library
add_library(add_lib STATIC src/example.c)

# Make the header available to anything that links to the library
target_include_directories(add_lib PUBLIC src)

# Build the main executable
add_executable(hello src/hello.c)

# Link the library to the executable
target_link_libraries(hello PRIVATE add_lib)
