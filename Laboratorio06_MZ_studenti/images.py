'''Modulo didattico per immagini RGB come liste di liste di tuple (R,G,B).
Compatibile con Google Colab e con PyPNG. Richiede: pip install pypng.
Interfaccia compatibile: load, save, visd.
'''
import io
import png
import IPython.display as ipd


def _righe_rgb(img):
    if not img or not img[0]:
        raise ValueError('L\'immagine deve avere almeno una riga e una colonna')
    larghezza = len(img[0])
    righe = []
    for riga in img:
        if len(riga) != larghezza:
            raise ValueError('Tutte le righe devono avere la stessa lunghezza')
        piatta = []
        for pixel in riga:
            if (not isinstance(pixel, (tuple, list)) or len(pixel) != 3
                or any(type(c) is not int or not 0 <= c <= 255 for c in pixel)):
                raise ValueError('Ogni pixel deve contenere tre interi RGB tra 0 e 255')
            piatta.extend(pixel)
        righe.append(piatta)
    return larghezza, len(img), righe


def load(filename):
    '''Legge un PNG e restituisce una lista di righe di tuple RGB.'''
    with open(filename, 'rb') as f:
        larghezza, altezza, righe_png, _ = png.Reader(file=f).asRGB8()
        return [[(riga[i], riga[i+1], riga[i+2])
                 for i in range(0, larghezza * 3, 3)]
                for riga in righe_png]


def save(img, filename):
    '''Salva una lista di liste di tuple RGB in un file PNG.'''
    larghezza, altezza, righe = _righe_rgb(img)
    with open(filename, 'wb') as f:
        png.Writer(width=larghezza, height=altezza, greyscale=False, alpha=False,
                   bitdepth=8).write(f, righe)


class Image:
    '''Adattatore per visualizzare la matrice RGB in un notebook IPython.'''
    def __init__(self, img):
        self.pixels = img

    def _repr_png_(self):
        larghezza, altezza, righe = _righe_rgb(self.pixels)
        buffer = io.BytesIO()
        png.Writer(width=larghezza, height=altezza, greyscale=False, alpha=False,
                   bitdepth=8).write(buffer, righe)
        return buffer.getvalue()


def visd(img, didascalia=''):
    '''Visualizza una matrice RGB in Jupyter/Colab, con didascalia opzionale.'''
    ipd.display(Image(img))
    if didascalia:
        print(didascalia)
