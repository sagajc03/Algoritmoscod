from arbolBi import BinarySearchTree as BST

def testBinarySearchTree():
    bst = BST.BinarySearchTree()
    data = [100,80,105,70,82,104,110,60,84,103,109,50,62,83,86,108,64,85,107]
    print("insert:", data)
    for d in data:
        bst.insert(d)
    print("size:", len(bst))
    print("in-order:", bst.inOrder([]))
    print("pre-order:", bst.preOrder([]))
    print("post-order:", bst.postOrder([]))
    print("level-order:", bst.levelOrder([]))
    print("tree:")
    print(bst)
    print("min:", bst.getMin())
    print("max:", bst.getMax())
    print("exist 25:", bst.exists(25))
    print("exist 33:", bst.exists(33))
    data = [5, 25, 50]
    print("delete:", data)
    for d in data:
        bst.delete(d)
    print("size:", len(bst))
    print("in-order:", bst.inOrder([]))
    print("tree:")
    print(bst)


if __name__ == '__main__':
    testBinarySearchTree()