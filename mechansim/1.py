exec_code = compile("""
                    s = "hello"

                    def func():
                    print(s)

                    func()
                    """, "", "exec")
print(exec_code)
