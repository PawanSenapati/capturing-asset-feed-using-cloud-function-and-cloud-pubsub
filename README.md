# capturing-asset-feed-using-cloud-function-and-cloud-pubsub
This repository helps you to capture asset feed details from Cloud Asset Inventory using Cloud Function and Cloud Pub/Sub

```
1. Create a Cloud Pub/Sub topic:
--------------------------------------------
- Follow this documentation to create a Cloud Pub/Sub topic: https://cloud.google.com/pubsub/docs/create-topic#create_a_topic
```

```
2. Create an asset feed and publish the asset feed data to Cloud Pub/Sub:
------------------------------------------------------------------------------------
- Use the gcloud command:
      gcloud asset feeds create FEED_ID --project=PROJECT_ID 
      --asset-names="ASSET_NAME"
      --content-type=CONTENT_TYPE --asset-types="ASSET_TYPE"
      --pubsub-topic="projects/PROJECT_ID/topics/TOPIC_NAME"
Refer the documentation to understand different flags in the above command: https://cloud.google.com/sdk/gcloud/reference/asset/feeds/create

```

```
2. Create a Cloud Function:
--------------------------------------------
- Create a cloud function 2nd generation.
- Configure the Evantrac trigger and select the Cloud Pub/Sub topic created earlier as the trigger type. Refer this documentation: https://cloud.google.com/functions/docs/calling/eventarc#deployment
- Select "Python" runtime and use the code as in "main.py". Please note that the following is a sample code to illustrate the flow. More asset types can be added to the asset feed.
- Deploy the Cloud Function.
```

```
Check the logs of Cloud Function that is deployed to get the customised asset feed.

NOTE: Asset Feed of Cloud Function 2nd generation could be captured using the asset type "run.googleapis.com/Service" because Cloud Functions 2nd generation is Google Cloud's next-generation Functions-as-a-Service offering built on Cloud Run. Google Cloud Platform Product Engineering team is working on capturing the asset feed of Cloud Functions 2nd generation under the asset type "cloudfunctions.googleapis.com/Function".
```
