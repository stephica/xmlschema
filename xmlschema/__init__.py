# -*- coding: utf-8 -*-
#
# Copyright (c), 2016, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
from .core import set_logger
from .exceptions import XMLSchemaException
from .etree import etree_to_dict, element_to_dict
from .schema import validate, to_dict, XMLSchema, XMLSchema_v1_0

__version__ = '0.8b3'
__author__ = "Davide Brunato"
__contact__ = "brunato@sissa.it"
__copyright__ = "Copyright 2016, SISSA"
__license__ = "MIT"
__status__ = "Development"

set_logger(__name__)
