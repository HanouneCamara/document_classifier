import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from src.utils import preprocess_image

def test_preprocess_image_with_valid_input():
    import numpy as np
    from PIL import Image
    import tempfile

    # Crée une image temporaire
    image_array = np.ones((100, 100, 3), dtype=np.uint8) * 255
    img = Image.fromarray(image_array)
    with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
        img.save(tmp.name)
        result = preprocess_image(tmp.name)
        assert result is not None

def test_preprocess_image_with_invalid_input():
    with pytest.raises(Exception):
        preprocess_image(None)