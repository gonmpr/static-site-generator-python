
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
            props_str += f" {key}={self.props[key]}"
        return props_str

    def __repr__(self):
        return f"HTMLNode(tag= {self.tag}, value= {self.value},children={self.children}, props= {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):

        if self.value == None:
            raise ValueError("Not valid value for a LeafNode Object")
        if self.tag == None:
            return self.value

        return f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"
