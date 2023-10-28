package main

 type TreeNode struct {
    Val int
    Left *TreeNode
    Right * TreeNode
}

 type NodeLvlItem struct {
    node *TreeNode
    lvl int
}

func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    depth := 1
    var nodes []NodeLvlItem
    nodes = append(nodes, NodeLvlItem{root, 1})

    for len(nodes) > 0 {
        nodeLvlItem := nodes[len(nodes) - 1]
        node := nodeLvlItem.node
        lvl := nodeLvlItem.lvl

        nodes = nodes[:len(nodes) - 1]

        if lvl > depth {
            depth = lvl
        }

        if node.Left != nil {
            nodes = append(nodes, NodeLvlItem{node.Left, lvl + 1})
        }
        
        if node.Right != nil {
            nodes = append(nodes, NodeLvlItem{node.Right, lvl + 1})
        }
    }

    return depth
}