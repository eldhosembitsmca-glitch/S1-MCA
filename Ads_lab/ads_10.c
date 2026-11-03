#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node *lchild;
    int data;
    struct node *rchild;
} *root = NULL, *new, *p, *tp, *t;

void create()
{
    new = (struct node *)malloc(sizeof(struct node));

    printf("Enter the data to the node: ");
    scanf("%d", &new->data);

    new->lchild = NULL;
    new->rchild = NULL;
}

void search(struct node *rt)
{
    if (new->data < rt->data)
    {
        if (rt->lchild == NULL)
            rt->lchild = new;
        else
            search(rt->lchild);
    }
    else if (new->data > rt->data)
    {
        if (rt->rchild == NULL)
            rt->rchild = new;
        else
            search(rt->rchild);
    }
    else
    {
        printf("Duplicate value not allowed\n");
        free(new);
    }
}

void insert()
{
    create();

    if (root == NULL)
        root = new;
    else
        search(root);
}

void preorder(struct node *rt)
{
    if (rt != NULL)
    {
        printf("%d->", rt->data);
        preorder(rt->lchild);
        preorder(rt->rchild);
    }
}

void postorder(struct node *rt)
{
    if (rt != NULL)
    {
        postorder(rt->lchild);
        postorder(rt->rchild);
        printf("%d->", rt->data);
    }
}

void inorder(struct node *rt)
{
    if (rt != NULL)
    {
        inorder(rt->lchild);
        printf("%d->", rt->data);
        inorder(rt->rchild);
    }
}



void deletenode(struct node *rt)
{

    if (rt->lchild == NULL && rt->rchild == NULL)
    {
        if (rt == root)
        {
            root = NULL;
        }
        else if (rt == p->lchild)
        {
            p->lchild = NULL;
        }
        else
        {
            p->rchild = NULL;
        }

        free(rt);
    }

    else if (rt->lchild != NULL && rt->rchild == NULL)
    {
        if (rt == root)
        {
            root = rt->lchild;
        }
        else if (rt == p->lchild)
        {
            p->lchild = rt->lchild;
        }
        else
        {
            p->rchild = rt->lchild;
        }

        free(rt);
    }

    
    else if (rt->lchild == NULL && rt->rchild != NULL)
    {
        if (rt == root)
        {
            root = rt->rchild;
        }
        else if (rt == p->lchild)
        {
            p->lchild = rt->rchild;
        }
        else
        {
            p->rchild = rt->rchild;
        }

        free(rt);
    }

  
    else
    {
        t = rt->rchild;
        tp = rt;

        while (t->lchild != NULL)
        {
            tp = t;
            t = t->lchild;
        }

        rt->data = t->data;

        if (tp != rt)
            tp->lchild = t->rchild;
        else
            tp->rchild = t->rchild;

        free(t);
    }
}

void dsearch(struct node *rt, int val)
{
    if (rt == NULL)
    {
        printf("Element not found\n");
        return;
    }

    if (val < rt->data)
    {
        p = rt;
        dsearch(rt->lchild, val);
    }
    else if (val > rt->data)
    {
        p = rt;
        dsearch(rt->rchild, val);
    }
    else
    {
        deletenode(rt);
    }
}

void delete()
{
    int val;

    printf("Enter the value to be deleted: ");
    scanf("%d", &val);

    dsearch(root, val);
}

int main()
{
    int ch;
     printf("\n\n1) Insert");
        printf("\n2) Preorder");
        printf("\n3) Postorder");
        printf("\n4) Inorder");
        printf("\n5) Delete");
        printf("\n6) Exit");

    do
    {
        
        ch=0;
        printf("\n\nChoose Option: ");
        scanf("%d", &ch);

        switch (ch)
        {
            case 1:
                insert();
                break;

            case 2:
                if (root == NULL)
                    printf("Tree is empty");
                else
                    preorder(root);
                break;

            case 3:
                if (root == NULL)
                    printf("Tree is empty");
                else
                    postorder(root);
                break;

            case 4:
                if (root == NULL)
                    printf("Tree is empty");
                else
                    inorder(root);
                break;

            case 5:
                if (root == NULL)
                    printf("Tree is empty");
                else
                    delete();
                break;

            case 6:
                exit(0);

            default:
                printf("Wrong Choice");
        }

    } while (1);

    return 0;
}
