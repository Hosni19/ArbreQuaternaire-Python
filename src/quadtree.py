from __future__ import annotations
import tkinter as tk
import json

class QuadTree:
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bg: bool | QuadTree, bd: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bg = bg
        self.bd = bd

    @property
    def depth(self) -> int:
        if isinstance(self.hg, QuadTree):
            return 1 + self.hg.depth
        return 1

    @staticmethod
    def fromFile(filename):
        with open(filename, 'r') as file:
            content = file.read().strip()

        try:
            data = json.loads(content)
            quadtree = QuadTree.fromList(data)
        except json.JSONDecodeError as e:
            print("Erreur lors du décodage JSON:", e)
            raise
        except Exception as e:
            print("Erreur inattendue:", e)
            raise

        return quadtree

    @staticmethod
    def fromList(data):
        if not data or len(data) != 4:
            raise ValueError("La liste 'data' n'a pas la longueur attendue.")

        hg = QuadTree(*data[3])
        hd = QuadTree(*data[2])
        bg = QuadTree(*data[1])
        bd = QuadTree(*data[0])

        return QuadTree(hg, hd, bg, bd)

    def paint(self):
        print(f"Profondeur: {self.depth}")
        self._paint()

    def _paint(self, depth=0):
        print(f"Depth: {depth}, Node: {self.hg}, {self.hd}, {self.bg}, {self.bd}")
        if isinstance(self.hg, QuadTree):
            self.hg._paint(depth + 1)
            self.hd._paint(depth + 1)
            self.bg._paint(depth + 1)
            self.bd._paint(depth + 1)


class TkQuadTree(QuadTree):
    def paint(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=400, height=400)
        canvas.pack()


        self._draw(canvas, 0, 0, 400, 400)

        root.mainloop()

    def _draw(self, canvas, x, y, width, height, depth=0):
        if isinstance(self.hg, QuadTree):
            half_width = width // 2
            half_height = height // 2

            TkQuadTree._draw(canvas, x, y, half_width, half_height, self.hg, depth + 1)
            TkQuadTree._draw(canvas, x + half_width, y, half_width, half_height, self.hd, depth + 1)
            TkQuadTree._draw(canvas, x + half_width, y + half_height, half_width, half_height, self.bg, depth + 1)
            TkQuadTree._draw(canvas, x, y + half_height, half_width, half_height, self.bd, depth + 1)
        else:
            text = f"{depth}"
            canvas.create_text(x + width // 2, y + height // 2, text=text, font=("Helvetica", 12))


filename = 'C:/ProjetPython/files/quadtree.txt'
tkinter_viewer = TkQuadTree.fromFile(filename)
tkinter_viewer.paint()
