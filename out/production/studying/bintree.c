#include <stdio.h>
#include <stdlib.h>

typedef struct treenode{
    struct treenode *leftchild;
    char data;
    struct treenode *rightchild;
} TREE;

void inorder(TREE *currentnode)
{
    if(currentnode != NULL)
    {
        inorder(currentnode->leftchild);
        printf("%c",currentnode->data);
        inorder(currentnode->rightchild);
    }
}

void preorder(TREE *currentnode)
{
    if(currentnode != NULL)
    {
        printf("%c",currentnode->data);
        preorder(currentnode->leftchild);
        preorder(currentnode->rightchild);
    }
}

void postorder(TREE *currentnode)
{
    if(currentnode != NULL)
    {
        postorder(currentnode->leftchild);
        postorder(currentnode->rightchild);
        printf("%c",currentnode->data);
    }
}