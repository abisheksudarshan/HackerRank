/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

    Root: If node is root node.
    Leaf: If node is leaf node.
    Inner: If node is neither root nor leaf node.

*/

Solution:

select n, if(p is null,'Root',if((select count(*) from bst where p=b.n)>0,'Inner','Leaf')) from bst as b order by n;
