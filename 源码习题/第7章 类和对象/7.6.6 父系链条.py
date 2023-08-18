class TreeNode:
    def __init__(self,treeNodeData=''):
        self.data =treeNodeData #数据
        self.deep = 0 #深度
        self.__children = [] #下级节点集合
        self.parent = None #父节点

    def print(self):
        print('  '* self.deep + self.data)
        for subTreeNode in self.children:
                TreeNode.print(subTreeNode) #调用递归函数    

    def parents(self):
        if self.parent is None:
            return []
        return TreeNode.parents(self.parent) + [self.parent]

    def tree_print(self):
        #以下代码画出制表线，根节点即parent为空，不需要制表符
        if self.parent:        
            lines = '' 
            #以下画出这个节点上层节点的制表符
            for node in self.parents():
                if node.parent is not None:
                    if node !=node.parent.children[-1]:
                        lines += '│ ' 
                    else:
                        lines += '  '
            #以下画出这个紧邻节点前的制表符
            if self.parent.children[-1]==self: 
                #如果当前打印的节点已经是同级最后一个节点，线条就不向下延伸
                lines += '└─' 
            else:
                lines += '├─' #默认还可以向下延伸
            print(lines ,end ='')
        print(self.data) #打印出数据
        #如果存在子节点，那么就递归打印
        for subTreeNode in self.__children:
            TreeNode.tree_print(subTreeNode) #调用递归函数
    
    @property
    def children(self):
        return self.__children

    def add(self,subTreeNode):
        #这是一个判断对象是否某个类的实例
        assert isinstance(subTreeNode,TreeNode)
        #子结点的深度是上级节点+1
        subTreeNode.deep = self.deep +1 
        #子结点的父节点是上级节点
        subTreeNode.parent = self
        #防止递归的时候，重复把节点加入列表
        if subTreeNode not in  self.__children:
            self.__children.append(subTreeNode)
        #下面通过枚举，把所有子节点的deep值重新进行更新
        for node in subTreeNode.children:
            TreeNode.add(subTreeNode,node)
        return subTreeNode


HenryTreeNode =  TreeNode('Henry')
JoeTreeNode =TreeNode('Joe')
HenryTreeNode.add(JoeTreeNode)
man = JoeTreeNode.add(TreeNode("Joe's man1"))
print("man's parents:")
for m in man.parents():
    print(m.data)
print("Joe's parents:")
for m in JoeTreeNode.parents():
    print(m.data)
