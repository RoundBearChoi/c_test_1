cmake_minimum_required(VERSION 3.14)
project(CExample LANGUAGES C)

# Enforce modern C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# ──────────────────────────────────────────────────────────────
# AUTOMATICALLY find ALL .c files for the library
# ──────────────────────────────────────────────────────────────
file(GLOB_RECURSE ADD_LIB_SOURCES CONFIGURE_DEPENDS
    "src/*.c"          # All .c files in src/ and any subdirectories
)

add_library(add_lib STATIC ${ADD_LIB_SOURCES})

# Make headers available
target_include_directories(add_lib PUBLIC src)
# ──────────────────────────────────────────────────────────────

file(GLOB_RECURSE HELLO_SOURCES CONFIGURE_DEPENDS
    "src/hello.c"
)

add_executable(hello ${HELLO_SOURCES})

target_link_libraries(hello PRIVATE add_lib)
