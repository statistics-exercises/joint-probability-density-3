import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_plot(self) :
          mypx = sy.integrate( k*(x**2*y**2 + x*y**3),(y,0,3) )
          self.assertTrue( px==mypx, "you have evaluated px wrongly" )
          mypy = sy.integrate( k*(x**2*y**2 + x*y**3),(x,1,2) )
          self.assertTrue( py==mypy, "you have evaluated py wrongly" )
