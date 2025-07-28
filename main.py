import pygame
import sys
import config
import math
import runpy
import os

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("ez")

clock = pygame.time.Clock()

drawing = False
drawn_positions = []

sk = config.sk

import math
def load_points(filename):
    points = []
    with open(filename, "r", encoding="latin-1") as f:
        for line in f:
            try:
                x, y = map(float, line.strip().split(","))
                points.append((x, y))
            except ValueError:
                print(f"Skipping invalid line in {filename}: {line.strip()}")
    return points

def dist(points1, points2):
    min_len = min(len(points1), len(points2))
    total = 0
    for i in range(min_len):
        x1, y1 = points1[i]
        x2, y2 = points2[i]
        total += math.hypot(x1 - x2, y1 - y2)
    return total

def compare_with_training_data(input_file, training_folder):
    input_points = load_points(input_file)
    distance_list = []

    for i in range(10):  # 0.txt to 9.txt
        train_file = os.path.join(training_folder, f"{i}.txt")
        if os.path.exists(train_file):
            try:
                train_points = load_points(train_file)
                total_dist = dist(input_points, train_points)
                distance_list.append((i, total_dist))
            except Exception as e:
                print(f"❌ Error comparing with {i}.txt: {e}")
        else:
            print(f"⚠️ File {i}.txt not found")
    distance_list.sort(key=lambda x: x[1])
    print("\n📊 :")
    for i, d in distance_list:
        print(f"{i}: {d/1000}")

    if distance_list:
        best_match = distance_list[0]
        print(f"\n✅ Closest match: {best_match[0]}")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open(sk, "w").close()
            with open(sk, "w") as f:
                for pos in drawn_positions:
                    f.write(f"{pos[0]},{pos[1]}\n")
                
            
            compare_with_training_data("input.txt", "training data")
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        drawn_positions.append(mouse_pos)
        pygame.draw.circle(screen, (255,0,0), mouse_pos,5)  # Draw dot at cursor

    pygame.display.flip()
    clock.tick(120)


    pygame.display.flip()  # Update the display

# Clean up
pygame.quit()
sys.exit()
