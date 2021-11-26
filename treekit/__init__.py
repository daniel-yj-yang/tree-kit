# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: MIT


from .__about__ import (
    __version__,
    __license__,
)

from .binarytree import binarytree, bst


# this is for "from <package_name> import *"
__all__ = ["binarytree", "bst"]
