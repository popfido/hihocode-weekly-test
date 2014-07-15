#include <stdio.h>
#include <string.h>

typedef struct node{
	char index;
	int childNum;
	struct node *father;
	struct node *child[26];
} Node;

Node* init(char c, Node *elder, int cnum){
	int i;
	Node *n = malloc(sizeof(Node));
	n->index = c;
	n->father = elder;
	n->childNum = cnum;
	for(i=0;i<26;i++){
		n->child[i] = NULL;
	}
	return n;
}

int insert(char *word, Node *root){
	int i,j;
	Node *n = root;
	int word_length = strlen(word);
	for(i=0;i<word_length;i++){
		j = 0;
		while(n->child[j] != NULL && n->child[j]->index != word[i]){
			j++;
		}
		if(n->child[j] == NULL)
			n->child[j] = init(word[i],n,1);
		else
			n->child[j]->childNum += 1;
		n = n->child[j];
	}

}

int clean(char *word, int size){
	int i;
	for(i = 0;i<size;i++)
		word[i] = '\0';
	return 1;
}

int findPrefix(Node *root, char *word){
	int word_length = strlen(word);
	int i,j;
	Node *n = root;
	Node *temp;
	for(i=0;i<word_length;i++){
		j = 0;
		while(n->child[j] != NULL && n->child[j]->index != word[i])
			j++;
		if(n->child[j] == NULL)
			return 0;
		else
			n = n->child[j];
	}
	return n->childNum;
}

int main(){
	int i;
	int dictSize = 0;
	int askNum = 0;
	char *word = malloc(sizeof(char) * 10);
	scanf("%d",&dictSize);
	Node *root = init(0, NULL,0);
	for(i=0;i<dictSize;i++){
		scanf("%s",word);
		insert(word,root);
		clean(word,10);
	}
	scanf("%d",&askNum);
	i = askNum;
	int ans[askNum];
	while(i){
		scanf("%s",word);
		ans[askNum - i] = findPrefix(root,word);
		i--;
	}
	for(i = 0;i < askNum;i++)
		printf("%d\n",ans[i]);

	return 0;
}
