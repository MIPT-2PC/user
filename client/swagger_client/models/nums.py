# coding: utf-8

"""
    Preprocessor server

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mipt@mipt.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Nums(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'num1': 'float',
        'num2': 'float',
        'operation': 'str'
    }

    attribute_map = {
        'num1': 'num1',
        'num2': 'num2',
        'operation': 'operation'
    }

    def __init__(self, num1=None, num2=None, operation=None):  # noqa: E501
        """Nums - a model defined in Swagger"""  # noqa: E501
        self._num1 = None
        self._num2 = None
        self._operation = None
        self.discriminator = None
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    @property
    def num1(self):
        """Gets the num1 of this Nums.  # noqa: E501


        :return: The num1 of this Nums.  # noqa: E501
        :rtype: float
        """
        return self._num1

    @num1.setter
    def num1(self, num1):
        """Sets the num1 of this Nums.


        :param num1: The num1 of this Nums.  # noqa: E501
        :type: float
        """
        if num1 is None:
            raise ValueError("Invalid value for `num1`, must not be `None`")  # noqa: E501

        self._num1 = num1

    @property
    def num2(self):
        """Gets the num2 of this Nums.  # noqa: E501


        :return: The num2 of this Nums.  # noqa: E501
        :rtype: float
        """
        return self._num2

    @num2.setter
    def num2(self, num2):
        """Sets the num2 of this Nums.


        :param num2: The num2 of this Nums.  # noqa: E501
        :type: float
        """
        if num2 is None:
            raise ValueError("Invalid value for `num2`, must not be `None`")  # noqa: E501

        self._num2 = num2

    @property
    def operation(self):
        """Gets the operation of this Nums.  # noqa: E501

        Types of operations  # noqa: E501

        :return: The operation of this Nums.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Nums.

        Types of operations  # noqa: E501

        :param operation: The operation of this Nums.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["+", "-", "*"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Nums, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Nums):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
