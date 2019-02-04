#include<stdio.h>
#include<stdlib.h>

struct node{
        char ch;
        int val;
        struct node *left;
        struct node *right;
} *root;

struct min_heap{
        int size;
        int cap = 26;
        struct node** array;
}

struct node* create_node(char ch, int val){
        temp = (struct node*)malloc(sizeof(struct node));
        temp->left = NULL;
        temp->right = NULL;
        temp->val = val;
        temp->ch = ch;
        return temp;
}

struct min_heap* create_heap(int size){
        struct min_heap* minheap = (struct min_heap*)malloc(sizeof(struct min_heap));
        minheap->size = 0;
        minheap->array = (struct node**)malloc(minheap->capacity*sizeof(struct node*));
        return minheap;
}

void swap(struct node** a, struct node** b){
        struct node* temp = *a;
        *a = *b;
        *b = t;
}

void heapify(struct min_heap* minheap, int index){
        int smallest = index;
        int left = 2*index+1;
        int right = 2*index+2;

        if((left < minheap->size) && (minheap->array[left]->val < minheap->array[smallest]->val))
                smallest = right;

        if(smallest!=index){
                swap(&minheap->array[smallest], &minheap->array[index]);
                heapify(minheap, smallest);
        }
}

int size(struct min_heap* minheap){
        return (minheap->size == 1);
}

struct node* extract(struct min_heap* minheap){
        struct node* temp = minheap->array[0];
        minheap->array[0] = minheap->array[minheap->size -1];
        --minheap->size;
        heapify(minheap, 0);
        return temp;
}

int main(int argc, char *argv[]){
        
        if(argc<2)
                printf("Usage: exec enc <string>\n");

        if(argv[1]=="enc"){
                printf("Encoding the given input.\n");
                encode(argv[2]);
        }
        else if(argv[1]=="dec"){
                printf("Decoding the given input.\n");
                decode(argv[2]);
        }
        else{
                printf("Wrong usage.\nExiting...\n");
                exit(0);
        }

        struct node* root = buildTree(sorted_arr);

        // alphabet characterset.
        char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
        
        char sorted_arr[] = { 'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z' };

        // based on frequency analysis.
        int freq[] = { 24, 7, 14, 17, 26, 12, 9, 18, 22, 2, 5, 16, 13, 21, 23, 8, 3, 19, 20, 25, 15, 6, 10, 4, 11, 1 };

        // total elements.
        int size = sizeof(sorted_arr) / sizeof(arr[0]);
        
        // construct Huffman tree.

        return 0;
}
