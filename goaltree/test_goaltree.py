#!/usr/bin/env python

import unittest

from goaltree import GoalTree

class TestGoalTree(unittest.TestCase):

    def test_init(self):
        g = GoalTree('Test')
        self.assertEqual(g.parent, None)
        self.assertEqual(g.name, 'Test')
        g = GoalTree('parent', [ GoalTree('child')])
        self.assertEqual(g._children[0].parent, 'parent')
        self.assertEqual(g._children[0].name, 'child')
        self.assertEqual(g.name, 'parent')
        self.assertEqual(g.parent, None)

    def test_add_child(self):
        g = GoalTree('Test')
        g.add_child(GoalTree('child'))
        self.assertEqual(g._children[0].parent, 'Test')
        self.assertEqual(g._children[0].name, 'child')

    def test_bfs(self):
        g = GoalTree('root', [ GoalTree('child1', [ (GoalTree('subchild1'))]), GoalTree('child2')])
        subchild1 = g.bfs('subchild1')
        self.assertEqual(subchild1.parent, 'child1')
        self.assertEqual(subchild1.name, 'subchild1')

    def test_how(self):
        g = GoalTree('root',
            [ GoalTree('child1', [ GoalTree('subchild1'), GoalTree('subchild2') ]),
            GoalTree('child2') ])
        self.assertEqual(g.How('child1'), 'Following this steps: subchild1 & subchild2')
        self.assertEqual(g.How('Not exists'), 'I didn\'t.')
        self.assertEqual(g.How('child2'), 'By doing it.')

    def test_why(self):
        g = GoalTree('root',
            [ GoalTree('child1', [ GoalTree('subchild1'), GoalTree('subchild2') ]),
            GoalTree('child2') ])
        self.assertEqual(g.Why('Fuck the police'), 'I didn\'t.')
        self.assertEqual(g.Why('root'), 'Because you told me.')
        self.assertEqual(g.Why('subchild1'), 'Because I was trying to child1')

if __name__ == '__main__':
    unittest.main()
