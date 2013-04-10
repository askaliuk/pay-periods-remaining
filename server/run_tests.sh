# Run specific test module
# python -m unittest server.test.test_simple
# Run specific test method
# python -m unittest server.test.test_simple.TestSimple.test_simple
# Run all tests
python -m unittest discover -s ./test -t . -v