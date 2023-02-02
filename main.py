import base64
import functions_framework
import json

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
   # Print out the data from Pub/Sub, to prove that it worked
   asset_data = base64.b64decode(cloud_event.data["message"]["data"])
   asset_list = json.loads(asset_data)
   asset_feed_data = asset_list['asset']

   if asset_feed_data['assetType'] == "cloudfunctions.googleapis.com/CloudFunction":
      print("Function Name:", asset_feed_data['name'],"\nAsset Type: Cloud Function 1st Generation")
   elif asset_feed_data['assetType'] == "run.googleapis.com/Service" and "goog-managed-by" in asset_feed_data["resource"]["data"]["metadata"]["labels"]:
      print("Function Name:", asset_feed_data['name'],"\nAsset Type: Cloud Function 2nd Generation")
   elif asset_feed_data['assetType'] == "run.googleapis.com/Service" and "goog-managed-by" not in asset_feed_data["resource"]["data"]["metadata"]["labels"]:
      print("Function Name:", asset_feed_data['name'],"\nAsset Type: Cloud Run Service")
