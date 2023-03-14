from pathlib import Path
from qdrant_client import QdrantClient, models
from qdrant_client.models import VectorParams, Distance, ScoredPoint
import face_recognition
import numpy as np
import hashlib
from typing import Dict, List
from exceptions import FaceAlreadyExistsException
from qdrant import search, get_encodings, register_face
from facial import parseTestImage



if __name__ == '__main__':
    with open('qdrant_key.txt', 'r') as f:
        hostname = f.readline().rstrip()
        key = f.readline().rstrip()

    qdrant_client = QdrantClient(host=hostname,
                                 api_key=key)
    
    test_list = Path('testImages').glob('*.jpg')
    for image in test_list:
        encoding = get_encodings(image)
        # if image == Path('testImages/jason0.jpg'):
        #     res = search(encoding[0])
        #     print(res)
        if image == Path('testImages/miguel.jpg'):
            res = search(qdrant_client,encoding[0])
            assert res[0].payload["name"] == "Miguel"
        # elif image == Path('testImages/maximostest0.jpg'):
        #     res = search(encoding[0])
        #     print(res)
        # elif image == Path('testImages/golfsteak1.jpg'):
        #     res = search(encoding[0])
        #     print(res)
        elif image == Path('testImages/maximostest1.jpg'):
            res = search(qdrant_client,encoding[0])
            assert res[0].payload["name"] == "Max"
        elif image == Path('testImages/rand.jpg'):
            res = search(qdrant_client,encoding[0])
            assert not res 

 
            

    

