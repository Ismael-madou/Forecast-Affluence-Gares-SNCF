# 🚄 Data Ingestion Project – SNCF Station Footfall

## 📅 Deadline
**November 6, 2025**

---

## 🎯 Project Summary
This project aims to build a **data ingestion pipeline** to analyze **train station footfall (passenger traffic)** in relation to **weather conditions** and **public holidays/school vacations**.

The pipeline collects open data from multiple APIs, stores it in **Google Cloud Storage (GCS)**, and loads it into **BigQuery** using a **Star Schema** data model.

---

## 🧱 Main Steps

### 1️⃣ Data Collection
- **SNCF OpenData API** → Station footfall data  
- **Météo France API** → Daily weather information  
- **API Gouv** → Public holidays and school vacations  

All data is collected in JSON/CSV format.

---

### 2️⃣ Data Lake – Google Cloud Storage
Raw data from each source is stored in dedicated GCS buckets:
- `affluence-raw-data` → Raw data  
- `affluence-processed-data` → Cleaned and transformed data  
- `affluence-archive-data` → Archived datasets  

---

### 3️⃣ Data Warehouse – BigQuery
Data is structured and loaded into BigQuery using a **Star Schema** model:

- **fact_affluence** → Daily footfall metrics  
- **dim_gare** → Station information (id, name, region)  
- **dim_date** → Dates and holidays  
- **dim_meteo** → Weather measures  

---

## 🧰 Technologies
- **Language:** Python 3.10+  
- **Package Manager:** Poetry  
- **Cloud Platform:** Google Cloud Platform (GCS & BigQuery)  
- **Libraries:** pandas, requests, google-cloud-storage, google-cloud-bigquery  

---

## 👤 Authors
Academic project – *Forecast Affluence : Gares SNCF*  
**Deadline:** November 6, 2025  
Developed by **[Ismael Madou Gagi & Rilwanou mahamane]** under the supervision of **[Ouael ETTOUILEB]**  
