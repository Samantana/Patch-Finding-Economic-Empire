import math
import random

from PIL import Image
from PIL.Image import Image


class Maping_sqr:
    def __init__(self):
        self.batiment = {}
        self.eau = {}
        self.personnage = {}
        self.travail = {}
        self.object_p = {}
        self.route = {}
        self.obstacle = {}
        self.vt = random.randint(0, 2)

    def add_batiment(self, x, y, v=1):
        self.batiment[(x, y)] = v

    def add_eau(self, x, y, v=1):
        self.eau[(x, y)] = v

    def add_personnage(self, x, y, v=1):
        self.personnage[(x, y)] = v

    def add_travail(self, x, y, v=1):
        self.travail[(x, y)] = v

    def add_object_p(self, x, y, v=1):
        self.object_p[(x, y)] = v

    def add_route(self, x, y, v=1):
        self.route[(x, y)] = v

    def add_obstacle(self, x, y, v=1):
        self.obstacle[(x, y)] = v

    ######################################
    # path finding
    ######################################
    def path_finding_r(self, x1, y1, x2, y2, v_flore: list = [3], v_obstacle: list = [4]):
        lx = [x1]
        ly = [y1]
        l = []
        lt = []  # pour le momment, il ressemble comme ce qui suit: [[[x][y]]...]
        s = True
        self.route_ = self.route.copy()
        while s:
            l.append(lx.copy())
            l.append(ly.copy())
            lt.append(l.copy())
            l.clear()
            lx.clear()
            ly.clear()
            lv = lt[-1]
            s1 = 0
            for i in range(len(lv[0])):

                x = lv[0][i]
                y = lv[1][i]
                x_ = x - 1
                x__ = x + 1
                y_ = y - 1
                y__ = y + 1
                if (x, y_) in self.route_:
                    try:
                        if self.route_[(x, y_)] in v_flore:  # 1-
                            self.route_[(x, y_)] = -5
                    finally:
                        lx.append(x)
                        ly.append(y_)
                        s += 1
                if (x == x2) and (y_ == y2): break
                if (x_, y) in self.route_:
                    if self.route_[(x_, y)] in v_flore:  # 2-
                        self.route_[(x_, y)] = -5
                        lx.append(x_)
                        ly.append(y)
                        s += 1
                if (x_ == x2) and (y == y2): break
                if (x_, y_) in self.route_:
                    if self.route_[(x_, y_)] in v_flore:  # 3-
                        self.route_[(x_, y_)] = -5
                        lx.append(x_)
                        ly.append(y_)
                        s1 += 1
                if (x_ == x2) and (y_ == y2): break
                if (x__, y) in self.route_:
                    if self.route_[(x__, y)] in v_flore:  # 4-
                        self.route_[(x__, y)] = -5
                        lx.append(x__)
                        ly.append(y)
                        s1 += 1
                if (x__ == x2) and (y == y2): break
                if (x, y__) in self.route_:
                    if self.route_[(x, y__)] in v_flore:  # 5-
                        self.route_[(x, y__)] = -5
                        lx.append(x)
                        ly.append(y__)
                        s1 += 1
                if (x == x2) and (y__ == y2): break
                if (x__, y_) in self.route_:
                    if self.route_[(x__, y_)] in v_flore:  # 6-
                        self.route_[(x__, y_)] = -5
                        lx.append(x__)
                        ly.append(y_)
                        s1 += 1
                if (x__ == x2) and (y_ == y2): break
                if (x_, y__) in self.route_:
                    if self.route_[(x_, y__)] in v_flore:  # 7
                        self.route_[(x_, y__)] = -5
                        lx.append(x_)
                        ly.append(y__)
                        s1 += 1
                if (x_ == x2) and (y__ == y2): break
                if (x__, y__) in self.route_:
                    if self.route_[(x__, y__)] in v_flore:  # 8-
                        self.route_[(x__, y__)] = -5
                        lx.append(x__)
                        ly.append(y__)
                        s1 += 1
                if (x__ == x2) and (y__ == y2): break
            if s1 == 0:
                return [False, []]  # cela signifie qu'il n'y a aucune possibilité
        l.append(lx)
        l.append(ly)
        lt.append(l)
        del self.route_
        v1 = len(lt[-1][0])
        lt1 = []
        l1 = []
        for e in lt:
            for i in e:
                while len(i) > v1:
                    i.pop(-1)
                l1.append(i)
            lt1.append(l1)
        lt.clear()

        for e in reversed(range(len(lt1))):
            l = lt1[e]
            lx = l[0]
            ly = l[1]
            lo = len(lx) - 1
            for e in reversed(range(lx)):
                if e != lo:
                    lx.pop(e)
                    ly.pop(e)
            l.clear()
            l.append(lx)
            l.append(ly)
            lt.append(l)
        return lt

    def new_patch(self, x1, y1, x2, y2, v_flore: list = [3], v_obstacle: list = []):
        lx = [x1]
        ly = [y1]
        l = []
        lt = []  # pour le momment, il ressemble comme ce qui suit: [[[x][y]]...]
        s = True
        self.route_ = self.route.copy()
        while s:
            l.append(lx.copy())
            l.append(ly.copy())
            lt.append(l.copy())
            l.clear()
            lx.clear()
            ly.clear()
            lv = lt[-1]
            s1 = 0
            for i in range(len(lv[0])):
                x = lv[0][i]
                y = lv[1][i]
                x_ = x - 1
                x__ = x + 1
                y_ = y - 1
                y__ = y + 1
                if (x, y_) not in self.route_:
                    try:
                        if self.route_[(x, y_)] in v_flore:  # 1-
                            self.route_[(x, y_)] = -5
                            lx.append(x_)
                            ly.append(y)
                            s += 1
                    except KeyError:
                        self.route_[(x,y_)] = -5
                        lx.append(x_)
                        ly.append(y)
                        s += 1
                if (x == x2) and (y_ == y2): break
                if (x_, y) not in v_obstacle:
                    try:
                        if self.route_[(x_, y)] in v_flore:  # 2-
                            self.route_[(x_, y)] = -5
                            lx.append(x_)
                            ly.append(y)
                            s += 1
                    except KeyError:
                        self.route_[(x_,y)] = -5
                        lx.append(x_)
                        ly.append(y)
                        s += 1
                if (x_ == x2) and (y == y2): break
                if (x_, y_) not in v_obstacle:
                    try:
                        if self.route_[(x_, y_)] in v_flore:  # 3-
                            self.route_[(x_, y_)] = -5
                            lx.append(x_)
                            ly.append(y_)
                            s1 += 1
                    except KeyError:
                        self.route_[(x_,y_)] = -5
                        lx.append(x_)
                        ly.append(y_)
                        s1 += 1
                if (x_ == x2) and (y_ == y2): break
                if (x__, y) not in v_obstacle:
                    try:
                        if self.route_[(x__, y)] in v_flore:  # 4-
                            self.route_[(x__, y)] = -5
                            lx.append(x__)
                            ly.append(y)
                            s1 += 1
                    except KeyError:
                        self.route_[(x__,y)] = -5
                        lx.append(x__)
                        ly.append(y)
                        s1 += 1
                if (x__ == x2) and (y == y2): break
                if (x, y__) not in v_obstacle:

                    try:
                        if self.route_[(x, y__)] in v_flore:  # 5-
                            self.route_[(x, y__)] = -5
                            lx.append(x)
                            ly.append(y__)
                            s1 += 1
                    except KeyError:
                        self.route_[(x,y__)] = -5
                        lx.append(x)
                        ly.append(y__)
                        s1 += 1

                if (x == x2) and (y__ == y2): break
                if (x__, y_) not in v_obstacle:
                    try:
                        if self.route_[(x__, y_)] in v_flore:  # 6-
                            self.route_[(x__, y_)] = -5
                    except KeyError:
                        self.route_[(x__,y_)] = -5
                    finally:
                        lx.append(x__)
                        ly.append(y_)
                        s1 += 1
                if (x__ == x2) and (y_ == y2): break
                if (x_, y__) not in v_obstacle:
                    try:
                        if self.route_[(x_, y__)] in v_flore:  # 7
                            self.route_[(x_, y__)] = -5
                    except KeyError:
                        self.route_[(x_,y__)] = -5
                    finally:
                        lx.append(x_)
                        ly.append(y__)
                        s1 += 1
                        print('====start===')
                        print(lx)
                        print(ly)
                        print("-------------")
                if (x_ == x2) and (y__ == y2): break
                if (x__, y__) not in v_obstacle:
                    try:
                        if self.route_[(x__, y__)] in v_flore:  # 8-
                            self.route_[(x__, y__)] = -5
                    except KeyError:
                        self.route_[(x__,y__)] = -5
                    finally:
                        lx.append(x__)
                        ly.append(y__)
                        s1 += 1
                if (x__ == x2) and (y__ == y2): break
            if s1 == 0:
                return [False, []]  # cela signifie qu'il n'y a aucune possibilité
        l.append(lx)
        l.append(ly)
        lt.append(l)
        del self.route_
        v1 = len(lt[-1][0])
        lt1 = []
        l1 = []
        for e in lt:
            for i in e:
                while len(i) > v1:
                    i.pop(-1)
                l1.append(i)
            lt1.append(l1)
        lt.clear()
        sizex = math.fabs(x2 - x1)
        sizey = math.fabs(y2 - y1)
        img = Image.new("RGB", (sizex, sizey))
        for e in reversed(range(len(lt1))):
            l = lt1[e]
            lx = l[0]
            ly = l[1]
            lo = len(lx) - 1
            for e in reversed(range(lx)):
                if e != lo:
                    lx.pop(e)
                    ly.pop(e)
            l.clear()
            l.append(lx)
            l.append(ly)
            lt.append(l)
        for e in range(len(lt)):
            l = lt[e]
            lx = l[0]
            ly = l[1]
            for i in range(lx):
                self.add_route(lx[i], ly[i])
                try:
                    color1 = (52, 153, 117)
                    img.putpixel((lx[i], ly[i]), color1)
                except:
                    print("L'image est trops petite pour pouvoire ajouté le pixel voulue")
        img.show()
        # a par tire d'ici, tout les liste de x et y on soit la même taille, ou elle sont plus petite.
        self.path = lt
        return [True, lt]

    def img_b(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.batiment:
                    v = str(self.batiment[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_e(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.eau:
                    v = str(self.eau[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_p(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.personnage:
                    v = str(self.personnage[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_t(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.travail:
                    v = str(self.travail[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_obj(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.object_p:
                    v = str(self.object_p[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_r(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.route:
                    v = str(self.route[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_obstacle(self, size=(100, 100)):
        """
        :argument
        :size la taille de la map: exemple: (100,100)

        si l'id est de la coordonné est un nombre ex: 1, alors, la couleur du pixel vas être (1,1,1)
        :return: un fichier image.
        """
        self.img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                xy = (x, y)
                if xy in self.obstacle:
                    v = str(self.obstacle[xy])
                    if len(v) == 1:
                        v = int(v)
                        v = (v, v, v)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 2:
                        v1 = int(v[0])
                        v2 = int(v[1])
                        v = (v1 + v2) / 2
                        v = (v, v1, v2)
                        self.img.putpixel((x, y), value=v)
                    elif len(v) == 3:
                        v = (int(v[0]), int(v[1]), int(v[2]))
                        self.img.putpixel((x, y), value=v)
                    else:
                        v = (255, 255, 255)
                        self.img.putpixel((x, y), value=v)

    def img_save(self, file_name: str = "img.jpg", size=(100, 100)):
        try:  # Si aucune affichage n'avais été appeler, il vas provoqué une erreur, pour évité l'arrête du système, une image contenent les routes seras créer.
            self.img.save(file_name)
        except:
            self.img_r(size)
            self.img.save(file_name)

    def affiche(self):
        self.img.show()

    def save_unless(self, size=(100, 100)):
        self.img_b(size)
        self.img_save("img_b.jpg")
        self.img_e(size)
        self.img_save("img_e.jpg")
        self.img_p(size)
        self.img_save("img_p.jpg")
        self.img_t(size)
        self.img_save("img_t.jpg")
        self.img_obj(size)
        self.img_save("img_obk.jpg")
        self.img_r(size)
        self.img_save("img_.jpg")


m = Maping_sqr()
m.add_eau(5, 3)
print(type(m))
print(m)
print(m.eau)

m.new_patch(5, 3, 1, 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
v = m.path_finding_r(5, 3, 1, 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(v)
