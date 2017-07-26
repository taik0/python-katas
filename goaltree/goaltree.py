#!/usr/bin/env python

class GoalTree():

    def __init__(self, name, childs = []):
        self.name = name
        self.parent = None
        self._children = []
        for child in childs:
            self.add_child(child)

    def add_child(self, child):
        child.parent = self.name
        self._children.append(child)

    def children(self):
        for child in self._children:
            yield child

    def bfs(self, command):
        if self.name == command:
            return self
        q = [self]
        visited = [self]
        while len(q) > 0:
            current = q.pop(0)
            if current.name == command:
                return current
            for child in current.children():
                if child not in visited:
                    visited.append(child)
                    q.append(child)
        return None

    def How(self, command):
        """
        - I didn't
        - Following this steps: step1 & step2 & ...
        - By doing it
        """
        item = self.bfs(command)
        if item == None:
            return "I didn't."
        elif len(item._children) == 0:
            return "By doing it."
        else:
            return 'Following this steps: ' + ' & '.join([child.name for child in item.children()])

    def Why(self, command):
        """
        - You told me
        - I didn't
        - Because I was trying to X
        """
        item = self.bfs(command)
        if item == None:
            return "I didn't."
        elif item.parent == None:
            return "Because you told me."
        else:
            return "Because I was trying to %s" % (item.parent)
