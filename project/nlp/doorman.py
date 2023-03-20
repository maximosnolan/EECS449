import time
import sys
from pathlib import Path
sys.path.insert(1, '../')
import numpy as np
import pandas as pd
import client.server_access as camera_client
from typing import Dict, List
import face_recognition
from sentence_transformers import util, SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import ScoredPoint
from facial.qdrant import get_encodings,search
from facial.facialExceptions import FaceAlreadyExistsException
from facial.serializeQdrant import *

# TODO: make local?
modelPath = 'all-MiniLM-L6-v2'
#modelPath = 'local/multi-qa-MiniLM-L6-dot-v1'
model = SentenceTransformer(modelPath)
INTENTS_CSV = 'intents.csv'

SIMILARITY_THRESHOLD = 0.54
FACE_COLLECTION_NAME = 'faces'


def search(client: QdrantClient, face_encoding):
    return client.search(
        collection_name=FACE_COLLECTION_NAME,
        query_vector=(face_encoding),
        limit=1,
        score_threshold=SIMILARITY_THRESHOLD,
        with_payload=True
    )

class Doorman:
    def __init__(self):
        # data schema from qdrant
        self.v_data = None
        # time.time() timestamp of last visitor's time
        self.v_time = 0
        self.VISITOR_TIME_DELAY_ALLOWED = 5*60 # 5 minutes
        # list of (embeddings, id) tuples
        intents_df = pd.read_csv(INTENTS_CSV)
        self.intents_embeddings = self._embed_intents(intents_df) # embed intents_df
        self.last_visitor_time = time.time()
        self.last_visitor_id = None
        self.intent_id = 0
        with open('qdrant_key.txt', 'r') as f:
            hostname = f.readline().rstrip()
            key = f.readline().rstrip()

        self.qdrant_client = QdrantClient(host=hostname,
                                    api_key=key)


    def handleRequest(self, user_speech: str) -> str:
        """Returns the text response to the user's input"""
        # if the visitor is new
        if (time.time() - self.last_visitor_time < self.VISITOR_TIME_DELAY_ALLOWED or self.v_data == None):
            # call camera and get rbg ndarray
            image = camera_client.request_image()
            camera_client.save_image(image)
            #face_embeddings = face_recognition.face_encodings(image)
            imgPath = Path('../CapturedImages/capturedImage.png')
            face_embeddings = get_encodings(imgPath)
            # call call qdrant
            results = search(self.qdrant_client, face_embeddings[0])
            if len(results) == 1:
                self.v_data = results[0].payload
                print("got a match")
                serializedPerson = person(results[0].payload)
                self.last_visitor_id = 2
        self.intent_id = self._get_intent(user_speech)
        text_response = self._get_response(self.intent_id)
        return text_response

    def _get_intent(self, user_speech: str) -> int:
        """Returns the id of the most similar intent to the user's input or None if there is no reasonable match."""
        user_embeddings = model.encode(user_speech)
        max_sim = -1.1
        max_sim_id = None
        for intent_embedding, id in self.intents_embeddings:
            sim = util.cos_sim(user_embeddings, intent_embedding)
            if max_sim < sim:
                max_sim = sim
                max_sim_id = id
        if max_sim > 0.9:
            return max_sim_id
        return None

    def _get_response(self, intent_id: int) -> str:
        if self.last_visitor_id == None:
            return "I'm not who is at the door"
        if self.intent_id == None:
            return "I'm not sure what you meant by that, please rephrase"
        if intent_id == 0:
            return f"{self.v_data['name']} is at the door"
        elif intent_id == 1:
            return f"{self.v_data['name']} was last here on {self.v_data['last_visit_date']}"
        elif intent_id == 2:
            if self.v_data['relationship'] >= 2:
                relationships_text = ", ".join(self.v_data['relationship'][:-1]) + ", and " + self.v_data['relationship'][1]
            else:
                relationships_text = self.v_data['relationship'][0]
            return f"{self.v_data['data']} is related to you by being {relationships_text}"
    def _embed_intents(self, intents_df):
        intents_embeddings = []
        for i, row in intents_df.iterrows():
            embeddings = model.encode(row.intent)
            intents_embeddings.append((embeddings,row.id))
        return intents_embeddings
