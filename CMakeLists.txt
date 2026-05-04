cmake_minimum_required(VERSION 3.14)
project(CExample LANGUAGES C)

# Enforce modern C standard (no GNU extensions)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# ──────────────────────────────────────────────────────────────
# Automatically find ALL .c files for the library
# ──────────────────────────────────────────────────────────────
file(GLOB_RECURSE ADD_LIB_SOURCES CONFIGURE_DEPENDS
    "src/*.c"
)

# Exclude hello.c so main() doesn't end up in the library
list(REMOVE_ITEM ADD_LIB_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/hello.c")

add_library(add_lib STATIC ${ADD_LIB_SOURCES})

# Make headers available to the library and anything that links against it
target_include_directories(add_lib PUBLIC src)
# ──────────────────────────────────────────────────────────────

# Executable (only the file that contains main())
file(GLOB_RECURSE HELLO_SOURCES CONFIGURE_DEPENDS
    "src/hello.c"
)

add_executable(hello ${HELLO_SOURCES})
target_link_libraries(hello PRIVATE add_lib)
