"""07_01_egg_model_maker_1_2_3_4_5_6.py"""

coordinate = """\
<CoordinateSystem> { Z-Up }

"""
vertex_pool = """\
<VertexPool> box {
  <Vertex> 1 {
    0 1 1
    <UV> { 1 1 }
  }
  <Vertex> 2 {
    1 1 1
    <UV> { 0 1 }
  }
  <Vertex> 3 {
    0 0 1
    <UV> { 0 1 }
  }
  <Vertex> 4 {
    1 0 1
    <UV> { 1 1 }
  }
  <Vertex> 5 {
    0 1 0
    <UV> { 1 0 }
  }
  <Vertex> 6 {
    1 1 0
    <UV> { 0 0 }
  }
  <Vertex> 7 {
    0 0 0
    <UV> { 0 0 }
  }
  <Vertex> 8 {
    1 0 0
    <UV> { 1 0 }
  }
  <Vertex> 9 {
    0 1 1
    <UV> { 0 0 }
  }
  <Vertex> 10 {
    1 1 1
    <UV> { 1 0 }
  }
  <Vertex> 11 {
    0 1 0
    <UV> { 0 1 }
  }
  <Vertex> 12 {
    1 1 0
    <UV> { 1 1 }
  }
}

"""
group = """\
<Group> box {
  <Polygon> {
    <TRef> { one }
    <Normal> { 0 1 0 }
    <VertexRef> { 3 7 8 4 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { two }
    <Normal> { 0 1 0 }
    <VertexRef> { 2 6 5 1 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { three }
    <Normal> { -1 0 0 }
    <VertexRef> { 1 5 7 3 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { four }
    <Normal> { 1 0 0 }
    <VertexRef> { 4 8 6 2 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { five }
    <Normal> { 0 0 1 }
    <VertexRef> { 9 3 4 10 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { six }
    <Normal> { 0 0 -1 }
    <VertexRef> { 7 11 12 8 <Ref> { box } }
  }
}

"""


class EggModel:
    def __init__(self, model_name, texture1, texture2, texture3, texture4, texture5, texture6):
        self.model_name = model_name
        self.texture1 = texture1
        self.texture2 = texture2
        self.texture3 = texture3
        self.texture4 = texture4
        self.texture5 = texture5
        self.texture6 = texture6

    def make(self):
        model = coordinate
        model += f'<Texture> one {{\n  "../textures/{self.texture1}.png"\n}}\n\n'
        model += f'<Texture> two {{\n  "../textures/{self.texture2}.png"\n}}\n\n'
        model += f'<Texture> three {{\n  "../textures/{self.texture3}.png"\n}}\n\n'
        model += f'<Texture> four {{\n  "../textures/{self.texture4}.png"\n}}\n\n'
        model += f'<Texture> five {{\n  "../textures/{self.texture5}.png"\n}}\n\n'
        model += f'<Texture> six {{\n  "../textures/{self.texture6}.png"\n}}\n\n'
        model += vertex_pool + group

        print(model)

        # クライアントから送られてきたデータをファイルに書き出す
        with open(f"models/{self.model_name}.egg", "w") as f:
            f.write(model)


if __name__ == "__main__":
    blocks_1_2_3_4_5_6 = {
        'player_head': ['player_textures/head/1', 'player_textures/head/2', 'player_textures/head/3', 'player_textures/head/4', 'player_textures/head/5', 'player_textures/head/6'],
        'player_body': ['player_textures/body/1', 'player_textures/body/2', 'player_textures/body/3', 'player_textures/body/4', 'player_textures/body/5', 'player_textures/body/6'],
        'player_hand': ['player_textures/hand/1', 'player_textures/hand/2', 'player_textures/hand/3', 'player_textures/hand/4', 'player_textures/hand/5', 'player_textures/hand/6'],
        'player_leg': ['player_textures/leg/1', 'player_textures/leg/2', 'player_textures/leg/3', 'player_textures/leg/4', 'player_textures/leg/5', 'player_textures/leg/6'],
    }

    for key, value in blocks_1_2_3_4_5_6.items():
        egg_model = EggModel(key, value[0], value[1], value[2], value[3], value[4], value[5])
        egg_model.make()