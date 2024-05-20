

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else [] 
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be overidden by subclasses")
    
    def props_to_html(self):
        if not self.props:
            return ""
        attributes = []
        for key, value in self.props.items():
            attributes.append(f' {key}="{value}"')
        return "".join(attributes)
    
    def __repr__(self):
        children_count = len(self.children) if self.children else 0
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={children_count}, props={self.props})"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value=value, props=None)
        if value is None:
            raise ValueError("LeafNode must have a value")
    
    def to_html(self):
        if not self.tag:
            return self.value
        
        # Otherwise, contruct the HTML tag string
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        if not self.tag:
            raise ValueError("no tag value")
        if not self.children:
            raise ValueError("no children value")

        self.tag = tag
        self.children = children
        
    def to_html(self):
        if not self.tag:
            raise ValueError("no tag value")
        if not self.children:
            raise ValueError("no children value")
        
        children_html = ''.join(child.to_html() for  child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"