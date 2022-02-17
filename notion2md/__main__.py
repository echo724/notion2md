import sys


sys.path.append("../notion2md")

if __name__ == "__main__":
    from .console import application

    sys.exit(application.main())
