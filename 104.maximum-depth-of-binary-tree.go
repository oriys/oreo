/*
 * @lc app=leetcode id=104 lang=golang
 *
 * [104] Maximum Depth of Binary Tree
 */
/**
 * Definition for a binary tree node.
 */
 package leetcode
 
 
 type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }
 
func maxDepth(root *TreeNode) int {
	return getMax(root,0)
}

func getMax(node *TreeNode,depth int)int   {
	if node==nil {
		return depth
	}
	depth++
	left:=getMax(node.Left,depth)
	right:=getMax(node.Right,depth)
	if left>right{
		return left
	}
	return right
}

