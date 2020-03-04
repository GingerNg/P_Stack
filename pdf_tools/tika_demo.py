from tika import parser


def tika_parse(org_full_path):
    parsed = parser.from_file(org_full_path, "http://localhost:9998/")
    return parsed["content"] if "content" in parsed else ""


if __name__ == '__main__':
    content = tika_parse("./cases/report123.pdf")
    print(content)
    open("./cases/report123.txt","w").write(content)

