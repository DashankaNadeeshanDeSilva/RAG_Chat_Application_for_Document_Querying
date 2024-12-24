from charset_normalizer import detect

def get_content(content: bytes) -> str:
    # detect encoding
    detection = detect(content)
    # Default to UTF-8 if unknown
    encoding = detection.get('encoding', 'utf-8')

    # decode using the detected encoding
    try:
        text = content.decode(encoding)
    except Exception as e:
        raise ValueError(f"Failed to decode content with detected encoding {encoding}: {e}")
    
    return text


if __name__ == "__main__":

    content = b'\xff\xfeH\x00e\x00l\x00l\x00o\x00'  # UTF-16 encoded "Hello"

    try:
        text = get_content(content)
        print(f"Decoded Text: {text}")
    except ValueError as e:
        print(f"Error: {e}")