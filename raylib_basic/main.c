#include "raylib.h"

int main(void)
{
    //--------------------------------------------------------------------------------------
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");
    SetTargetFPS(60);               // We want 60 FPS
    //--------------------------------------------------------------------------------------

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // Update
        // (nothing to update in this tiny example)

        // Draw
        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawText("Congrats! You created your first raylib window!", 120, 200, 20, LIGHTGRAY);
            DrawText("(C with CMake)", 300, 240, 20, GRAY);
        EndDrawing();
    }

    // De-initialization
    CloseWindow();
    return 0;
}
