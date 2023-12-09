"""03_03_egg_model_maker_1.py"""

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
    <TRef> { one }
    <Normal> { 0 1 0 }
    <VertexRef> { 2 6 5 1 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { one }
    <Normal> { -1 0 0 }
    <VertexRef> { 1 5 7 3 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { one }
    <Normal> { 1 0 0 }
    <VertexRef> { 4 8 6 2 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { one }
    <Normal> { 0 0 1 }
    <VertexRef> { 9 3 4 10 <Ref> { box } }
  }
  <Polygon> {
    <TRef> { one }
    <Normal> { 0 0 -1 }
    <VertexRef> { 7 11 12 8 <Ref> { box } }
  }
}

"""


class EggModel:
    def __init__(self, model_name, texture1):
        self.model_name = model_name
        self.texture1 = texture1

    def make(self):
        model = coordinate
        model += f'<Texture> one {{\n  "../textures/{self.texture1}.png"\n}}\n\n'
        model += vertex_pool + group

        print(model)

        # クライアントから送られてきたデータをファイルに書き出す
        with open(f"models/{self.model_name}.egg", "w") as f:
            f.write(model)


if __name__ == "__main__":
    blocks_1 = {
        'stone': ['0-1'],
        'dirt': ['0-2'],
        'bricks': ['0-7'],
        'cobblestone': ['1-0'],
        'bedrock': ['1-1'],
        'sand': ['1-2'],
        'iron_block': ['1-6'],
        'gold_block': ['1-7'],
        'diamond_block': ['1-8'],
        'emerald_block': ['1-9'],
        'gold_ore': ['2-0'],
        'iron_ore': ['2-1'],
        'coal_ore': ['2-2'],
        'mossy_cobblestone': ['2-4'],
        'obsidian': ['2-5'],
        'sponge': ['3-0'],
        'glass': ['3-1'],
        'diamond_ore': ['3-2'],
        'redstone_ore': ['3-3'],
        'oak_leaves': ['3-4'],
        'oak_plants': ['0-4'],
        'stone_bricks': ['3-6'],
        'lava': ['3-21'],
        'water': ['3-22'],
        'white_wool': ['4-0'],
        'mob_spawner': ['4-1'],
        'snow': ['4-2'],
        'ice': ['4-3'],
        'black_wool': ['7-1'],
        'gray_wool': ['7-2'],
        'red_wool': ['8-1'],
        'pink_wool': ['8-2'],
        'lapis_block': ['9-0'],
        'green_wool': ['9-1'],
        'lime_wool': ['9-2'],
        'lapis_ore': ['10-0'],
        'brown_wool': ['10-1'],
        'yellow_wool': ['10-2'],
        'blue_wool': ['11-1'],
        'cyan_wool': ['11-2'],
        'purple_wool': ['12-1'],
        'magenta_wool': ['12-2'],
        'spruce_planks': ['12-6'],
        'jungle_planks': ['12-7'],
        'light_blue_wool': ['13-1'],
        'orange_wool': ['13-2'],
        'birch_planks': ['13-6'],
        'light_gray_wool': ['14-1'],
        'target_block': ['target_block'],
    }

    for key, value in blocks_1.items():
        egg_model = EggModel(key, value[0])
        egg_model.make()