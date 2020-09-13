from flask import Blueprint, request, Response
import pymongo
import urllib
from bson.json_util import dumps
import datetime
import math
mod_data = Blueprint('routes', __name__, )
from dbUtils import DBUtils

@mod_data.route('/get-2d-shapes')
def get_2d_shapes():
    return dumps(list(DBUtils().get_collection_obj("LOCAL", "shapes", "shape").find({"type": "2D"})))

@mod_data.route('/get-3d-shapes')
def get_3d_shapes():
    return dumps(list(DBUtils().get_collection_obj("LOCAL", "shapes", "shape").find({"type": "3D"})))

@mod_data.route('/get-shapes')
def get_shapes():
    return dumps(list(DBUtils().get_collection_obj("LOCAL", "shapes", "shape").find({})))

@mod_data.route('/get-shape-defination')
def get_shape_defination():
    shape = request.args.get("shape")
    if shape is not None:
        return dumps(DBUtils().get_collection_obj("LOCAL", "shapes", "shape").find_one({"id": shape}))
    else:
        return "shape is a compulsory param", 404
    
@mod_data.route('/get-shape-geometry')
def get_shape_geometr():
    shape = request.args.get("shape")
    if shape is not None:
        if shape == "triangleEquilateral":
            side = float(request.args.get("x"))
            return dumps({"Area": (math.sqrt(3)* math.pi * side*side)/4, "Perimeter": 3*side})
        elif shape == "triangleIsoceles":
            side = float(request.args.get("a"))
            base = float(request.args.get("b"))
            height = float(request.args.get("h"))
            return dumps({"Area": (base*height)/2, "Perimeter": (2*side)+base})
        elif shape == "triangleScalene":
            side = float(request.args.get("a"))
            otherside = float(request.args.get("c"))
            base = float(request.args.get("b"))
            height = float(request.args.get("h"))
            return dumps({"Area": (base*height)/2, "Perimeter": side + otherside + base})    
        elif shape == "triangleRightAngled":
            side = float(request.args.get("a"))
            base = float(request.args.get("b"))
            return dumps({"Area": (side*base)/2, "Perimeter": side + base + math.sqrt(side*side + base*base)})   
        elif shape == "square":
            side = float(request.args.get("a"))
            return dumps({"Area": (side*side), "Perimeter": 4*side})
        elif shape == "rectangle":
            side = float(request.args.get("a"))
            otherSide = float(request.args.get("b"))
            return dumps({"Area": (side*otherSide), "Perimeter": 2*(side + otherSide)})
        elif shape == "cube":
            side = float(request.args.get("a"))
            return dumps({"Suraface Area": 6*(side*side), "Perimeter": 12*side, "Volume": side*side*side})
        elif shape == "cuboid":
            length =float(request.args.get("l")) 
            width = float(request.args.get("w"))
            height = float(request.args.get("h"))
            return dumps({"Suraface Area": (2*(length*width)+2*(width*height)+2*(height*length)),
             "Perimeter": 4*(length + width + height),
              "Volume": height*width*length})
        elif shape == "cylinder":
            radius =float(request.args.get("r")) 
            height = float(request.args.get("h"))
            return dumps({"Suraface Area": 2* ( math.pi * radius * height + math.pi * radius * radius),
             "Perimeter": 2*math.pi*radius*height,
              "Volume": math.pi*radius*radius*height})        
    else:
        return "shape is a compulsory param", 404