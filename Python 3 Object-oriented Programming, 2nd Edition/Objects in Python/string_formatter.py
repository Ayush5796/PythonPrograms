def format_string(string, formatter=None):
    '''Format a String using formatter object, which 
    is expected to have a format() method that accepts the string'''
    class DefaultFormatter:
        '''Format a string in title case'''
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

hello_world = "hello world, how are you?"
print("input: " + hello_world)  
print("output: " + format_string(hello_world))      