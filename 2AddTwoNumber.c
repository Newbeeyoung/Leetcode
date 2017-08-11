/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *node1=l1;
    struct ListNode *node2=l2;
    
    while((node1!=NULL)||(node2!=NULL)){
      
        node1->val+=node2->val;
        if((node1->val)>=10){
            if(node1->next==NULL){
                node1->next=malloc(sizeof(struct ListNode));
                node1->next->val=0;
                node1->next->next=NULL;
            }
            node1->val-=10;
            node1->next->val+=1;
        }
        if((node1->next==NULL)&&(node2->next!=NULL)){
            node1->next=malloc(sizeof(struct ListNode));
            node1->next->val=0;
            node1->next->next=NULL;
        }
        if((node2->next==NULL)&&(node1->next!=NULL)){
            node2->next=malloc(sizeof(struct ListNode));
            node2->next->val=0;
            node2->next->next=NULL;
        }
        node1=node1->next;
        node2=node2->next;
    }
    return l1;
}
