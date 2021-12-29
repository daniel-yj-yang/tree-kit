# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: MIT


from typing import List, Union
from pyvis.network import Network # see also https://visjs.org/
from pathlib import Path
import webbrowser



class TreeNode:
    def __init__(self, val: Union[float, int, str] = None, shape: str = "ellipse"):
        self.val = val
        self.children = []
        self.shape = shape

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class tree(object):
    def __init__(self, data: List[Union[float, int, str]] = [], *args, **kwargs):
        """
        https://en.wikipedia.org/wiki/Binary_tree#Arrays
        "Binary trees can also be stored in breadth-first order as an implicit data structure in arrays"
        """
        super().__init__(*args, **kwargs)
        self.treetype = 'Tree'
        self.root = None
        
    def __repr__(self) -> str:
        if self.root:
            return f"TreeNode({self.root.val})"

    def tree_traversals_summary(self):
      self.root = TreeNode('Tree Traversals')
      node_DFS = TreeNode('Depth-First Search\n(DFS)')
      node_BFS = TreeNode('Breadth-First Search\n(BFS)')
      node_BFS_iteration = TreeNode('BFS\nIteration w/ queue')
      node_BFS.children.extend([node_BFS_iteration,])
      node_preorder = TreeNode('Preorder')
      node_inorder = TreeNode('Inorder')
      node_postorder = TreeNode('Postorder')
      node_preorder_iteration = TreeNode('Preorder\nIteration w/ stack')
      node_preorder_recursion = TreeNode('Preorder\nRecursion')
      node_preorder_morris = TreeNode('Preorder\nMorris')
      node_inorder_iteration = TreeNode('Inorder\nIteration w/ stack')
      node_inorder_recursion = TreeNode('Inorder\nRecursion')
      node_inorder_morris = TreeNode('Inorder\nMorris')
      node_postorder_iteration = TreeNode('Postorder\nIteration w/ stack')
      node_postorder_recursion = TreeNode('Postorder\nRecursion')
      node_postorder_morris = TreeNode('Postorder\nMorris')
      node_preorder.children.extend([node_preorder_iteration, node_preorder_recursion, node_preorder_morris])
      node_inorder.children.extend([node_inorder_iteration, node_inorder_recursion, node_inorder_morris])
      node_postorder.children.extend([node_postorder_iteration, node_postorder_recursion, node_postorder_morris])
      node_DFS.children.extend([node_preorder, node_inorder, node_postorder])
      self.root.children.extend([node_DFS, node_BFS])
      self.show(heading='Tree Traversals')

    def validate_IP_address(self):
      self.root = TreeNode('IP string', shape = 'text')
      level1_three_dots = TreeNode('Contains 3 dots', shape='text')
      level1_seven_colons = TreeNode('Contains 7 colons', shape='text')
      level1_neither = TreeNode('Otherwise, return \"Neither\"', shape='text')
      level2_ip4_validate = TreeNode('Validate each \"IPv4\" chunk', shape='text')
      level3_ip4_valid = TreeNode('Valid, return \"IPv4\"', shape='text')
      level3_ip4_invalid = TreeNode('Invalid, return \"Neither\"', shape='text')
      level2_ip6_validate = TreeNode('Validate each \"IPv6\" chunk', shape='text')
      level3_ip6_valid = TreeNode('Valid, return \"IPv6\"', shape='text')
      level3_ip6_invalid = TreeNode('Invalid, return \"Neither\"', shape='text')
      level2_ip4_validate.children.extend([level3_ip4_valid, level3_ip4_invalid])
      level2_ip6_validate.children.extend([level3_ip6_valid, level3_ip6_invalid])
      level1_three_dots.children.extend([level2_ip4_validate])
      level1_seven_colons.children.extend([level2_ip6_validate])
      self.root.children.extend([level1_three_dots, level1_seven_colons, level1_neither])
      self.show(heading='Validate IP Address')

    def remove_invalid_parenthese(self, s: str = '()())a)b()))'):
      """
      https://leetcode.com/problems/remove-invalid-parentheses/
      """
      def DFS(s='', pair=('(', ')'), anomaly_scan_left_range=0, removal_scan_left_range=0, depth=0, parent: TreeNode = None):
        # phase 1: scanning for anomaly
        stack_size = 0
        for index_i in range(anomaly_scan_left_range, len(s)):
            if s[index_i] == pair[0]:
                stack_size += 1
            elif s[index_i] == pair[1]:
                stack_size -= 1
                if stack_size == -1:
                    break
        if stack_size < 0:
            # phase 2: scanning for removal
            for index_j in range(removal_scan_left_range, index_i+1):
                if s[index_j] == pair[1]:
                    if index_j == removal_scan_left_range or s[index_j-1] != pair[1]:
                        new_s = s[:index_j] + s[(index_j+1):len(s)]
                        # add the node - start
                        if pair[0] == '(':
                          curr_node = TreeNode(val=new_s)
                        else:
                          curr_node = TreeNode(val=new_s[::-1])
                        parent.children.append(curr_node)
                        # add the node - end
                        DFS(s=new_s, pair=pair, anomaly_scan_left_range=index_i, removal_scan_left_range=index_j, depth=depth+1, parent=curr_node)
        elif stack_size > 0:
            # phase 3: reverse scanning
            DFS(s=s[::-1], pair=(')', '('), depth=depth, parent=parent)
        else:
          if pair[0] == '(':
              res.append(s)
          else:
              res.append(s[::-1])
      res = []
      self.root = TreeNode(val=s)
      DFS(s=s, pair=('(', ')'), depth=0, parent=self.root)
      self.show(heading='DFS Search Space for Removing Invalid Parentheses')
      return res

    def show(self, filename: str = 'output.html', heading: str = None):
        if not self.root:
            return
        def dfs(parent, level=0):
            if parent.children:
              for child in parent.children:
                g.add_node(n_id=id(child), label=child.val, shape=child.shape, level=level+1, title=f"child node of Node({parent.val}), level={level+1}")
                g.add_edge(source=id(parent), to=id(child))
                dfs(child, level=level+1)               
        g = Network(width='100%', height='60%')
        g.add_node(n_id=id(self.root), label=self.root.val, shape=self.root.shape, level=0, title=f"root node of the tree, level=0")
        dfs(parent=self.root)
        if not heading:
          g.heading = f"{self.treetype}"
        else:
          g.heading = heading
        g.set_options("""
var options = {
  "nodes": {
    "font": {
      "size": 20
    }
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true
      }
    },
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
      "centralGravity": 0,
      "springConstant": 0.2,
      "nodeDistance": 150
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  },
  "configure": {
      "enabled": true,
      "filter": "layout,physics" 
  }
}""")
        full_filename = Path.cwd() / filename
        g.write_html(full_filename.as_posix())
        webbrowser.open(full_filename.as_uri(), new = 2)
        return g
