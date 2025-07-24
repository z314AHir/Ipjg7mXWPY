
# Week 4: AWS Cloud Foundations - Data Pipeline & Application Deployment

## ✅ Week Overview
This week focuses on:
- Performing ETL processes using AWS Glue
- Creating and managing Data Catalogs
- Summarizing and transforming data
- Deploying Python applications using AWS Elastic Beanstalk
- Managing S3 logs for deployed applications

---

## 1. ✅ **ETL Architecture Visualization**

A comprehensive architecture diagram outlines the ETL workflow, data flow from ingestion to summarization, and S3 object storage. Each user group interacts with the system through clearly defined roles and pipelines.

---

## 2. ✅ **Glue Data Catalog Configuration**

Three tables were successfully added to the Glue Data Catalog:
- `aca_prg_trf_sys1`, `aca_prg_trf_sys2`, and `aca_prg_trf_sys3`  
All tables were saved in **Parquet** format and are available for querying and job linking.

---

## 3. ✅ **Glue Job: Panel-list-Summarization**

A visual ETL flow was built using AWS Glue Studio, involving:
- Extracting the panel dataset
- Schema changes
- Summarization
- Conversion to Parquet
- Final storage into S3 buckets

---

## 4. ✅ **S3 Folder: Summarized Output Storage**

Data generated from summarization was successfully saved to:
```
s3://academics-cur-lok/panel-list/metrics/system/Report_Date=2025-50-09-09:50/
```

---

## 5. ✅ **Additional Metrics Transformation**

Transformation jobs were run on datasets:
- `faculty-performance`
- `user`
- `preliminary-feedback`

All transformations produced **Parquet** outputs under respective S3 metric folders.

---

## 6. ✅ **Glue Catalog Table Update**

Four new tables were added to reflect updated metrics:
- `faculty performance metrics`
- `feedback metrics`
- `panel-list-metrics`

---

## 7. ✅ **ETL Jobs in Glue Studio**

Three summarization jobs created and successfully run:
- `Panel-list-Summarization`
- `Faculty-Performance-Summarization`
- `Preliminary-Feedback-Summarization`

---

## 8. ✅ **Final Catalog Overview**

The final Glue Data Catalog includes 6 organized tables, allowing seamless querying and future transformation tasks.

---

## 9. ✅ **Deployed Python App on Elastic Beanstalk**

A sample Python application was successfully deployed using AWS Elastic Beanstalk.
- ✅ URL loaded with **Congratulations Page**
- ✅ Python environment launched successfully

---

## 10. ✅ **Log Handling for Application**

The logs from the Elastic Beanstalk Python environment were tailed and uploaded to:
```
s3://academics-raw-lok/academics/academic-app-log/year-2025/quarter-01/month-02/day-05/TailLogs-1739154681200.txt
```

---

## ✅ Knowledge Check

**Module 2 AWS Academy Cloud Foundations Quiz**  
- Scored: **90%**
- Required: 70%  
✅ Module successfully completed.

---

## 📌 Summary

This week covered the full lifecycle of a data pipeline:
- ETL workflow setup
- Data catalog management
- Visual job execution
- Output validation
- Python application deployment on AWS
- Log maintenance on S3

**Next Steps:**  
Work on analytics and monitoring through Athena or Redshift, and automate Glue workflows.

---

![image12](https://github.com/user-attachments/assets/c6113bc7-aba4-43ba-ae93-a19909b0b8a7)
![image11](https://github.com/user-attachments/assets/3ff72b79-ccf8-4f0d-bb53-cc447492af14)
![image10](https://github.com/user-attachments/assets/9324f7be-30dc-447c-a11f-5bbe7174cfae)
![image9](https://github.com/user-attachments/assets/d5794108-689c-4b57-baf9-03c8200a08ab)
![image8](https://github.com/user-attachments/assets/c4be2be0-9f74-4a9b-b91a-5d03b4b3e7c4)
![image7](https://github.com/user-attachments/assets/afd553ee-c5a2-4398-b033-26488fcf2e09)
![image6](https://github.com/user-attachments/assets/84831183-8ebe-400c-8149-ca3a9a13a760)
![image5](https://github.com/user-attachments/assets/3e2587d9-33c9-4555-a63f-3e9ff00d9430)
![image4](https://github.com/user-attachments/assets/365b9e60-fd5a-44e1-9c7c-f2f99cf39981)
![image3](https://github.com/user-attachments/assets/089e2c4a-4076-4b58-80f6-3816132c8df2)
![image2](https://github.com/user-attachments/assets/774a7f2c-932c-4357-921d-a982d1e6e5d1)
![image1](https://github.com/user-attachments/assets/b7d1ae53-af5c-449e-b6aa-dad8ab51f103)
