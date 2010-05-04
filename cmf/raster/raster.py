# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _raster.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_raster', [dirname(__file__)])
        except ImportError:
            import _raster
            return _raster
        if fp is not None:
            try:
                _mod = imp.load_module('_raster', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _raster = swig_import_helper()
    del swig_import_helper
else:
    import _raster
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


from math import *

class RasterStatistics(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    min = _swig_property(_raster.RasterStatistics_min_get, _raster.RasterStatistics_min_set)
    max = _swig_property(_raster.RasterStatistics_max_get, _raster.RasterStatistics_max_set)
    mean = _swig_property(_raster.RasterStatistics_mean_get, _raster.RasterStatistics_mean_set)
    stdev = _swig_property(_raster.RasterStatistics_stdev_get, _raster.RasterStatistics_stdev_set)
    count = _swig_property(_raster.RasterStatistics_count_get, _raster.RasterStatistics_count_set)
    def __init__(self): 
        _raster.RasterStatistics_swiginit(self,_raster.new_RasterStatistics())
    __swig_destroy__ = _raster.delete_RasterStatistics
RasterStatistics_swigregister = _raster.RasterStatistics_swigregister
RasterStatistics_swigregister(RasterStatistics)

class Histogram(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _raster.Histogram_swiginit(self,_raster.new_Histogram(*args))
    def __getitem__(self,index):
        if index<0 : index=self.size()+index
        if index<0 or index>=self.size() : raise IndexError("Bar of histogram not available")
        return (self.barcenter(index),self.frequency(index))
    def __len__(self):
        return self.size()

    __swig_destroy__ = _raster.delete_Histogram
Histogram.min = new_instancemethod(_raster.Histogram_min,None,Histogram)
Histogram.max = new_instancemethod(_raster.Histogram_max,None,Histogram)
Histogram.barwidth = new_instancemethod(_raster.Histogram_barwidth,None,Histogram)
Histogram.size = new_instancemethod(_raster.Histogram_size,None,Histogram)
Histogram.sum = new_instancemethod(_raster.Histogram_sum,None,Histogram)
Histogram.frequency = new_instancemethod(_raster.Histogram_frequency,None,Histogram)
Histogram.relfrequency = new_instancemethod(_raster.Histogram_relfrequency,None,Histogram)
Histogram.pos = new_instancemethod(_raster.Histogram_pos,None,Histogram)
Histogram.barcenter = new_instancemethod(_raster.Histogram_barcenter,None,Histogram)
Histogram.quantile = new_instancemethod(_raster.Histogram_quantile,None,Histogram)
Histogram.CountValue = new_instancemethod(_raster.Histogram_CountValue,None,Histogram)
Histogram_swigregister = _raster.Histogram_swigregister
Histogram_swigregister(Histogram)

class double_raster(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _raster.double_raster_swiginit(self,_raster.new_double_raster(*args))
    __swig_destroy__ = _raster.delete_double_raster
double_raster.Xllcorner = new_instancemethod(_raster.double_raster_Xllcorner,None,double_raster)
double_raster.Yllcorner = new_instancemethod(_raster.double_raster_Yllcorner,None,double_raster)
double_raster.XCellsize = new_instancemethod(_raster.double_raster_XCellsize,None,double_raster)
double_raster.YCellsize = new_instancemethod(_raster.double_raster_YCellsize,None,double_raster)
double_raster.ColumnCount = new_instancemethod(_raster.double_raster_ColumnCount,None,double_raster)
double_raster.RowCount = new_instancemethod(_raster.double_raster_RowCount,None,double_raster)
double_raster.Width = new_instancemethod(_raster.double_raster_Width,None,double_raster)
double_raster.Height = new_instancemethod(_raster.double_raster_Height,None,double_raster)
double_raster.NoData = new_instancemethod(_raster.double_raster_NoData,None,double_raster)
double_raster.HasData = new_instancemethod(_raster.double_raster_HasData,None,double_raster)
double_raster.SetData = new_instancemethod(_raster.double_raster_SetData,None,double_raster)
double_raster.GetXPosition = new_instancemethod(_raster.double_raster_GetXPosition,None,double_raster)
double_raster.GetYPosition = new_instancemethod(_raster.double_raster_GetYPosition,None,double_raster)
double_raster.statistics = new_instancemethod(_raster.double_raster_statistics,None,double_raster)
double_raster.histogram = new_instancemethod(_raster.double_raster_histogram,None,double_raster)
double_raster.__imul__ = new_instancemethod(_raster.double_raster___imul__,None,double_raster)
double_raster.__iadd__ = new_instancemethod(_raster.double_raster___iadd__,None,double_raster)
double_raster.__isub__ = new_instancemethod(_raster.double_raster___isub__,None,double_raster)
double_raster.__idiv__ = new_instancemethod(_raster.double_raster___idiv__,None,double_raster)
double_raster.__mul__ = new_instancemethod(_raster.double_raster___mul__,None,double_raster)
double_raster.__add__ = new_instancemethod(_raster.double_raster___add__,None,double_raster)
double_raster.__sub__ = new_instancemethod(_raster.double_raster___sub__,None,double_raster)
double_raster.__div__ = new_instancemethod(_raster.double_raster___div__,None,double_raster)
double_raster.WriteToASCFile = new_instancemethod(_raster.double_raster_WriteToASCFile,None,double_raster)
double_raster.WriteToBinary = new_instancemethod(_raster.double_raster_WriteToBinary,None,double_raster)
double_raster.ToInt = new_instancemethod(_raster.double_raster_ToInt,None,double_raster)
double_raster.ToFloat = new_instancemethod(_raster.double_raster_ToFloat,None,double_raster)
double_raster.ToDouble = new_instancemethod(_raster.double_raster_ToDouble,None,double_raster)
double_raster.adress = new_instancemethod(_raster.double_raster_adress,None,double_raster)
double_raster.focal_min = new_instancemethod(_raster.double_raster_focal_min,None,double_raster)
double_raster.focal_max = new_instancemethod(_raster.double_raster_focal_max,None,double_raster)
double_raster.focal_mean = new_instancemethod(_raster.double_raster_focal_mean,None,double_raster)
double_raster.focal_stdev = new_instancemethod(_raster.double_raster_focal_stdev,None,double_raster)
double_raster.focal_majority = new_instancemethod(_raster.double_raster_focal_majority,None,double_raster)
double_raster.focal_mean_difference = new_instancemethod(_raster.double_raster_focal_mean_difference,None,double_raster)
double_raster.clone = new_instancemethod(_raster.double_raster_clone,None,double_raster)
double_raster.GetData = new_instancemethod(_raster.double_raster_GetData,None,double_raster)
double_raster.ToBuffer = new_instancemethod(_raster.double_raster_ToBuffer,None,double_raster)
double_raster.__radd__ = new_instancemethod(_raster.double_raster___radd__,None,double_raster)
double_raster.__rsub__ = new_instancemethod(_raster.double_raster___rsub__,None,double_raster)
double_raster.__rmul__ = new_instancemethod(_raster.double_raster___rmul__,None,double_raster)
double_raster.__rdiv__ = new_instancemethod(_raster.double_raster___rdiv__,None,double_raster)
double_raster_swigregister = _raster.double_raster_swigregister
double_raster_swigregister(double_raster)

class float_raster(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _raster.float_raster_swiginit(self,_raster.new_float_raster(*args))
    __swig_destroy__ = _raster.delete_float_raster
float_raster.Xllcorner = new_instancemethod(_raster.float_raster_Xllcorner,None,float_raster)
float_raster.Yllcorner = new_instancemethod(_raster.float_raster_Yllcorner,None,float_raster)
float_raster.XCellsize = new_instancemethod(_raster.float_raster_XCellsize,None,float_raster)
float_raster.YCellsize = new_instancemethod(_raster.float_raster_YCellsize,None,float_raster)
float_raster.ColumnCount = new_instancemethod(_raster.float_raster_ColumnCount,None,float_raster)
float_raster.RowCount = new_instancemethod(_raster.float_raster_RowCount,None,float_raster)
float_raster.Width = new_instancemethod(_raster.float_raster_Width,None,float_raster)
float_raster.Height = new_instancemethod(_raster.float_raster_Height,None,float_raster)
float_raster.NoData = new_instancemethod(_raster.float_raster_NoData,None,float_raster)
float_raster.HasData = new_instancemethod(_raster.float_raster_HasData,None,float_raster)
float_raster.SetData = new_instancemethod(_raster.float_raster_SetData,None,float_raster)
float_raster.GetXPosition = new_instancemethod(_raster.float_raster_GetXPosition,None,float_raster)
float_raster.GetYPosition = new_instancemethod(_raster.float_raster_GetYPosition,None,float_raster)
float_raster.statistics = new_instancemethod(_raster.float_raster_statistics,None,float_raster)
float_raster.histogram = new_instancemethod(_raster.float_raster_histogram,None,float_raster)
float_raster.__imul__ = new_instancemethod(_raster.float_raster___imul__,None,float_raster)
float_raster.__iadd__ = new_instancemethod(_raster.float_raster___iadd__,None,float_raster)
float_raster.__isub__ = new_instancemethod(_raster.float_raster___isub__,None,float_raster)
float_raster.__idiv__ = new_instancemethod(_raster.float_raster___idiv__,None,float_raster)
float_raster.__mul__ = new_instancemethod(_raster.float_raster___mul__,None,float_raster)
float_raster.__add__ = new_instancemethod(_raster.float_raster___add__,None,float_raster)
float_raster.__sub__ = new_instancemethod(_raster.float_raster___sub__,None,float_raster)
float_raster.__div__ = new_instancemethod(_raster.float_raster___div__,None,float_raster)
float_raster.WriteToASCFile = new_instancemethod(_raster.float_raster_WriteToASCFile,None,float_raster)
float_raster.WriteToBinary = new_instancemethod(_raster.float_raster_WriteToBinary,None,float_raster)
float_raster.ToInt = new_instancemethod(_raster.float_raster_ToInt,None,float_raster)
float_raster.ToFloat = new_instancemethod(_raster.float_raster_ToFloat,None,float_raster)
float_raster.ToDouble = new_instancemethod(_raster.float_raster_ToDouble,None,float_raster)
float_raster.adress = new_instancemethod(_raster.float_raster_adress,None,float_raster)
float_raster.focal_min = new_instancemethod(_raster.float_raster_focal_min,None,float_raster)
float_raster.focal_max = new_instancemethod(_raster.float_raster_focal_max,None,float_raster)
float_raster.focal_mean = new_instancemethod(_raster.float_raster_focal_mean,None,float_raster)
float_raster.focal_stdev = new_instancemethod(_raster.float_raster_focal_stdev,None,float_raster)
float_raster.focal_majority = new_instancemethod(_raster.float_raster_focal_majority,None,float_raster)
float_raster.focal_mean_difference = new_instancemethod(_raster.float_raster_focal_mean_difference,None,float_raster)
float_raster.clone = new_instancemethod(_raster.float_raster_clone,None,float_raster)
float_raster.GetData = new_instancemethod(_raster.float_raster_GetData,None,float_raster)
float_raster.ToBuffer = new_instancemethod(_raster.float_raster_ToBuffer,None,float_raster)
float_raster.__radd__ = new_instancemethod(_raster.float_raster___radd__,None,float_raster)
float_raster.__rsub__ = new_instancemethod(_raster.float_raster___rsub__,None,float_raster)
float_raster.__rmul__ = new_instancemethod(_raster.float_raster___rmul__,None,float_raster)
float_raster.__rdiv__ = new_instancemethod(_raster.float_raster___rdiv__,None,float_raster)
float_raster_swigregister = _raster.float_raster_swigregister
float_raster_swigregister(float_raster)

class int_raster(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _raster.int_raster_swiginit(self,_raster.new_int_raster(*args))
    __swig_destroy__ = _raster.delete_int_raster
int_raster.Xllcorner = new_instancemethod(_raster.int_raster_Xllcorner,None,int_raster)
int_raster.Yllcorner = new_instancemethod(_raster.int_raster_Yllcorner,None,int_raster)
int_raster.XCellsize = new_instancemethod(_raster.int_raster_XCellsize,None,int_raster)
int_raster.YCellsize = new_instancemethod(_raster.int_raster_YCellsize,None,int_raster)
int_raster.ColumnCount = new_instancemethod(_raster.int_raster_ColumnCount,None,int_raster)
int_raster.RowCount = new_instancemethod(_raster.int_raster_RowCount,None,int_raster)
int_raster.Width = new_instancemethod(_raster.int_raster_Width,None,int_raster)
int_raster.Height = new_instancemethod(_raster.int_raster_Height,None,int_raster)
int_raster.NoData = new_instancemethod(_raster.int_raster_NoData,None,int_raster)
int_raster.HasData = new_instancemethod(_raster.int_raster_HasData,None,int_raster)
int_raster.SetData = new_instancemethod(_raster.int_raster_SetData,None,int_raster)
int_raster.GetXPosition = new_instancemethod(_raster.int_raster_GetXPosition,None,int_raster)
int_raster.GetYPosition = new_instancemethod(_raster.int_raster_GetYPosition,None,int_raster)
int_raster.statistics = new_instancemethod(_raster.int_raster_statistics,None,int_raster)
int_raster.histogram = new_instancemethod(_raster.int_raster_histogram,None,int_raster)
int_raster.__imul__ = new_instancemethod(_raster.int_raster___imul__,None,int_raster)
int_raster.__iadd__ = new_instancemethod(_raster.int_raster___iadd__,None,int_raster)
int_raster.__isub__ = new_instancemethod(_raster.int_raster___isub__,None,int_raster)
int_raster.__idiv__ = new_instancemethod(_raster.int_raster___idiv__,None,int_raster)
int_raster.__mul__ = new_instancemethod(_raster.int_raster___mul__,None,int_raster)
int_raster.__add__ = new_instancemethod(_raster.int_raster___add__,None,int_raster)
int_raster.__sub__ = new_instancemethod(_raster.int_raster___sub__,None,int_raster)
int_raster.__div__ = new_instancemethod(_raster.int_raster___div__,None,int_raster)
int_raster.WriteToASCFile = new_instancemethod(_raster.int_raster_WriteToASCFile,None,int_raster)
int_raster.WriteToBinary = new_instancemethod(_raster.int_raster_WriteToBinary,None,int_raster)
int_raster.ToInt = new_instancemethod(_raster.int_raster_ToInt,None,int_raster)
int_raster.ToFloat = new_instancemethod(_raster.int_raster_ToFloat,None,int_raster)
int_raster.ToDouble = new_instancemethod(_raster.int_raster_ToDouble,None,int_raster)
int_raster.adress = new_instancemethod(_raster.int_raster_adress,None,int_raster)
int_raster.focal_min = new_instancemethod(_raster.int_raster_focal_min,None,int_raster)
int_raster.focal_max = new_instancemethod(_raster.int_raster_focal_max,None,int_raster)
int_raster.focal_mean = new_instancemethod(_raster.int_raster_focal_mean,None,int_raster)
int_raster.focal_stdev = new_instancemethod(_raster.int_raster_focal_stdev,None,int_raster)
int_raster.focal_majority = new_instancemethod(_raster.int_raster_focal_majority,None,int_raster)
int_raster.focal_mean_difference = new_instancemethod(_raster.int_raster_focal_mean_difference,None,int_raster)
int_raster.clone = new_instancemethod(_raster.int_raster_clone,None,int_raster)
int_raster.GetData = new_instancemethod(_raster.int_raster_GetData,None,int_raster)
int_raster.ToBuffer = new_instancemethod(_raster.int_raster_ToBuffer,None,int_raster)
int_raster.__radd__ = new_instancemethod(_raster.int_raster___radd__,None,int_raster)
int_raster.__rsub__ = new_instancemethod(_raster.int_raster___rsub__,None,int_raster)
int_raster.__rmul__ = new_instancemethod(_raster.int_raster___rmul__,None,int_raster)
int_raster.__rdiv__ = new_instancemethod(_raster.int_raster___rdiv__,None,int_raster)
int_raster_swigregister = _raster.int_raster_swigregister
int_raster_swigregister(int_raster)

try:
    import numpy
except ImportError:
    numpy=None
try:
    import matplotlib.pyplot as pyplot
except ImportError:
    pyplot=None
class Raster:
    def __init__(self,filename=None,dtype="f",shape=None,corner=(0,0),cellsize=(1,1),NoData=-9999,raster=None):
        """ Creates a raster
           filename = The filename of an raster file in the ESRI ASCII format
           dtype = shortcut for the data type, either 'f' for float, 's' for float32 or 'i' for integer (32 bit)
        The next parameters have no meaning, if a filename was given
           shape = the dimensins of the raster, a tuple of integers (rows,columns)
           corner = (x,y) the position of the lower left corner in world coordinates
           cellsize = the cellsize in map units, can be a tuple with one vlaue for x direction and another for the y direction
           NoData = Value to indicate no data
        The raster keyword is only for internal usage
        """
        self.dtype=dtype
        if (raster):
            self.raster=raster
            return
        if (dtype in ["f","f8"]):
            rtype=double_raster
        elif (dtype in ["s","f4"]):
            rtype=single_raster
        elif (dtype in ["i","i4"]):
            rtype=int_raster
        else:
            raise ValueError("Data type mast be f,s or i")
        if (filename):
            self.raster=rtype(filename)
        else:
            try:
                row,col=shape
            except:
                raise ValueError("If no filename is given the dimensions of the raster has to be specified as a tuple, e.g. (10,10)")
            try:
                x_size,y_size=cellsize
            except:
                x_size=y_size=cellsize
            self.raster=rtype(col,row,corner[0],corner[1],x_size,y_size,NoData,NoData)
    @property
    def llcorner(self):
        "The lower left corner (x,y)"
        return (self.raster.Xllcorner(),self.raster.Yllcorner())
    @property
    def cellsize(self):
        "The cell size (x,y) in map coordinates"
        return (self.raster.XCellsize(),self.raster.YCellsize())
    @property
    def shape(self):
        "The tuple (rows,cols)"
        return (self.raster.RowCount(),self.raster.ColumnCount())
    @property
    def extent(self):
        "The extent of the raster (width,height) in map coordinates"
        return self.llcorner[0],self.llcorner[0]+self.shape[1]*self.cellsize[0],self.llcorner[1],self.llcorner[1]+self.shape[0]*self.cellsize[1]
    def neighbors(self,x,y):
        """ Returns a list of the neighbors to the given position
        x,y are intepreted as real coordinates, if they are floating point numbers,
            otherwise they are interpreted as column and row of the raster
        Result: A tuple for each adjacent neighbor of type (column,row,value,distance,x_direction,y_direction)
        """
        if type(x) is float or type(y) is float:
            col,row=colrow(x,y)
        else:
            col,row=int(x),int(y)
        x_pos=y_pos=[-1,0,1]
        res=[]
        for y in y_pos:
            for x in x_pos:
                v=self[col+x,row+y]
                if (x or y) and v!=self.nodata:   # Exclude the cell itself and nodata cells
                    distance=sqrt((x*self.cellsize[0])**2+(y*self.cellsize[1])**2)
                    res.append((col+x,row+y,v,distance,x,y))
        return res
    def xy(self,col,row):
        "Gets a position in world coordinates from a position in the dataset (col,row)->(x,y)"
        return (col*self.cellsize[0]+self.llcorner[0],(self.shape[0]-row)*self.cellsize[1]+self.llcorner[1])
    def colrow(self,x,y):
        "Gets a position in the dataset from world coordinates (x,y)->(colr,row)"
        return (int((x-self.corner[0])/self.cellsize[0]),int(self.shape[0]-(y-self.corner[1])/self.cellsize[1]))
    @property
    def nodata(self):
        "Gets the no data value of the raster"
        return self.raster.NoData()
    @property
    def rows(self):
        "Gets the number of rows in the data set"
        for r in range(self.shape[0]):
            yield [self.raster.GetData(r,c) for c in range(self.shape[1])]
    @property
    def cells(self):
        """ Returns an iterator over all cells of the raster, that returns the tuple (x,y,value,area,column,row) """
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                if self[c,r]!=self.nodata:
                    x=self.llcorner[0]+self.cellsize[0]*(c+0.5)
                    y=self.llcorner[1]+self.cellsize[1]*(self.shape[0]-(r+0.5))
                    v=self[c,r]
                    area=self.cellsize[0]*self.cellsize[1]
                    yield((x,y,v,area,c,r))
    def __iter__(self):
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                yield c,r
    @property 
    def values(self):
        """Returns a dictionary containing all distinct values and the number of their appearances """
        res={}
        for c,r in self:
            v=self[c,r]
            if v==self.nodata: continue
            if v in res:
                res[v]+=1
            else:
                res[v]=1
        return res
    def __getitem__(self,pos):
        if hasattr(pos,"__len__"):
            if (len(pos)==2):
                return self.raster.GetData(*pos)
        raise ValueError("Only two coordinates, x and y can be used for __getitem__")
    def __setitem__(self,pos,value):
        if hasattr(pos,"__len__"):
            if (len(pos)==2):
                return self.raster.SetData(pos[0],pos[1],value)
        raise ValueError("Only two coordinates, x and y can be used for __getitem__")
    def __call__(self,x,y,z=0):
        x=float(x) if type(x) is int else x
        y=float(y) if type(y) is int else y
        v=self.raster.GetData(x,y)
        return v if not v==self.nodata else None
    def histogram(self,bins=100):
        return self.raster.histogram(bins)
    @property
    def statistics(self):
        return self.raster.statistics()
    def save(self,filename,binary=False):
        if binary:
            self.raster.WriteToBinary(filename)
        else:
            self.raster.WriteToASCFile(filename)
    def focal_min(self,n=3):
        """ Focal minimum function: each cell of the new raster gets the minimum value of the surrounding n x n matrix"""
        res=self.raster.focal_min(n)
        return Raster(dtype=self.dtype,raster=res)
    def focal_max(self,n=3):
        """ Focal maximum function: each cell of the new raster gets the maximum value of the surrounding n x n matrix"""
        res=self.raster.focal_max(n)
        return Raster(self,raster=res)
    def focal_mean(self,n=3):
        """ Focal mean function: each cell of the new raster gets the mean value of the surrounding n x n matrix"""
        res=self.raster.focal_mean(n)
        return Raster(dtype=self.dtype,raster=res)
    def focal_stdev(self,n=3):
        """ Focal standard deviation function: each cell of the new raster gets the standard deviation value of the surrounding n x n matrix"""
        res=self.raster.focal_stdev(n)
        return Raster(dtype=self.dtype,raster=res)
    def focal_majority(self,n=3):
        """ Focal majority function: each cell of the new raster gets the most frequent value of the surrounding n x n matrix. 
            If each value is unique in the matrix, the result is the old value"""
        res=self.raster.focal_majority(n)
        return Raster(dtype=self.dtype,raster=res)
    def focal_mean_difference(self,n=3):
        """ Optimised shortcut for =r-r.focal_mean(n) """
        res=self.raster.focal_mean_difference(n)
        return Raster(dtype=self.dtype,raster=res)
    def to_int(self):
        """ Creates a new raster of type integer from self (int 32)"""
        res=self.raster.ToInt()
        return Raster(dtype=self.dtype,raster=res)
    def to_double(self):
        """ Creates a new raster of type double (floating point 64) from self """
        res=self.raster.ToDouble()
        return Raster(dtype=self.dtype,raster=res)
    def to_single(self):
        """ Creates a new raster of type single (floating point 32) from self """
        res=self.raster.ToSingle()
        return Raster(dtype=self.dtype,raster=res)
    @property
    def mask(self):
        res=self.raster.HasData()
        return Raster(dtype='i',raster=res)
    def clone(self):
        """ Creates a copy of this raster """
        res=self.raster.clone()
        return Raster(dtype=self.dtype,raster=res)
    def __iadd__(self,other):
        if type(other) is type(self):
            self.raster+=other.raster
        else:
            try:
               self.raster+=other
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __imul__(self,other):
        if type(other) is type(self):
            self.raster*=other.raster
        else:
            try:
               self.raster*=other
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __isub__(self,other):
        if type(other) is type(self):
            self.raster-=other.raster
        else:
            try:
               self.raster-=other
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __idiv__(self,other):
        if type(other) is type(self):
            self.raster/=other.raster
        else:
            try:
               self.raster/=other
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __add__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster+other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster+other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __mul__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster*other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster*other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __sub__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster-other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster-other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __div__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster/other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster/other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __radd__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster+other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster+other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __rmul__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=self.raster*other.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=self.raster*other)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __rsub__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=other.raster - self.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=other - self.raster)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __rdiv__(self,other):
        if type(other) is type(self):
            return Raster(dtype=self.dtype,raster=other.raster/self.raster)
        else:
            try:
               return Raster(dtype=self.dtype,raster=other/self.raster)
            except TypeError:
               raise TypeError("Can't add a %s to this raster %s" % (typename(other),typename(self.raster)))
    def __neg__(self):
        return Raster(dtype=self.dtype,raster= self.raster * (-1))
    @property
    def __array_interface__(self):
        "Returns the array interface for the raster."
        types={'i':'|i4','f':'|f8','s':'|f4'}
        return dict(shape  = self.shape,
                    data   = (self.raster.adress(),0),
                    typestr= types[self.dtype],
                    mask   = self.mask,
                   )
    def asarray(self):
        "Returns a 2D masked array, where nodata areas are masked"
        try:
            import numpy.ma
            mres=numpy.ma.array(numpy.asarray(self),mask=1-numpy.asarray(self.mask,dtype=numpy.bool),copy=False)
            return mres
        except ImportError:
            raise NotImplementedError("asarray needs an installation of numpy to work!")
    def draw(self,cmap=None,vmin=None,vmax=None,hold=1,interpolation='nearest',**kwargs):
        try:
            import matplotlib.pyplot as pyplot
            if cmap is None:
                cmap=pyplot.cm.jet
            if vmin is None:
                vmin=self.statistics.min
            if vmax is None:
                vmax=self.statistics.max
            pyplot.imshow(self.asarray(),cmap,interpolation=interpolation,
                          aspect='equal',vmin=vmin,vmax=vmax,hold=hold,
                          extent=self.extent,
                          **kwargs)
        except ImportError:
            raise NotImplementedError("Raster.draw needs an installation of matplotlib to work")
    def __repr__(self):
        stat=self.statistics
        fmt="Raster<%s>: n=%i,min=%g,mean=%g,max=%g,stdev=%g,row,col=%s,cellsize=(%g,%g)"
        return fmt % (self.dtype,stat.count,stat.min,stat.mean,stat.max,stat.stdev,
                      self.shape,self.cellsize[0],self.cellsize[1])




