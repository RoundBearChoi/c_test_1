cmake_minimum_required(VERSION 3.11)
project(raylib_basic C)

# Raylib works with C99, but C11 is also fine and more modern
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Fetch raylib automatically (no need to install it system-wide)
include(FetchContent)
FetchContent_Declare(
    raylib
    GIT_REPOSITORY https://github.com/raysan5/raylib.git
    GIT_TAG        6.0          # Latest stable as of May 2026
    GIT_SHALLOW    TRUE
)

# Optional but highly recommended: don't build raylib's own examples/games
# (saves a lot of compile time on the first build)
set(BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(BUILD_GAMES    OFF CACHE BOOL "" FORCE)

FetchContent_MakeAvailable(raylib)

# Your executable
add_executable(${PROJECT_NAME} main.c)

# Link raylib
target_link_libraries(${PROJECT_NAME} PRIVATE raylib)

# Nice-to-have: organize the build folder cleanly
set_property(TARGET ${PROJECT_NAME} PROPERTY VS_DEBUGGER_WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}")
