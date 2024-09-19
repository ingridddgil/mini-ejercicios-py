try:
    f = open('test_file.txt')
    if f.name == 'file_text.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Unavailable")
else:
    print(f.read())
    f.close()
finally:
    print("Executed already")