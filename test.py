import cppimport
nokia = cppimport.imp("nokia")

nokia.LCDInit(14, 12, 5, 10, 4, 50)
nokia.LCDclear()
nokia.LCDdrawChar(1, 0, 'A', 0, 0)
nokia.LCDdisplay()