#include<iostream>
#include<cstdlib>
using namespace std;
struct node
{
int key;
struct node *left,*right;
};
struct node *newNode(int item)
{
struct node *temp=(struct node *)malloc(sizeof(struct node));
temp->key=item;
temp->left=temp->right=NULL;
return temp;
}
void inorder(struct node *root)
{
if(root !=NULL)
{
inorder(root->left);
cout<<root->key<<"->";
inorder(root->right);
}
}
struct node *insert(struct node *node,int key)
{
if(node==NULL)return newNode(key);
if(key<node->key)
node->left=insert(node->left,key);
else
node->right=insert(node->right,key);
return node;
}
struct node *minvalueNode(struct node *node){
struct node *current=node;
while(current && current->left!=NULL)
current=current->left;
return current;
}
struct node *deleteNode(struct node *root,int key){
if(root==NULL)return root;
if(key<root->key)
root->left=deleteNode(root->left,key);
else if(key>root->key)
root->right=deleteNode(root->right,key);
else
{
if(root->left==NULL)
{
struct node *temp=root->right;
free(root);
return temp;
}
else if(root->right=NULL)
{
struct node *temp=root->left;
free(root);
return temp;
}
struct node *temp=minvalueNode(root->right);
root->key=temp->key;
root->right=deleteNode(root->right,temp->key);
}
return root;
}
int main()
{
struct node *root=NULL;
root=insert(root,50);
root=insert(root,30);
root=insert(root,20);
root=insert(root,40);
root=insert(root,70);
root=insert(root,60);
root=insert(root,80);
cout<<"Inorder traversal:";
inorder(root);
cout<<"\nAfter deleting 60\n";
root=deleteNode(root,60);
cout<<"Inorder traversal:";
inorder(root);
