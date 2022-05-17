import pygame

class Node:
    def __init__(self, state, parent=None, action=None):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(state = next_state, parent = self, action = action)
        return next_node

def And_Or_Search(problem):
    """
    :param problem:
    :return: a conditional plan, or failure
    """
    node = Node(problem.initial)
    return Or_Search(node, problem, [])


def Or_Search(state, problem, path):
    """

    :param state:
    :param problem:
    :param path:
    :return: a conditional plan, or failure
    """
    if problem.goalTest(state):
        return None
    if state in path:
        return False
    for action in problem.actions(state):
        plan = And_Or_Search(problem.results(state, action), problem, state)
        if plan:
           return action
    return False


def And_Search(states, problem, path):
    """

    :param states:
    :param problem:
    :param path:
    :return: a conditional plan, or failure
    """
    for state in states:
        plan = Or_Search(state, problem, path)
        if not plan:
            yield False
        else:
            yield plan