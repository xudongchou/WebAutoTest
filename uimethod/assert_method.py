from unittest import TestCase
from .helpers import Logger
class Assert(TestCase):
    def assert_Equal(self,first,second,msg=None):

        try:
            self.assertEqual(first=first, second=second)
            Logger.logger.info(str(first) + "等于" +str(second))
        except AssertionError:
            Logger.logger.info(str(first) + "不等于" + str(second))
    def assert_NotEqual(self,first,second,msg=None):
        try:
            self.assertNotEqual(first=first, second=second)
            Logger.logger.info(str(first)+"不等于"+str(second))
        except AssertionError:
            Logger.logger.info(str(first)+"等于"+str(second))
    def assert_True(self,exp,msg=None):
        try:
            self.assertTrue(expr=exp)
            Logger.logger.info(str(exp)+"为真")
        except AssertionError:
            Logger.logger.info(str(exp)+"为假")


    def assert_False(self, exp, msg=None):
        try:
            self.assertFalse(expr=exp)
            Logger.logger.info(str(exp)+"成立")
        except AssertionError:
            Logger.logger.info(str(exp)+"不成立")
    def assert_In(self,member,container,msg=None):
        try:
            self.assertIn(member=member,container=container)
            Logger.logger.info(str(container)+"包含"+str(member))
        except AssertionError:
            Logger.logger.info(str(container)+"不包含"+str(member))
    def assert_NotIn(self,member,container,msg=None):
        try:
            self.assertNotIn(member=member,container=container)
            Logger.logger.info(str(container)+"不包含"+str(member))
        except AssertionError:
            Logger.logger.info(str(container)+"包含"+str(member))
    def assert_DictEqual(self,dict1,dict2,msg=None):
        try:
            self.assertDictEqual(d1=dict1,d2=dict2)
            Logger.logger.info(str(dict1)+"等于"+str(dict2))
        except:
            Logger.logger.info(str(dict1)+"不等于"+str(dict2))
    def assert_DictContainsSubset(self,subset,dict1,msg=None):
        try:
            self.assertDictContainsSubset(subset=subset,dictionary=dict1)
            Logger.logger.info(str(dict1)+"包含"+str(subset))
        except AssertionError:
            Logger.logger.info(str(dict1)+"不包含"+str(subset))
    def assert_IsNone(self,obj,msg=None):
        try:
            self.assertIsNone(obj=obj)
            Logger.logger.info(str(obj) + "不存在")
        except AssertionError:
            Logger.logger.info(str(obj)+"存在")
