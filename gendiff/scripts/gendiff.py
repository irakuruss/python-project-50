#!/usr/bin/env python3
from gendiff.parse_args import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()