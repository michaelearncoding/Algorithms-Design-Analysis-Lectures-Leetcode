#include <iostream>

// Your existing code
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* findFromEnd(ListNode* head, int k) {
    ListNode* p1 = head;
    for (int i = 0; i < k; i++) {
        p1 = p1->next;
    }
    ListNode* p2 = head;
    while (p1 != nullptr) {
        p2 = p2->next;
        p1 = p1->next;
    }
    return p2;
}

// Main function to test the findFromEnd function
int main() {
    // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    // Find the 2nd node from the end
    ListNode* result = findFromEnd(head, 2);
    if (result != nullptr) {
        std::cout << "The value of the 2nd node from the end is: " << result->val << std::endl;
    } else {
        std::cout << "The list is shorter than 2 nodes." << std::endl;
    }

    // Clean up the allocated memory
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}