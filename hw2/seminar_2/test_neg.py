from lib_checkout import checkout_negativ

folder_tst = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"


def test_1_neg():
    # test1
    assert checkout_negativ(f"cd {folder_out}; 7z e arx2bad.7z", "ERROR"), "test_neg 1 FAIL"


def test_2_neg():
    # test2
    assert checkout_negativ(f"cd {folder_out}; 7z t arx2bad.7z", "ERROR"), "test_neg 2 FAIL"