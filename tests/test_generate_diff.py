from gendiff.generate_diff import generate_diff


TEST_FILES = [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result.txt'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'tests/fixtures/result.txt'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/result.txt'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'tests/fixtures/result2.txt'),
    ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml', 'tests/fixtures/result2.txt'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'tests/fixtures/result2.txt'),
]


def test_generate_diff():
    for kit in TEST_FILES:
        file1, file2, result = kit[0], kit[1], kit[2]
        with open(result, 'r') as result_file:
            result_string = "\n".join(result_file.read().splitlines())
            assert generate_diff(file1, file2) == result_string
