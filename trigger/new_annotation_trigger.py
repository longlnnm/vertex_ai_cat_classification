from kfp.v2.google.client import AIPlatformClient
import os

PROJECT_ID = "famous-momentum-338708"
REGION = 'us-central1'
GCBUCKET = "gs://long_cat_classification"
PIPELINE_ROOT = os.path.join(GCBUCKET, "pipeline")
PIPELINE_SPEC_PATH = os.path.join("./", "pipeline", "spec", "pipeline.json")

def vertex_ai_pipeline_trigger(event, context):
    file_name = event.name["name"]
    print("File: {}".format(file_name))
    print("Extension: ()".format(file_name.split(".")[-1]))
    
    if file_name.split(".")[-1] == "jsonl":
        print("Target file extension changed")
        
        api_client = AIPlatformClient(
            project_id=PROJECT_ID,
            region=REGION
        )
        
        print("api_client is successfully instantiated. Rerunning pipeline")
        # Retrain model (use same pipeline spec)
        response = api_client.create_run_from_job_spec(
            f"{PIPELINE_SPEC_PATH}",
            pipeline_root=f"{PIPELINE_ROOT}",
            parameter_values={"project": PROJECT_ID}
        )        
        print("Response: {}".format(response))