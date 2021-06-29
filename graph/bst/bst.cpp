
struct bst {
    bst* left;
    bst* right;
    int val;
};

bst* create(int v) {
    bst* b = new bst();
    b->val = v;
    return b;
}

void add(bst* b, int v) {  // b must be non-empty
    if(v < b->val)
        if(!(b->left))
            b->left = create(v);
        else
            add(b->left, v);
    else if(!(b->right))
            b->right = create(v);
        else
            add(b->right, v);
}

void rm(bst* b, int v) {
    if(v == b->val) {
        bst* b1 = b->left;
        if(!b1)
            *b = *(b->right);
        else {
            while(b1->right)
                b1 = b1->right;
            b1->right = b->right;
            *b = *b1;
        }
    }
    else if(v < b->val) 
        rm(b->left, v);
    else
        rm(b->right, v);
}

int main() {
    bst* b = create(6);
    add(b, 8);
    add(b, 2);
    add(b, 5);
    add(b, 7);
    add(b, 9);
    rm(b, 8);
    rm(b, 6);
    rm(b, 9);
    rm(b, 5);
}