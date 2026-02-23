# Blender Imports
import bpy
from mathutils import Euler

# Resonitelink Imports
from resonitelink.proxies.datamodel.slot_proxy import SlotProxy
from resonitelink.proxies.datamodel.component_proxy import ComponentProxy

class ID_SlotData():

    def __init__(self, id : bpy.types.ID, slotProxy : SlotProxy):
        self.id : bpy.types.ID = id
        self.slot : SlotProxy = slotProxy


class ObjectSlotData(ID_SlotData):

    def __init__(self, obj : bpy.types.Object, slotProxy : SlotProxy):
        super().__init__(obj, slotProxy)

    def GetObject(self) -> bpy.types.Object:
        return self.id
    
    def GetData(self) -> bpy.types.ID:
        return self.id.data


class MeshSlotData(ObjectSlotData):

    def __init__(self, obj : bpy.types.Object, slotProxy : SlotProxy):
        super().__init__(obj, slotProxy)
        self.meshComp : ComponentProxy = None
        self.matComps : list[ComponentProxy] = [] 
        self.meshRenderer : ComponentProxy = None
        self.hidden = False
    

class SceneSlotData(ID_SlotData):

    pass


def b2u_coords(x, y, z):
    """
    Convert Blender coordinates to Unity coordinates.
    
    Parameters
    ----------
    x : float
        The Blender x coordinate
    y : float
        The Blender y coordinate
    z : float
        The Blender z coordinate
    
    Returns
    -------
    x : float
        The converted Unity x coordinate
    y : float
        The converted Unity y coordinate
    z : float
        The converted Unity z coordinate
    """
    
    #return -x, -z, y
    return -x, z, -y

def b2u_scale(x, y, z):
    """
    Convert Blender scales to Unity scales.
    
    Parameters
    ----------
    x : float
        The Blender x scale
    y : float
        The Blender y scale
    z : float
        The Blender z scale
    
    Returns
    -------
    x : float
        The converted Unity x scale
    y : float
        The converted Unity y scale
    z : float
        The converted Unity z scale
    """
    
    return x, z, y

def b2u_euler2quaternion(e):
    """
    Convert Blender Euler rotation to Unity quaternion.
    
    Parameters
    ----------
    e : mathutils.Euler
        The input Blender euler rotation
    
    Returns
    -------
    q : Quaternion
        The output Unity quaternion
    """
    
    return Euler((e.x, -e.z, e.y), "XYZ").to_quaternion()

def b2u_mat4(m):
    """
    Convert a Blender 4x4 transform Matrix into a
    Unity Float4x4 transform matrix.
    
    Parameters
    ----------
    m : Matrix
        The input Blender transform matrix (4x4)
    
    Returns
    -------
    o : Float4x4
        The output Unity transform matrix (4x4)
    """
    
    # TODO: Fix transformation
    return Float4x4(
        m[0][0], m[0][1], m[0][2], m[0][3],
        m[1][0], m[1][1], m[1][2], m[1][3],
        m[2][0], m[2][1], m[2][2], m[2][3],
        m[3][0], m[3][1], m[3][2], m[3][3]
    )
