def test_function():
    def inner_function():
        print('Я в области вдимости функции test_function')

    inner_function()
test_function()
inner_function()



