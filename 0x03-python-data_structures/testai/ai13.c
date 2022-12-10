#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// Node structure for a singly-linked list
struct Node {
  int data;
  struct Node* next;
};

// Function that returns true if the given linked list is a palindrome,
// otherwise it returns false
bool isPalindrome(struct Node* head) {
  // Use slow and fast pointers to find the middle of the list
  struct Node* slow = head;
  struct Node* fast = head;
  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }

  // If the list has an odd number of elements, skip the middle element
  if (fast) {
    slow = slow->next;
  }

  // Reverse the second half of the list
  struct Node* prev = NULL;
  while (slow) {
    struct Node* next = slow->next;
    slow->next = prev;
    prev = slow;
    slow = next;
  }

  // Compare the nodes from the first half of the original list with the
  // nodes from the second half of the reversed list. If any node doesn't
  // match, the given linked list is not a palindrome
  struct Node* curr = head;
  slow = prev;
  while (curr && slow) {
    if (curr->data != slow->data) {
      return false;
    }
    curr = curr->next;
    slow = slow->next;
  }

  return true;
}

// Function to create a new node with the given data and link the current node to it
struct Node* push(struct Node* head, int data) {
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = head;
  head = newNode;
  return head;
}

// Function to print the linked list
void printList(struct Node* head) {
  while (head) {
    printf("%d ", head->data);
    head = head->next;
  }
  printf("\n");
}

// main function
int main(void) {
  clock_t t;
  t = clock();  
  struct Node* head = NULL;

  // create a linked list 1->2->3->2->1
  head = push(head, 1);
  head = push(head, 2);
  head = push(head, 3);
  head = push(head, 2);
  head = push(head, 1);

  printf("Linked list: ");
  printList(head);

  if (isPalindrome(head)) {
    printf("The given linked list is a palindrome\n");
}
   t = clock() - t;
        double time_taken = ((double)t)/CLOCKS_PER_SEC;
        printf("t: %f secs\n", time_taken);
  return 0;
}
