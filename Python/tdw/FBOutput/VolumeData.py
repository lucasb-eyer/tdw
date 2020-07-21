# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class VolumeData(object):
    __slots__ = ['_tab']

    # VolumeData
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # VolumeData
    def Id(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # VolumeData
    def Volume(self): return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreateVolumeData(builder, id, volume):
    builder.Prep(4, 8)
    builder.PrependFloat32(volume)
    builder.PrependInt32(id)
    return builder.Offset()