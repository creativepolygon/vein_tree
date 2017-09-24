# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Vein Tree",
    "author": "Thomas Rigsby aka Thomas Mueller",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "View3D > Tools",
    "description": "Creates awesome vein structures",
    "warning": "WITHOUT ANY WARRANTY",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Vein_Tree",
    "category": "Mesh"}

import bpy
from bpy.types import AddonPreferences

# Define Classes to register
classes = (
    TracerProperties,
    addTracerObjectPanel,
    OBJECT_OT_convertcurve,
    OBJECT_OT_objecttrace,
    OBJECT_OT_objectconnect,
    OBJECT_OT_writing,
    OBJECT_OT_particletrace,
    OBJECT_OT_traceallparticles,
    OBJECT_OT_curvegrow,
    OBJECT_OT_reset,
    OBJECT_OT_fcnoise,
    OBJECT_OT_meshfollow,
    OBJECT_OT_materialChango,
    OBJECT_OT_clearColorblender,
    btrace_preferences,
    )


def register():


def unregister():

if __name__ == "__main__":
    register()
