import os

for nb, replacements in [
    (
        r"c:\Users\rrienks\projects\DataManagement\AI_for_Datamanagement.ipynb",
        [
            (
                '    "    AI-driven semantic type detection.\\n",\n    "    Combines column name analysis with pattern recognition in the data.\\n",',
                '    "    Rule-based semantic type detection.\\n",\n    "    Matches column name against keyword lists; no ML involved.\\n",'
            ),
            (
                '    "    AI-driven classification of a column based on:\\n",',
                '    "    Rule-based classification of a column based on:\\n",'
            ),
        ]
    ),
    (
        r"c:\Users\rrienks\projects\DataManagement\AI_voor_Datamanagement.ipynb",
        [
            (
                '    "    AI-gestuurde classificatie van een kolom op basis van:\\n",\n    "    - Kolomnaam (semantische analyse)\\n",\n    "    - Patroonherkenning in de waarden\\n",\n    "    - Statistische kenmerken\\n",',
                '    "    Regelgebaseerde kolomclassificatie op basis van:\\n",\n    "    - Kolomnaam (sleutelwoord-matching, geen ML)\\n",\n    "    - Patroonherkenning via regex in de waarden\\n",\n    "    - Statistische kenmerken\\n",'
            ),
        ]
    ),
]:
    with open(nb, "r", encoding="utf-8") as f:
        content = f.read()
    changed = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changed = True
            print(f"Fixed in {os.path.basename(nb)}: {old[:50]!r}")
        else:
            print(f"NOT FOUND in {os.path.basename(nb)}: {old[:50]!r}")
    if changed:
        with open(nb, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved {os.path.basename(nb)}")
