import os
import resvg_py
from PIL import Image

# 1. Definición del SVG Vectorial Maestro con Respiro / Margen de Seguridad Perimetral
# para imprenta, folletos, carteles y papelería (viewBox optimizado 36x36 con centro exacto en 16, 16)
SVG_FOLLETO_PRINT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 36 36" width="2048" height="2048">
  <defs>
    <linearGradient id="shieldBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1B3D"/>
      <stop offset="100%" stop-color="#11295E"/>
    </linearGradient>
  </defs>

  <!-- Escudo Base con respiro perimetral para evitar cortes en bordes de imprenta -->
  <path d="M1 0.5 L16 0 L31 0.5 C31 13 31.5 23.5 16 32 C0.5 23.5 1 13 1 0.5 Z" 
        fill="url(#shieldBg)" 
        stroke="#2563EB" 
        stroke-width="1.8" 
        stroke-linejoin="round" 
        stroke-linecap="round"/>

  <!-- Corona del Pistón (Blanco nítido pericial) -->
  <rect x="7" y="5.5" width="18" height="11" rx="2" fill="#FFFFFF"/>
  
  <!-- Ranuras de compresión oscuras -->
  <rect x="6" y="8.8" width="20" height="1.6" fill="#0B1B3D"/>
  <rect x="7" y="12.6" width="18" height="1.2" fill="#0B1B3D"/>

  <!-- Biela inferior y bulón -->
  <rect x="13.5" y="16.5" width="5" height="7.5" fill="#E2E8F0"/>
  <circle cx="16" cy="25.5" r="4" fill="#E2E8F0"/>
  <circle cx="16" cy="25.5" r="2" fill="#0B1B3D"/>

  <!-- Checkmark de Verificación Verde Neón / Esmeralda -->
  <!-- Sombra / Reborde oscuro perimetral para máximo contraste sobre cualquier fondo -->
  <path d="M7 16.5 L14 23.5 L27.5 7" 
        fill="none" 
        stroke="#060E21" 
        stroke-width="5" 
        stroke-linecap="round" 
        stroke-linejoin="round"/>
        
  <!-- Trazo verde esmeralda brillante de verificación -->
  <path d="M7 16.5 L14 23.5 L27.5 7" 
        fill="none" 
        stroke="#00E676" 
        stroke-width="3" 
        stroke-linecap="round" 
        stroke-linejoin="round"/>
</svg>"""

# 2. Versión idéntica a sangre (viewBox 0 0 32 32 original)
SVG_ORIGINAL_BLEED = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="2048" height="2048">
  <defs>
    <linearGradient id="shieldBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1B3D"/>
      <stop offset="100%" stop-color="#11295E"/>
    </linearGradient>
  </defs>

  <path d="M1 0.5 L16 0 L31 0.5 C31 13 31.5 23.5 16 32 C0.5 23.5 1 13 1 0.5 Z" 
        fill="url(#shieldBg)" 
        stroke="#2563EB" 
        stroke-width="1.8" 
        stroke-linejoin="round"/>

  <rect x="7" y="5.5" width="18" height="11" rx="2" fill="#FFFFFF"/>
  <rect x="6" y="8.8" width="20" height="1.6" fill="#0B1B3D"/>
  <rect x="7" y="12.6" width="18" height="1.2" fill="#0B1B3D"/>

  <rect x="13.5" y="16.5" width="5" height="7.5" fill="#E2E8F0"/>
  <circle cx="16" cy="25.5" r="4" fill="#E2E8F0"/>
  <circle cx="16" cy="25.5" r="2" fill="#0B1B3D"/>

  <path d="M7 16.5 L14 23.5 L27.5 7" fill="none" stroke="#060E21" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M7 16.5 L14 23.5 L27.5 7" fill="none" stroke="#00E676" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

os.makedirs("assets", exist_ok=True)

# Guardar SVG Vectorial Maestro para Illustrator / Canva / Imprenta
with open("assets/icono-motorfiable-vector.svg", "w", encoding="utf-8") as f:
    f.write(SVG_FOLLETO_PRINT)

with open("assets/icono-motorfiable-original.svg", "w", encoding="utf-8") as f:
    f.write(SVG_ORIGINAL_BLEED)

print("SVG vector files saved to assets/")

# Generar versiones PNG de Ultra Alta Resolución
# Versión 2048 x 2048 px (Folleto / Diseño estándar)
png_2048 = resvg_py.svg_to_bytes(
    svg_string=SVG_FOLLETO_PRINT, 
    width=2048, 
    height=2048, 
    dpi=300.0,
    shape_rendering="geometric_precision"
)
with open("assets/icono-motorfiable-2048x2048.png", "wb") as f:
    f.write(png_2048)
print("Rendered assets/icono-motorfiable-2048x2048.png")

# Versión 4096 x 4096 px (300 DPI Imprenta profesional / Gran Formato)
png_4096 = resvg_py.svg_to_bytes(
    svg_string=SVG_FOLLETO_PRINT, 
    width=4096, 
    height=4096, 
    dpi=300.0,
    shape_rendering="geometric_precision"
)
with open("assets/icono-motorfiable-4096x4096.png", "wb") as f:
    f.write(png_4096)
print("Rendered assets/icono-motorfiable-4096x4096.png")

# Versión 1024 x 1024 px (Web, redes, dossiers digitales)
png_1024 = resvg_py.svg_to_bytes(
    svg_string=SVG_FOLLETO_PRINT, 
    width=1024, 
    height=1024, 
    dpi=300.0,
    shape_rendering="geometric_precision"
)
with open("assets/icono-motorfiable-1024x1024.png", "wb") as f:
    f.write(png_1024)
print("Rendered assets/icono-motorfiable-1024x1024.png")

# También generar la versión original sin margen en 2048x2048
png_orig_2048 = resvg_py.svg_to_bytes(
    svg_string=SVG_ORIGINAL_BLEED, 
    width=2048, 
    height=2048, 
    dpi=300.0,
    shape_rendering="geometric_precision"
)
with open("assets/icono-motorfiable-original-2048x2048.png", "wb") as f:
    f.write(png_orig_2048)
print("Rendered assets/icono-motorfiable-original-2048x2048.png")

print("All high resolution icon assets successfully generated!")
