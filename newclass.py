templete = """
#ifndef ___HEADER_DEFINE
#define ___HEADER_DEFINE
___NAMESPACE_BEGIN

class  ___CLASSNAME {
public:
    ___CLASSNAME();
    ~___CLASSNAME();
private:
    ___CLASSNAME(const ___CLASSNAME&);
    ___CLASSNAME& operator=(const ___CLASSNAME&);
};

___NAMESPACE_END
#endif
"""

import sys

def echo_use_help():
    print "use python newclass.py a.b.c.ClassName"


def get_space(num):
    result = ""
    i = 0
    while i < num:
        result = result + " "
        i = i + 1
    return result

def get_header_content(namespace):
    namespace_vec = namespace.split(".")
    class_name = namespace_vec[-1]
    namespace_vec = namespace_vec[0:-1]

    content = ""
    define_content = ""

    for key in namespace_vec:
        define_content = define_content + key.upper() + "_";
    define_content = define_content + class_name.upper();

    namespace_begin_content = "";
    namespace_end_content = "";

    index = 0
    size = len(namespace_vec)
    while (index < size):
        namespace_begin_content = namespace_begin_content +  "namespace " + namespace_vec[index] + " {\n"
        namespace_end_content =  "} " + namespace_end_content
        index = index + 1
    if len(namespace_begin_content) != 0:
        namespace_begin_content = namespace_begin_content[0:-1]
    doc = templete.replace("___HEADER_DEFINE", define_content)
    doc = doc.replace("___CLASSNAME", class_name)
    doc = doc.replace("___NAMESPACE_BEGIN", namespace_begin_content)
    doc = doc.replace("___NAMESPACE_END", namespace_end_content)
    print doc


if __name__ == "__main__":
    if len(sys.argv) != 2:
        echo_use_help()
        exit(-1)
    class_name = sys.argv[1]
    get_header_content(class_name)
