import os
import struct
import base64

def get_image_info(data):
    size = len(data)
    height = -1
    width = -1
    content_type = ''

    # handle PNG
    if (size >= 24) and data.startswith(b'\211PNG\r\n\032\n') and (data[12:16] == b'IHDR'):
        content_type = 'image/png'
        w, h = struct.unpack(">LL", data[16:24])
        width = int(w)
        height = int(h)

    # handle JPEG
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        # Scan for SOF markers
        try:
            offset = 2
            while offset < size:
                # Find next marker 0xFF
                while (offset < size) and (data[offset] != 0xFF):
                    offset += 1
                
                if offset >= size - 1:
                    break
                
                # Skip padding FF
                while (offset < size) and (data[offset] == 0xFF):
                    offset += 1
                
                if offset >= size:
                    break
                    
                marker = data[offset]
                offset += 1
                
                # EOI (End of Image)
                if marker == 0xD9:
                    break
                
                length = struct.unpack(">H", data[offset:offset+2])[0]
                offset += 2
                
                # Start of Frame markers (Baseline, Progressive, etc.)
                # C0..CF, excluding C4 (DHT), C8 (JPG), CC (DAC)
                if (marker >= 0xC0) and (marker <= 0xCF) and (marker != 0xC4) and (marker != 0xC8) and (marker != 0xCC):
                    h, w = struct.unpack(">HH", data[offset+1:offset+5])
                    height = int(h)
                    width = int(w)
                    break
                    
                offset += length - 2
        except Exception:
            pass

    return content_type, width, height

LOGO_MAP = {
    'revit': 'revit.svg',
    'navisworks': 'navisworks.svg',
    'primavera': 'primavera.svg',
    'synchro': 'synchro.svg',
    'msproject': 'msproject.svg'
}

SRC_DIR = r'c:\4D\4dbim\assets\images\logos'

def convert():
    print(f"Scanning {SRC_DIR}...")
    files = os.listdir(SRC_DIR)
    
    converted_count = 0
    
    for filename in files:
        name_part = os.path.splitext(filename)[0].lower()
        
        # Match against our target logos
        target_svg = LOGO_MAP.get(name_part)
        
        # Handle 'primavera' explicitly if no extension
        if filename == 'primavera':
            target_svg = 'primavera.svg'
            
        if not target_svg:
            continue
            
        # Avoid re-processing SVGs themselves
        if filename.endswith('.svg'):
            continue
            
        filepath = os.path.join(SRC_DIR, filename)
        with open(filepath, 'rb') as f:
            data = f.read()
            
        ctype, w, h = get_image_info(data)
        
        if not ctype:
            print(f"Skipping {filename}: Could not determine image type.")
            continue
            
        print(f"Converting {filename} ({ctype}, {w}x{h}) -> {target_svg}")
        
        b64_data = base64.b64encode(data).decode('ascii')
        
        # Create SVG content
        # Use viewBox to maintain aspect ratio
        if w > 0 and h > 0:
            svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<image width="{w}" height="{h}" href="data:{ctype};base64,{b64_data}"/>
</svg>'''
        else:
            # Fallback if dimensions parsing failed
            svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
<image width="100%" height="100%" href="data:{ctype};base64,{b64_data}"/>
</svg>'''
            
        out_path = os.path.join(SRC_DIR, target_svg)
        with open(out_path, 'w') as f:
            f.write(svg_content)
            
        converted_count += 1

    print(f"Done. Converted {converted_count} images.")

if __name__ == '__main__':
    convert()
