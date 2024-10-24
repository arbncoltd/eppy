# Copyright (c) 2012 Santosh Philip
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================

"""just read the idf file"""
from __future__ import absolute_import, division, print_function, unicode_literals

import eppy.EPlusInterfaceFunctions.eplusdata as eplusdata
import eppy.EPlusInterfaceFunctions.iddgroups as iddgroups
import eppy.EPlusInterfaceFunctions.parse_idd as parse_idd
from eppy.EPlusInterfaceFunctions import iddindex

# from EPlusInterfaceFunctions import parse_idd
# from EPlusInterfaceFunctions import eplusdata


def readidf(idfname):
    """read the idf file"""
    # iddfile = sys.path[0] + '/EplusCode/Energy+.idd'
    iddfile = "Energy+.idd"
    # iddfile = './EPlusInterfaceFunctions/E1.idd' # TODO : can the path name be not hard coded
    iddtxt = open(iddfile, "r").read()
    block, commlst, commdct = parse_idd.extractidddata(iddfile)

    theidd = eplusdata.Idd(block, 2)
    data = eplusdata.Eplusdata(theidd, idfname)
    return data


def readiddidf(idfname):
    """read the idf file"""
    # iddfile = sys.path[0] + '/EplusCode/Energy+.idd'
    iddfile = "Energy+.idd"
    # iddfile = './EPlusInterfaceFunctions/E1.idd' # TODO : can the path name be not hard coded
    iddtxt = open(iddfile, "r").read()
    block, commlst, commdct = parse_idd.extractidddata(iddfile)

    theidd = eplusdata.Idd(block, 2)
    data = eplusdata.Eplusdata(theidd, idfname)
    return theidd, data


def readiddstuff(idfname):
    """read the idf file"""
    # iddfile = sys.path[0] + '/EplusCode/Energy+.idd'
    iddfile = "Energy+.idd"
    # iddfile = './EPlusInterfaceFunctions/E1.idd' # TODO : can the path name be not hard coded
    iddtxt = open(iddfile, "r").read()
    block, commlst, commdct = parse_idd.extractidddata(iddfile)

    theidd = eplusdata.Idd(block, 2)
    data = eplusdata.Eplusdata(theidd, idfname)
    return block, commlst, commdct


def readdatacommlst(idfname):
    """read the idf file"""
    # iddfile = sys.path[0] + '/EplusCode/Energy+.idd'
    iddfile = "Energy+.idd"
    # iddfile = './EPlusInterfaceFunctions/E1.idd' # TODO : can the path name be not hard coded
    iddtxt = open(iddfile, "r").read()
    block, commlst, commdct = parse_idd.extractidddata(iddfile)

    theidd = eplusdata.Idd(block, 2)
    data = eplusdata.Eplusdata(theidd, idfname)
    return data, commlst


def readdatacommdct(idfname, iddfile="Energy+.idd", commdct=None):
    """read the idf file"""
    if not commdct:
        block, commlst, commdct, idd_index = parse_idd.extractidddata(iddfile)
        theidd = eplusdata.Idd(block, 2)
    else:
        theidd = iddfile
    data = eplusdata.Eplusdata(theidd, idfname)
    return data, commdct, idd_index


def readdatacommdct1(idfname, iddfile="Energy+.idd", commdct=None, block=None):
    """read the idf file"""
    if not commdct:
        block, commlst, commdct, idd_index = parse_idd.extractidddata(iddfile)
        theidd = eplusdata.Idd(block, 2)
    else:
        theidd = eplusdata.Idd(block, 2)
        name2refs = iddindex.makename2refdct(commdct)
        ref2namesdct = iddindex.makeref2namesdct(name2refs)
        idd_index = dict(name2refs=name2refs, ref2names=ref2namesdct)
        updated_commdct = iddindex.ref2names2commdct(ref2namesdct, commdct)
    data = eplusdata.Eplusdata(theidd, idfname)
    return block, data, commdct, idd_index
