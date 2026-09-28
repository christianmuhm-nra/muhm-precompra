import math
from PIL import Image, ImageDraw

def render_shield_favicon(size=512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    scale = size / 64.0

    def s(x, y):
        return (x * scale, y * scale)

    # Coordenadas del escudo
    # d="M32 4 L53 12 C53 12 54 33 32 57 C10 33 11 12 11 12 Z"
    # Generar puntos del polígono aproximado del escudo para Pillow
    points = []
    points.append(s(32, 4))
    points.append(s(53, 12))
    
    # Curva derecha desde (53, 12) pasando por (54, 33) hasta (32, 57)
    for t in range(1, 21):
        p = t / 20.0
        # Bezier cuadratica/cubica aproximada
        # (53,12) -> (54,35) -> (32,57)
        x = (1-p)**2 * 53 + 2*(1-p)*p * 54 + p**2 * 32
        y = (1-p)**2 * 12 + 2*(1-p)*p * 36 + p**2 * 57
        points.append(s(x, y))

    # Curva izquierda desde (32, 57) pasando por (10, 33) hasta (11, 12)
    for t in range(1, 21):
        p = t / 20.0
        x = (1-p)**2 * 32 + 2*(1-p)*p * 10 + p**2 * 11
        y = (1-p)**2 * 57 + 2*(1-p)*p * 36 + p**2 * 12
        points.append(s(x, y))

    points.append(s(11, 12))

    # Dibujar borde exterior azul electrico
    draw.polygon(points, fill=(11, 27, 61, 255), outline=(37, 99, 235, 255), width=max(1, int(3 * scale)))

    # Borde interior sutil
    in_points = []
    in_points.append(s(32, 8))
    in_points.append(s(48, 14))
    for t in range(1, 21):
        p = t / 20.0
        x = (1-p)**2 * 48 + 2*(1-p)*p * 49 + p**2 * 32
        y = (1-p)**2 * 14 + 2*(1-p)*p * 32 + p**2 * 50
        in_points.append(s(x, y))
    for t in range(1, 21):
        p = t / 20.0
        x = (1-p)**2 * 32 + 2*(1-p)*p * 15 + p**2 * 16
        y = (1-p)**2 * 50 + 2*(1-p)*p * 32 + p**2 * 14
        in_points.append(s(x, y))
    in_points.append(s(16, 14))
    draw.polygon(in_points, fill=None, outline=(96, 165, 250, 110), width=max(1, int(1.2 * scale)))

    # Cabeza pistón
    draw.rounded_rectangle([s(23, 16), s(41, 29)], radius=int(2.5*scale), fill=(255, 255, 255, 255))
    draw.rectangle([s(21, 20), s(43, 22.5)], fill=(11, 27, 61, 255))
    draw.rectangle([s(25, 24), s(39, 26)], fill=(147, 197, 253, 255))

    # Biela
    draw.polygon([s(28, 29), s(30, 39), s(34, 39), s(36, 29)], fill=(226, 232, 240, 255))
    
    # Ojo de biela
    r_big = 3.5 * scale
    draw.ellipse([(32*scale - r_big, 38*scale - r_big), (32*scale + r_big, 38*scale + r_big)], fill=(147, 197, 253, 255))
    r_small = 1.5 * scale
    draw.ellipse([(32*scale - r_small, 38*scale - r_small), (32*scale + r_small, 38*scale + r_small)], fill=(11, 27, 61, 255))

    # Badge de verificación verde esmeralda
    badge_x = 44 * scale
    badge_y = 42 * scale
    r_badge_bg = 10.5 * scale
    draw.ellipse([(badge_x - r_badge_bg, badge_y - r_badge_bg), (badge_x + r_badge_bg, badge_y + r_badge_bg)], fill=(6, 78, 59, 255))
    
    r_badge = 9 * scale
    draw.ellipse([(badge_x - r_badge, badge_y - r_badge), (badge_x + r_badge, badge_y + r_badge)], fill=(16, 185, 129, 255), outline=(255, 255, 255, 255), width=max(1, int(1.8 * scale)))

    # Checkmark blanco
    check_coords = [s(40, 42), s(42.5, 44.8), s(48, 39)]
    draw.line(check_coords, fill=(255, 255, 255, 255), width=max(1, int(2.4 * scale)), joint="round")

    return img

base_img = render_shield_favicon(512)

# Export PNG sizes
ico_16 = base_img.resize((16, 16), Image.Resampling.LANCZOS)
ico_32 = base_img.resize((32, 32), Image.Resampling.LANCZOS)
ico_48 = base_img.resize((48, 48), Image.Resampling.LANCZOS)
ico_180 = base_img.resize((180, 180), Image.Resampling.LANCZOS)

ico_16.save("favicon-16x16.png")
ico_16.save("assets/favicon-16x16.png")

ico_32.save("favicon-32x32.png")
ico_32.save("assets/favicon-32x32.png")

ico_180.save("apple-touch-icon.png")
ico_180.save("assets/apple-touch-icon.png")

# Export .ico with multiple sizes
base_img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
base_img.save("assets/favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

print("All favicon assets generated successfully!")
