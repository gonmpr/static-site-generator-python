
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""

        props_str = ""
        for key in self.props:
            props_str += f' {key}="{self.props[key]}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode(tag= {self.tag}, value= {self.value},children={self.children}, props= {self.props})"


# Has no children parameter
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):

        if self.value == None:
            raise ValueError("Not valid value for a LeafNode Object")
        if self.tag == None:
            return self.value

        return f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"



# Has no value parameter
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag ==  None:
            raise ValueError("Tag parameter cant be None to use this method in ParentNode Object")
        if self.children == None:
            raise ValueError("Value parameter cant be None to use this method in ParentNode Object")

        if not isinstance(self.children, list):
            raise ValueError("children parameter must be a list instance")



        childrens = self.children.copy()

        def add_childrens(childrens):
            if len(childrens) == 0:
                return ''
            return childrens[0].to_html() + add_childrens(childrens[1:])

        return f"<{self.tag}>{add_childrens(childrens)}</{self.tag}>"








