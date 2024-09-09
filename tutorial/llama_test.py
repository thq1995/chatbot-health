from llama_index.core import Document
from llama_index.core.schema import TextNode
from llama_index.core.node_parser import TokenTextSplitter


text = "Hôm nay trời nắng, tôi đi ăn kem, lạnh buốt cả răng!"
doc = Document(
    text=text,
    metadata={"author": "Alice"},
    id_="123",
)

spitter = TokenTextSplitter(
    chunk_size=20,
    chunk_overlap=5,
    separator=" ",
)

nodes = spitter.get_nodes_from_documents([doc])

for node in nodes:
    print(node)
    print()