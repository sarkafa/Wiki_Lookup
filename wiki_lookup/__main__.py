# import sys
from wikilookup import wikilookup

def main():
    """Vyledávání článků na Wikipedii.
    """
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    wikilookup.initialize()


if __name__ == '__main__':
    main()