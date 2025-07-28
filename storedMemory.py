import pygame
import sys

def load_points(file_path):
    points = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    x, y = map(float, line.strip().split(","))
                    points.append((int(x), int(y)))
                except ValueError:
                    print(f"⚠️ Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    return points

def draw_points(points, screen, color=(255, 0, 0), radius=5):
    for x, y in points:
        pygame.draw.circle(screen, color, (x, y), radius)

def main():
    file_path = "training data/9.txt"  # You can change this to any .txt file
    points = load_points(file_path)

    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Drawing from TXT")
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background

        draw_points(points, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
