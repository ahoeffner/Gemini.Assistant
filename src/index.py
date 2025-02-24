import os
import nltk

from VectorDB import VectorDB
from dotenv import load_dotenv
from google.cloud import aiplatform


DOCUMENTS = "../bronze/"

load_dotenv()


def main() :
	print("Starting")

	PROJECT = os.environ.get("PROJECT_ID")
	GCREGION = os.environ.get("GOOGLE_CLOUD_REGION")

	nltk.data.path = [os.environ.get("NLTK_PATH")]
	aiplatform.init(project=PROJECT, location=GCREGION)

	VectorDB.connect()
	#VectorDB.query("docker commands")
	VectorDB.status()
	#VectorDB.loadPDF(DOCUMENTS+"Python.pdf")

	#for file in os.listdir(DOCUMENTS) :
	#	VectorDB.loadPDF(DOCUMENTS+file)

main()