#!/data/data/com.termux/files/usr/bin/python3.13
import tom
if __name__ == "__main__":
    if callable(getattr(tom, 'main', None)):
        tom.main()
    else:
        print("tom :", [x for x in dir(tom) if not x.startswith('_')])
