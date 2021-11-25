# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: MIT

from typing import List, Union

from pyvis.network import Network

import webbrowser

import pathlib

class Node:
    def __init__(self, val: Union[float, int, str] = None, left = None, right = None):
        self.val = val
        self.left = left    # left child node
        self.right = right  # right child node

    def __repr__(self) -> str:
        return f"Node({self.val})"


class binarytree(object):
    def __init__(self, data: List[Union[float, int, str]] = [1,2,3,None,5]):
        """
        data must be in levelorder
        """
        nodes = [None if d is None else Node(d) for d in data] # 'if d is None' is important because sometimes d = 0 but we still want Node(0)
        for i in range(1, len(nodes)):
            curr = nodes[i]
            if curr:
                parent = nodes[(i - 1) // 2]
                if i % 2:
                    parent.left = curr
                else:
                    parent.right = curr
        self.root = nodes[0] if nodes else None
    
    def show(self, filename: str = 'output.html'):
        if self.root is None:
            return
        def dfs(node, level=1):
            if node:
                g.add_node(node.val, level=level)
                if node.left:
                    g.add_node(node.left.val, level=level+1)
                    g.add_edge(node.val, node.left.val)
                    dfs(node.left, level=level+1)
                else:
                    hidden_left_n_id = f"{node.val}'s left child = None"
                    g.add_node(hidden_left_n_id, level=level+1, hidden = True) # label = ' ', color = 'white')
                    g.add_edge(node.val, hidden_left_n_id, hidden = True) # color = 'white')
                if node.right:
                    g.add_node(node.right.val, level=level+1)
                    g.add_edge(node.val, node.right.val)
                    dfs(node.right, level=level+1)
                else:
                    hidden_right_n_id = f"{node.val}'s right child = None"
                    g.add_node(hidden_right_n_id, level=level+1, hidden = True) # label = ' ', color = 'white')
                    g.add_edge(node.val, hidden_right_n_id, hidden = True) # color = 'white')                    
        g = Network(directed=True, width='100%', height='100%')
        dfs(self.root)
        g.set_options("""
var options = {
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "sortMethod": "directed"
    }
  },
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }
}
""")
        full_filename = pathlib.Path.cwd() / filename
        g.show(full_filename.as_posix())
        webbrowser.open(full_filename.as_uri(), new = 2)





        