from sieve import main
import cProfile
import io
import pstats
import sys

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        for _ in range(1):
            result = main(sys.argv[1])
    print(result)

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats("main")
    print(s.getvalue())