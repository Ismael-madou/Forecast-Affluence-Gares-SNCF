from google.cloud import storage, bigquery
import os
from src.config import settings

def _auth():
    key = settings.GCP_SERVICE_ACCOUNT_KEY
    if key and os.path.exists(key):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key

def create_buckets():
    client = storage.Client(project=settings.GCP_PROJECT_ID)
    for name in [settings.GCS_BUCKET_RAW, settings.GCS_BUCKET_PROCESSED, settings.GCS_BUCKET_ARCHIVE]:
        bucket = client.bucket(name)
        if bucket.exists():
            print(f"Bucket déjà existant : {name}")
        else:
            client.create_bucket(name, location="EU")
            print(f"Bucket créé : {name}")

def create_bigquery_dataset():
    bq = bigquery.Client(project=settings.GCP_PROJECT_ID)
    dataset_id = f"{settings.GCP_PROJECT_ID}.{settings.BIGQUERY_DATASET}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "EU"
    try:
        bq.create_dataset(dataset)
        print(f"Dataset créé : {dataset_id}")
    except Exception:
        print(f"Dataset déjà existant : {dataset_id}")

if __name__ == "__main__":
    _auth()
    assert settings.GCP_PROJECT_ID, "GCP_PROJECT_ID manquant"
    create_buckets()
    create_bigquery_dataset()
    print("Configuration GCP terminée.")
