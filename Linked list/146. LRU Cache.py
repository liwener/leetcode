"""
要让 put 和 get 方法的时间复杂度为 O(1)，我们可以总结出 cache 这个数据结构必要的条件：查找快，插入快，删除快，有顺序之分。

因为显然 cache 必须有顺序之分，以区分最近使用的和久未使用的数据；而且我们要在 cache 中查找键是否已存在；如果容量满了要删除最后一个数据；每次访问还要把数据插入到队头。

那么，什么数据结构同时符合上述条件呢？哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。
删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱。所以结合一下，形成一种新的数据结构：哈希链表。

在双向链表实现中，这里使用一个伪头部和伪尾部标记界限，这样在更新的时候就不需要检查是否是 null 节点。

为什么要在链表中同时存储 key 和 val，而不是只存储 val：
当缓存容量已满，我们不仅仅要删除最后一个 Node 节点，还要把 map 中映射到该节点的 key 同时删除，而这个 key 只能由 Node 得到。
如果 Node 结构中只存储 val，那么我们就无法得知 key 是什么，就无法删除 map 中的键，造成错误。

"""


class DlinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    # 在头节点后添加新节点
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除存在的节点
    def _remove_node(self, node):
        prev = node.prev
        back = node.next

        prev.next = back
        back.prev = prev

    # 将节点移动到头部
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    # 删除结尾节点之前的节点
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        # 字典
        self.cache = {}
        self.size = 0
        self.capacity = capacity

        # 建立双向链表
        self.head, self.tail = DlinkedNode(), DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 获取数据
    def get(self, key: int) -> int:
        # 返回指定键的值，如果值不在字典中，返回default值
        node = self.cache.get(key, None)
        if not node:
            return -1

        # 将访问的节点放到开头
        self._move_to_head(node)
        return node.value

    # 写入数据
    def put(self, key: int, value: int) -> None:
        # get返回指定键的值，如果值不在字典中返回default值
        node = self.cache.get(key)

        if not node:
            newNode = DlinkedNode()
            newNode.key = key   # 在链表中存储 key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)