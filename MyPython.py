import itertools
from os import system

def exec_function(user_input):
    try:
        compile(user_input,'<stdin>','eval')
    except SyntaxError:
        return exec
    return eval

def exec_user_input(user_input,user_globals):
    user_globals=user_globals.copy()
    try:
        retval=exec_function(user_input)(user_input,user_globals)
    except Exception as e:
        print("%s:%s"%(e.__class__.__name__,e))
    else:
        if retval is not None:
            print("%s"%(retval))
    return user_globals

def selected_user_globals(user_globals):
    return (
        (key,user_globals[key])
        for key in sorted(user_globals)
        if not key.startswith('__') or not key.endswith('__')           
    )

def save_user_globals(user_globals,path='user_globlas.txt'):
    with open(path,'w') as file:
        for key,value in selected_user_globals(user_globals):
            file.write("%s = %s (%s)\n"%(key,value,value.__class__.__name__))

def main():
    user_globals={}                               #stores all variables used   
    mode="line by line"
    save_user_globals(user_globals)
    while 1:
        if mode=="line by line":
            try:
                user_input=input(">>>")
            except KeyboardInterrupt:
                if mode=="line by line":
                    mode="all"
                    user_input=""
                    print()
                continue
            except EOFError:
                break
            if user_input.lower()=="exit" or user_input.lower()=="quit" or user_input.lower()=="q":
                print("Exiting...")
                break
            elif user_input.lower()=="clear":
                exec("system('cls')")
                continue
            user_globals=exec_user_input(user_input,user_globals)
        else:
            try:
                user_input=user_input+"\n"+input()
            except KeyboardInterrupt:
                try:
                    exec(user_input,user_globals)
                except Exception as e:
                    print("%s:%s"%(e.__class__.__name__,e))
                if mode=="all":
                    mode="line by line"
                    print()
        save_user_globals(user_globals)


if __name__=="__main__":
    main()