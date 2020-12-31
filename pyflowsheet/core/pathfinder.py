from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.core.heuristic import chebyshev, null, manhatten
from pathfinding.core.util import SQRT2
from math import pow
from pathfinding.core.util import backtrace, bi_backtrace
import heapq


def distance(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


def compressPath(path):
    if len(path) < 2:
        return path
    deltaPath = []
    newPath = []

    newPath.append(path[0])

    for i, n in enumerate(path[1:]):
        deltaPath.append((n[0] - path[i][0], n[1] - path[i][1]))

    for i, delta in enumerate(deltaPath[1:]):
        lastDelta = deltaPath[i]
        if delta[0] != lastDelta[0] or delta[1] != lastDelta[1]:
            newPath.append(path[i + 1])
    newPath.append(path[-1])
    return newPath


def rectifyPath(path, grid, end):

    if len(path) < 2:
        return path

    newPath = []
    deltaPath = []
    last = path[0]
    goal = (end.x, end.y)

    containsBends = True

    while containsBends:
        i = 0
        containsBends = False
        while i < len(path) - 2:
            if (
                path[i][0] == path[i + 1][0]
                and path[i][1] > path[i + 2][1]
                and path[i + 1][0] > path[i + 2][0]
            ):
                print("Up/Left-Bend detected")
                containsBends = True

                newNode = (path[i + 2][0], path[i][1])
                path.remove(path[i])
                path.remove(path[i])
                path.remove(path[i])
                path.insert(i, newNode)

            i += 1
    for n in path:
        newPath.append(n)
    # newPath.append(path[-2])
    # newPath.append(path[-1])
    # newPath.append(path[])

    return newPath


class Pathfinder(AStarFinder):
    def __init__(self, turnPenalty=150):
        super(Pathfinder, self).__init__(
            diagonal_movement=DiagonalMovement.never, heuristic=null
        )

        self.turnPenalty = turnPenalty
        return

    def process_node(self, node, parent, end, open_list, open_value=True):
        """
        we check if the given node is path of the path by calculating its
        cost and add or remove it from our path
        :param node: the node we like to test
            (the neighbor in A* or jump-node in JumpPointSearch)
        :param parent: the parent node (the current node we like to test)
        :param end: the end point to calculate the cost of the path
        :param open_list: the list that keeps track of our current path
        :param open_value: needed if we like to set the open list to something
            else than True (used for bi-directional algorithms)
        """
        # calculate cost from current node (parent) to the next node (neighbor)
        ng = self.calc_cost(parent, node)

        lastDirection = (
            None
            if parent.parent == None
            else (parent.x - parent.parent.x, parent.y - parent.parent.y)
        )
        turned = (
            0
            if lastDirection == None
            else (
                lastDirection[0] != parent.x - node.x
                or lastDirection[1] != parent.y - node.y
            )
        )

        ng += self.turnPenalty * turned

        if not node.opened or ng < node.g:
            node.g = ng
            node.h = node.h or self.apply_heuristic(node, end) * self.weight
            # f is the estimated total cost from start to goal
            node.f = node.g + node.h
            node.parent = parent

            if not node.opened:
                heapq.heappush(open_list, node)
                node.opened = open_value
            else:
                # the node can be reached with smaller cost.
                # Since its f value has been updated, we have to
                # update its position in the open list
                open_list.remove(node)
                heapq.heappush(open_list, node)

    def calc_cost(self, node_a, node_b):
        """
        get the distance between current node and the neighbor (cost)
        """
        if node_b.x - node_a.x == 0 or node_b.y - node_a.y == 0:
            # direct neighbor - distance is 1
            ng = 1
        else:
            # not a direct neighbor - diagonal movement
            ng = SQRT2

        # weight for weighted algorithms
        if self.weighted:
            ng *= node_b.weight

        return node_a.g + ng
