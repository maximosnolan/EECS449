from dataclasses import dataclass
from qdrant_client.models import VectorParams, Distance, ScoredPoint
from qdrant_client import QdrantClient, models
import hashlib
FACE_COLLECTION_NAME = 'faces'
@dataclass
class person:
    name: str
    birthday: str
    relationship: list[str]
    lastVisitDate: str
    numberOfVisits: int
    user_hash: int

    def __init__(self, payload):
        self.name = payload["name"]
        self.birthday = payload["birthday"]
        self.relationship = payload["relations"]
        self.lastVisitDate = payload["lastVisitDate"]
        self.numberOfVisits = payload["numberOfVisits"]
        self.user_hash = int(hashlib.sha256(f'{self.name}-{self.birthday}'.encode('utf-8')).hexdigest(), 16) % (10 ** 18)

    @property
    def getName(self) -> str:
        return self.name

    @property
    def getBirthday(self) -> str:
        return self.name

    @property
    def getRelationships(self) -> list[str]:
        return self.relationship

    @property
    def getLastVisitDate(self) -> str:
        return self.lastVisitDate

    @property
    def getNumberOfVisits(self) -> int:
        return self.numberOfVisits


    def updateRelationships(self, payload: list[str]):
        modifiedPayload = []
        for inputRelationship in payload:
            print(inputRelationship)
            if inputRelationship not in self.relationship:
                modifiedPayload.append(inputRelationship)
        self.relationship += modifiedPayload

        with open('qdrant_key.txt', 'r') as f:
            hostname = f.readline().rstrip()
            key = f.readline().rstrip()

            client = QdrantClient(host=hostname,
                                 api_key=key)
            client.set_payload(
            collection_name=FACE_COLLECTION_NAME,
            payload={
                "relations":self.relationship
            },
            points=[self.user_hash],
            )

    def pullRelationships(self) -> list[str]:
        with open('qdrant_key.txt', 'r') as f:
            hostname = f.readline().rstrip()
            key = f.readline().rstrip()

            client = QdrantClient(host=hostname,
                                 api_key=key)
        results = client.retrieve(
            collection_name="{collection_name}",
            ids=[self.user_hash],
        )
        return results[0].payload["relations"]

    def updateDate
