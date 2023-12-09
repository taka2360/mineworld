"""03_06_egg_model_maker_1_5_6.py"""

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
    <TRef> { two }
    <Normal> { -1 0 0 }
    <VertexRef> { 1 5 7 3 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { two }
    <Normal> { 1 0 0 }
    <VertexRef> { 4 8 6 2 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { five }
    <Normal> { 0 0 1 }
    <VertexRef> { 9 3 4 10 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { five }
    <Normal> { 0 0 -1 }
    <VertexRef> { 7 11 12 8 <Ref> { box } }
  }
}

"""


class EggModel:
    def __init__(self, model_name, texture1, texture2, texture5):
        self.model_name = model_name
        self.texture1 = texture1
        self.texture2 = texture2
        self.texture5 = texture5

    def make(self):
        model = coordinate
        model += f'<Texture> one {{\n  "../textures/{self.texture1}.png"\n}}\n\n'
        model += f'<Texture> two {{\n  "../textures/{self.texture2}.png"\n}}\n\n'
        model += f'<Texture> five {{\n  "../textures/{self.texture5}.png"\n}}\n\n'
        model += vertex_pool + group

        print(model)

        # クライアントから送られてきたデータをファイルに書き出す
        with open(f"models/{self.model_name}.egg", "w") as f:
            f.write(model)


if __name__ == "__main__":
    blocks_1_2_5 = {
        'furnace': ['2-12', '2-13', '3-14'],
        'burning_furnace': ['3-13', '2-13', '3-14'],
        'chest': ['6-19', '6-18', '6-17'],
        'pumpkin': ['7-7', '7-6', '6-6'],
        'jack_o_lantern': ['7-8', '7-6', '6-6'],
    }

    for key, value in blocks_1_2_5.items():
        egg_model = EggModel(key, value[0], value[1], value[2])
        egg_model.make()