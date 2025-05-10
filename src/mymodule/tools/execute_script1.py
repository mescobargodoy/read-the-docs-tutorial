import argparse
from mymodule.script1 import line

def main():
    parser = argparse.ArgumentParser(
        usage = """compute-line \\
            --m 2 \\
            --x 3 \\
            --b 0 \\
            --particle_type <particle>
            [OPTIONS]
            """,
        description="""Computes linear equation for given
                        slope, intercept and x-value."""
        )
    parser.add_argument(
        "--m",
        default=1,
        help="slope"
    )
    parser.add_argument(
        "--x",
        default=1,
        help="indepdendent variable"
    )
    parser.add_argument(
        "--b",
        default=0,
        help="intercept"
    )

    args = parser.parse_args()

    return line(args.m, args.x, args.m)

if __name__ == "__main__":
    main()