# a2test.py
# Walker White (wmw2)
# September 20, 2015
""" Unit Test for Assignment A2

This module shows off what a good unit test for a2 should look like"""
import cornelltest
import colormodel
import a2


def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a2.complement_rgb(colormodel.RGB(250, 0, 71)))
    cornelltest.assert_equals(colormodel.RGB(255-92, 255-128, 255-255),
                              a2.complement_rgb(colormodel.RGB(92, 128, 255)))
    
    # Make sure we are not modifying the color
    rgb = colormodel.RGB(128,128,128)
    cornelltest.assert_not_equals(id(rgb),id(a2.complement_rgb(rgb)))


def test_round():
    """Test function round (a2 version)"""
    cornelltest.assert_equals(130.6,   a2.round(130.59,1))
    cornelltest.assert_equals(130.5,   a2.round(130.54,1))
    cornelltest.assert_equals(100.0,   a2.round(100,1))
    cornelltest.assert_equals(100.6,   a2.round(100.55,1))
    cornelltest.assert_equals(99.57,   a2.round(99.566,2))
    cornelltest.assert_equals(99.99,   a2.round(99.99,2))
    cornelltest.assert_equals(100.00,  a2.round(99.995,2))
    cornelltest.assert_equals(22.00,   a2.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a2.round(21.994,2))
    cornelltest.assert_equals(10.01,   a2.round(10.013567,2))
    cornelltest.assert_equals(10.00,   a2.round(10.000000005,2))
    cornelltest.assert_equals(10.00,   a2.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a2.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a2.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a2.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a2.round(.0456,3))
    cornelltest.assert_equals(0.045,   a2.round(.0453,3))
    cornelltest.assert_equals(0.006,   a2.round(.0056,3))
    cornelltest.assert_equals(0.001,   a2.round(.0013,3))
    cornelltest.assert_equals(0.000,   a2.round(.0004,3))
    cornelltest.assert_equals(0.001,   a2.round(.0009999,3))


def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a2.str5(130.59))
    cornelltest.assert_equals('130.5',  a2.str5(130.54))
    cornelltest.assert_equals('100.0',  a2.str5(100))
    cornelltest.assert_equals('100.6',  a2.str5(100.55))
    cornelltest.assert_equals('99.57',  a2.str5(99.566))
    cornelltest.assert_equals('99.99',  a2.str5(99.99))
    cornelltest.assert_equals('100.0',  a2.str5(99.995))
    cornelltest.assert_equals('22.00',  a2.str5(21.99575))
    cornelltest.assert_equals('21.99',  a2.str5(21.994))
    cornelltest.assert_equals('10.01',  a2.str5(10.013567))
    cornelltest.assert_equals('10.00',  a2.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a2.str5(9.9999))
    cornelltest.assert_equals('9.999',  a2.str5(9.9993))
    cornelltest.assert_equals('1.355',  a2.str5(1.3546))
    cornelltest.assert_equals('1.354',  a2.str5(1.3544))
    cornelltest.assert_equals('0.046',  a2.str5(.0456))
    cornelltest.assert_equals('0.045',  a2.str5(.0453))
    cornelltest.assert_equals('0.006',  a2.str5(.0056))
    cornelltest.assert_equals('0.001',  a2.str5(.0013))
    cornelltest.assert_equals('0.000',  a2.str5(.0004))
    cornelltest.assert_equals('0.001',  a2.str5(.0009999))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a2.str5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 1.0)))
    cornelltest.assert_equals('(0.000, 20.03, 65.42, 100.0)',
                              a2.str5_cmyk(colormodel.CMYK(0.0, 20.03, 65.42, 100.000)))
    cornelltest.assert_equals('(0.000, 0.234, 1.000)',
                              a2.str5_hsv(colormodel.HSV(0.0, 0.2345, 1.000)))
    cornelltest.assert_equals('(350.0, 0.350, 0.856)',
                              a2.str5_hsv(colormodel.HSV(350.0, 0.35, 0.85632)))
    
    
def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a2.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a2.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a2.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a2.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a2.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a2.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a2.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a2.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a2.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a2.str5(cmyk.black))
    
    rgb = colormodel.RGB(10, 100, 200);
    cmyk = a2.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('95.00', a2.str5(cmyk.cyan))
    cornelltest.assert_equals('50.00', a2.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a2.str5(cmyk.yellow))
    cornelltest.assert_equals('21.57', a2.str5(cmyk.black))
    
    rgb = colormodel.RGB(210, 170, 53);
    cmyk = a2.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a2.str5(cmyk.cyan))
    cornelltest.assert_equals('19.05', a2.str5(cmyk.magenta))
    cornelltest.assert_equals('74.76', a2.str5(cmyk.yellow))
    cornelltest.assert_equals('17.65', a2.str5(cmyk.black))        


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk= colormodel.CMYK(100, 100, 100, 100)
    rgb= a2.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    cmyk= colormodel.CMYK(35, 38, 65, 0)
    rgb= a2.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(166, rgb.red)
    cornelltest.assert_equals(158, rgb.green)
    cornelltest.assert_equals(89, rgb.blue)

    cmyk= colormodel.CMYK(0, 0, 0, 0)
    rgb= a2.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    cmyk= colormodel.CMYK(0, 47, 88, 99)
    rgb= a2.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(3, rgb.red)
    cornelltest.assert_equals(1, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    rgb = colormodel.RGB(201, 201, 201)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a2.str5(hsv.saturation))
    cornelltest.assert_equals('0.788', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 201, 121)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('35.82', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.525', a2.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 25, 121)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('335.0', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.902', a2.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(146, 255, 146)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('120.0', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.427', a2.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a2.str5(hsv.value))
        
    rgb = colormodel.RGB(146, 20, 214)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('279.0', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.907', a2.str5(hsv.saturation))
    cornelltest.assert_equals('0.839', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(0, 0, 0)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('0.000', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a2.str5(hsv.saturation))
    cornelltest.assert_equals('0.000', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 100, 0)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('23.53', a2.str5(hsv.hue))
    cornelltest.assert_equals('1.000', a2.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 0, 100)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('336.5', a2.str5(hsv.hue))
    cornelltest.assert_equals('1.000', a2.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a2.str5(hsv.value))
    
    rgb = colormodel.RGB(50, 200, 150)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('160.0', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.750', a2.str5(hsv.saturation))
    cornelltest.assert_equals('0.784', a2.str5(hsv.value))
        
    rgb = colormodel.RGB(100, 200, 230)
    hsv = a2.rgb_to_hsv(rgb)
    cornelltest.assert_equals('193.8', a2.str5(hsv.hue))
    cornelltest.assert_equals('0.565', a2.str5(hsv.saturation))
    cornelltest.assert_equals('0.902', a2.str5(hsv.value))


def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    hsv = colormodel.HSV(40, .72, .78)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(199, rgb.red)
    cornelltest.assert_equals(151, rgb.green)
    cornelltest.assert_equals(56,  rgb.blue)
    
    hsv = colormodel.HSV(70.9, .718, .78)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(173, rgb.red)
    cornelltest.assert_equals(199, rgb.green)
    cornelltest.assert_equals(56,  rgb.blue)
    
    hsv = colormodel.HSV(120, .42, 1)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(148, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(148, rgb.blue)
    
    hsv = colormodel.HSV(195.5, .42, .89)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(132, rgb.red)
    cornelltest.assert_equals(202, rgb.green)
    cornelltest.assert_equals(227, rgb.blue)
    
    hsv = colormodel.HSV(262.2, .9, .36)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(40, rgb.red)
    cornelltest.assert_equals(9,  rgb.green)
    cornelltest.assert_equals(92, rgb.blue)
    
    hsv = colormodel.HSV(339.9, .9, 1)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(25,  rgb.green)
    cornelltest.assert_equals(102, rgb.blue)

    hsv = colormodel.HSV(20, .23, .45)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(115, rgb.red)
    cornelltest.assert_equals(97, rgb.green)
    cornelltest.assert_equals(88,  rgb.blue)
    
    hsv = colormodel.HSV(82.51, .693, .457)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(86, rgb.red)
    cornelltest.assert_equals(117, rgb.green)
    cornelltest.assert_equals(36,  rgb.blue)
    
    hsv = colormodel.HSV(130, 0, 1)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    hsv = colormodel.HSV(200.3, 1, .89)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(150, rgb.green)
    cornelltest.assert_equals(227, rgb.blue)
    
    hsv = colormodel.HSV(250.2, .7, .53)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(57, rgb.red)
    cornelltest.assert_equals(41,  rgb.green)
    cornelltest.assert_equals(135, rgb.blue)
    
    hsv = colormodel.HSV(340, .5, .5)
    rgb = a2.hsv_to_rgb(hsv)
    cornelltest.assert_equals(128, rgb.red)
    cornelltest.assert_equals(64,  rgb.green)
    cornelltest.assert_equals(85, rgb.blue)    


def test_to_float_list():
    """Test conversion function to_float_list"""
    seq = ['1.0', '2.2', '3.5']
    lst = a2.to_float_list(seq)
    cornelltest.assert_floats_equal(1.0, lst[0])
    cornelltest.assert_floats_equal(2.2, lst[1])
    cornelltest.assert_floats_equal(3.5, lst[2])
    
    seq = ['2.2', '3.5']
    lst = a2.to_float_list(seq)
    cornelltest.assert_floats_equal(2.2, lst[0])
    cornelltest.assert_floats_equal(3.5, lst[1])
    
    seq = ['1.0', '2.2', '3.5', '-7.5']
    lst = a2.to_float_list(seq)
    cornelltest.assert_floats_equal(1.0, lst[0])
    cornelltest.assert_floats_equal(2.2, lst[1])
    cornelltest.assert_floats_equal(3.5, lst[2])
    cornelltest.assert_floats_equal(-7.5, lst[3])


def test_file_to_data():
    """Test file function file_to_data"""
    file = 'colorblind/normal.dat'
    data = a2.file_to_data(file)
    cornelltest.assert_equals('Normal',data[0])
    cornelltest.assert_float_lists_equal([1,0,0],data[1])
    cornelltest.assert_float_lists_equal([0,1,0],data[2])
    cornelltest.assert_float_lists_equal([0,0,1],data[3])
    
    file = 'colorblind/tritanomaly.dat'
    data = a2.file_to_data(file)
    cornelltest.assert_equals('Tritanomaly',data[0])
    cornelltest.assert_float_lists_equal([0.967, 0.033, 0],data[1])
    cornelltest.assert_float_lists_equal([0, 0.733, 0.267],data[2])
    cornelltest.assert_float_lists_equal([0, 0.183, 0.817],data[3])


def test_files_to_dictionary():
    "Test loading function files_to_dictionary"""
    files = ['colorblind/normal.dat','colorblind/tritanomaly.dat']
    maps = a2.files_to_dictionary(files)
    
    cornelltest.assert_equals(2,len(maps))
    cornelltest.assert_true('Normal' in maps)
    cornelltest.assert_true('Tritanomaly' in maps)
    cornelltest.assert_float_lists_equal([1,0,0],maps['Normal'][0])
    cornelltest.assert_float_lists_equal([0,1,0],maps['Normal'][1])
    cornelltest.assert_float_lists_equal([0,0,1],maps['Normal'][2])
    cornelltest.assert_float_lists_equal([0.967, 0.033, 0],maps['Tritanomaly'][0])
    cornelltest.assert_float_lists_equal([0, 0.733, 0.267],maps['Tritanomaly'][1])
    cornelltest.assert_float_lists_equal([0, 0.183, 0.817],maps['Tritanomaly'][2])


# Execute the tests
test_complement()
test_round()
test_str5()
test_str5_color()
test_rgb_to_cmyk()
test_cmyk_to_rgb()
test_rgb_to_hsv()
test_hsv_to_rgb()
test_to_float_list()
test_file_to_data()
test_files_to_dictionary()
print "Module a2 is working correctly"
