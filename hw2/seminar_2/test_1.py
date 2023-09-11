from lib_checkout import checkout

folder_tst = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"

#cd /home/user/tst; 7z a ../out/arx2 test_file.txt

def test_1():
    # test1
    res1 = checkout(f"cd {folder_tst}; 7z a ../out/arx2 test_file.txt", "Everything is Ok")
    res2 = checkout(f"ls {folder_out}; ", "arx2.7z")
    assert res1 and res2, "test 1 FAIL"


def test_2():
    # test2

    res1 = checkout(f"cd {folder_out}; 7z e arx2.7z -o{folder_ext}", "Everything is Ok")
    res2 = checkout(f"ls {folder_ext}; ", "test_file.txt")
    assert res1 and res2, "test 2 FAIL"


def test_3():
    # test3
    assert checkout(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test 3 FAIL"


#def test_4():
#    # test3
#    assert checkout(f"cd {folder_out}; 7z u arx2.7z", "Everything is Ok"), "test 4 FAIL"
#
#
#def test_5():
#    # test3
#    assert checkout(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test 5 FAIL"
#