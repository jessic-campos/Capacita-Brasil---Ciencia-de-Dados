import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Criando a figura
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Definindo as entidades com posições
entities = {
    "LIVRO": (1, 6),
    "CATEGORIA": (4, 8),
    "EXEMPLAR": (4, 6),
    "USUARIO": (1, 2),
    "EMPRESTIMO": (4, 2)
}

# Desenhando as caixas de entidade
for name, (x, y) in entities.items():
    ax.add_patch(patches.Rectangle((x-0.5, y-0.5), 2, 1, edgecolor='black', facecolor='lightblue'))
    ax.text(x + 0.5, y, name, ha='center', va='center', fontsize=10, fontweight='bold')

# Desenhando os relacionamentos (linhas e setas)
connections = [
    ("LIVRO", "CATEGORIA", "pertence a"),
    ("LIVRO", "EXEMPLAR", "possui"),
    ("EXEMPLAR", "EMPRESTIMO", "é utilizado em"),
    ("USUARIO", "EMPRESTIMO", "realiza")
]

for ent1, ent2, label in connections:
    x1, y1 = entities[ent1]
    x2, y2 = entities[ent2]
    ax.annotate("",
                xy=(x2+0.5, y2), xycoords='data',
                xytext=(x1+0.5, y1), textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text((x1+x2)/2 + 0.5, (y1+y2)/2, label, fontsize=9, style='italic')

# Salvando o resultado
output_path = "/mnt/data/ERD_Biblioteca.png"
plt.savefig(output_path, bbox_inches='tight')
output_path
