# LRU（最近最少使用缓存）

## LRU缓存机制

**问题描述**：设计和实现一个满足LRU（最近最少使用）缓存约束的数据结构，它应该支持以下操作：获取数据 get 和写入数据 put，O(1) 时间复杂度

**解法**：双向列表 + map

```cpp
class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        head->before = nullptr;
        tail->before = head;
        tail->next = nullptr;
    }

    int get(int key) {
        if (m[key]) {
            moveHead(m[key]);
            return m[key]->val;
        }
        else return -1;
    }

    void put(int key, int value) {
        Node* now = m[key];
        if (now) {
            now->val = value;
            moveHead(now);
        }
        else {
            if (size < capacity) {
                size++;
                Node* tmp = new Node(key, value);
                m[key] = tmp;
                tmp->next = head->next;
                tmp->before = head;
                head->next->before = tmp;
                head->next = tmp;
            }
            else {
                Node* tmp = tail->before;
                m[tmp->key] = nullptr;
                m[key] = tmp;
                tmp->key = key;
                tmp->val = value;

                moveHead(tmp);
            }
        }
    }

    void moveHead(Node* now) {
        now->before->next = now->next;
        now->next->before = now->before;
        now->next = head->next;
        now->before = head;
        head->next = now;
        now->next->before = now;
    }

    map<int, Node*> m;
    int size = 0;
    int capacity;
    Node* head, * tail;
};
```
