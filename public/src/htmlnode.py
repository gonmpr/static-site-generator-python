
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

        props = ""
        for key in props:
            props += f" {key}={self.props[key]}"
        return props

    def __repr__(self):
        return f"HTMLNode(tag= {self.tag}, value= {self.value},children={self.children}, props= {self.props})"



