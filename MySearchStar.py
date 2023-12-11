import math
import time
import numpy as np
import pygame


class MySearchStar:

    def __init__(self, tile, colorfill=0, position=None):
        self.parent = self
        self.position = position

        # Total cost from starting node
        self.g = math.inf
        # Heuristic cost
        self.h = 0
        # Lowest cost from neighbouring node
        self.f = math.inf

        self.colorfill = colorfill
        self.rect = tile

        self.neighbours = []

def astar(grid, start, target_node, screen):
    start_node = start
    start_node.g = start_node.h = start_node.f = 0
    end_node = target_node
    end_node.g = end_node.h = end_node.f = 0

    no_rows, no_columns = np.shape(grid)  # Used for checking boundaries

    available_list = []  # Where can go
    visited_list = []  # Where it's been
    path = []  # Path array

    available_list.append(start_node)

    moves = ([-1, 0],  # Move up
             [1, 0],  # Move down
             [0, -1],  # Move left
             [0, 1])  # Move Right

    while len(available_list) > 0:

        current_node = available_list[0]
        current_index = 0
        for index, item in enumerate(available_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        time.sleep(.4)
        available_list.pop(current_index)
        visited_list.append(current_node)

        # Found the goal
        if current_node == target_node:
            return True

        for new_position in moves:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Checking boundaries
            if node_position[0] > (no_rows - 1) or node_position[0] < 0 or node_position[1] > (no_columns - 1) or node_position[1] < 0:
                continue

            # Ignoring Red tiles
            my_node = grid[node_position[0]][node_position[1]]

            if my_node.colorfill == 1:
                continue

            current_node.neighbours.append(my_node)

            for neighbour in current_node.neighbours:
                if neighbour in visited_list:
                    continue

                # Heuristic cost calculation:
                neighbour.g = current_node.g+1
                neighbour.h = ((neighbour.position[0] - end_node.position[0]) ** 2) + ((neighbour.position[1] - end_node.position[1]) ** 2)
                neighbour.f = neighbour.g + neighbour.h

                # Makes neighbour walkable again, updates path
                if neighbour not in available_list:
                    available_list.append(neighbour)
                    path.append(current_node.position)
                    pygame.draw.rect(screen, (255, 165, 0), neighbour.rect)
                    print('Parent: ', current_node.parent.position)
                    pygame.draw.rect(screen, (0, 255, 0), current_node.parent.rect)
                    pygame.display.update()

                    # If neighbour is target- make current node green and append the path
                if neighbour == target_node:
                    pygame.draw.rect(screen, (0, 255, 0), current_node.rect)
                    pygame.display.update()
                    print('Path: ', path)
                    print('Reversed path: ', path[::-1])
    return False
