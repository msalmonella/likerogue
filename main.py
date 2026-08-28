import pyray as pr

def main():
    pr.init_window(800, 600, "My Pyray Window")

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)

        pr.draw_text("Hello, Pyray!", 300, 280, 20, pr.BLACK)

        pr.end_drawing()

    pr.close_window()


if __name__ == "__main__":
    main()
