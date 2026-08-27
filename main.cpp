#include "raylib.h"
#include "rlgl.h"


int main(void)
{
	const int screenWidth = 1280;
	const int screenHeight = 720;
	const int map_size = 10;
	Camera camera = Camera3D{
		Vector3{0, 0.5f, 0},
			Vector3{1, 0.5f, 1},
			Vector3{0, 1, 0},
			60.0f,
			CAMERA_PERSPECTIVE
	};

	InitWindow(screenWidth, screenHeight, "raylib test (C++)");
	rlSetLineWidth(3);
	SetTargetFPS(60);

	while (!WindowShouldClose())
	{
		BeginDrawing();
		ClearBackground(SKYBLUE);
		BeginMode3D(camera);
		DrawGrid(map_size * 10, 0.2);
		DrawPlane(Vector3{0, -0.1f, 0}, Vector2{map_size * 10, 0.2f}, WHITE);
		EndMode3D();
		DrawFPS(10, 10);
		EndDrawing();
	}

	CloseWindow();
	return 0;
}
