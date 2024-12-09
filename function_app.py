# import azure.functions as func
# import logging
# from azure.storage.blob import BlobServiceClient
# import io

# # For processing PDFs
# from PyPDF2 import PdfReader

# # Connection details
# CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stginvoicepdf;AccountKey=L+C2a+5LgrnQ3qkbuVCMDmV32GZIP3W26kDdmZar8MVsB/6d0mfH3HRL1dHIe7q2SQeMBP/ymvCE+ASt0HY4Fg==;EndpointSuffix=core.windows.net"
# CONTAINER_NAME = "remittancepdfs"
# FOLDER_NAME = "Remittance PDFs"

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="ExtractData")
# def extract_data(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     try:
#         # Create a BlobServiceClient
#         blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
#         # Get container client
#         container_client = blob_service_client.get_container_client(CONTAINER_NAME)

#         # List all blobs in the folder
#         blobs = container_client.list_blobs(name_starts_with=FOLDER_NAME + "/")
#         latest_blob = None
#         latest_time = None

#         # Find the latest blob
#         for blob in blobs:
#             if latest_time is None or blob.last_modified > latest_time:
#                 latest_blob = blob.name
#                 latest_time = blob.last_modified

#         if not latest_blob:
#             return func.HttpResponse(
#                 "No files found in the specified folder.",
#                 status_code=404
#             )

#         # Log the latest file name
#         logging.info(f"Latest file retrieved: {latest_blob}")

#         # Download the blob content
#         blob_client = container_client.get_blob_client(latest_blob)
#         download_stream = blob_client.download_blob()
#         file_content = download_stream.readall()

#         # Process the file (example: PDF)
#         if latest_blob.lower().endswith(".pdf"):
#             reader = PdfReader(io.BytesIO(file_content))
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()
#             return func.HttpResponse(
#                 f"Extracted text from '{latest_blob}':\n\n{text}",
#                 status_code=200
#             )

#         # Add more processing logic for other file types (e.g., Excel, CSV, etc.)
#         return func.HttpResponse(
#             f"Latest file '{latest_blob}' downloaded but processing for this file type is not implemented.",
#             status_code=200
#         )

#     except Exception as e:
#         logging.error(f"Error processing the latest file: {e}")
#         return func.HttpResponse(
#             "An error occurred while processing the file. Please check the logs.",
#             status_code=500
#         )


#-------------------------Code2
# import azure.functions as func
# import logging
# from azure.storage.blob import BlobServiceClient
# import io
# import json

# # For processing PDFs
# from PyPDF2 import PdfReader

# # Connection details
# CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stginvoicepdf;AccountKey=L+C2a+5LgrnQ3qkbuVCMDmV32GZIP3W26kDdmZar8MVsB/6d0mfH3HRL1dHIe7q2SQeMBP/ymvCE+ASt0HY4Fg==;EndpointSuffix=core.windows.net"
# CONTAINER_NAME = "remittancepdfs"
# FOLDER_NAME = "Remittance PDFs"

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="ExtractData")
# def extract_data(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     try:
#         # Create a BlobServiceClient
#         blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
#         # Get container client
#         container_client = blob_service_client.get_container_client(CONTAINER_NAME)

#         # List all blobs in the folder
#         blobs = container_client.list_blobs(name_starts_with=FOLDER_NAME + "/")
#         latest_blob = None
#         latest_time = None

#         # Find the latest blob
#         for blob in blobs:
#             if latest_time is None or blob.last_modified > latest_time:
#                 latest_blob = blob.name
#                 latest_time = blob.last_modified

#         if not latest_blob:
#             return func.HttpResponse(
#                 "No files found in the specified folder.",
#                 status_code=404
#             )

#         # Log the latest file name
#         logging.info(f"Latest file retrieved: {latest_blob}")

#         # Download the blob content
#         blob_client = container_client.get_blob_client(latest_blob)
#         download_stream = blob_client.download_blob()
#         file_content = download_stream.readall()

#         # Process the file (example: PDF)
#         if latest_blob.lower().endswith(".pdf"):
#             reader = PdfReader(io.BytesIO(file_content))
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()

#             # Return the extracted text in JSON format
#             return func.HttpResponse(
#                 json.dumps({"file_name": latest_blob, "content": text}),
#                 status_code=200,
#                 headers={"Content-Type": "application/json"}
#             )

#         # Add more processing logic for other file types (e.g., Excel, CSV, etc.)
#         return func.HttpResponse(
#             f"Latest file '{latest_blob}' downloaded but processing for this file type is not implemented.",
#             status_code=200
#         )

#     except Exception as e:
#         logging.error(f"Error processing the latest file: {e}")
#         return func.HttpResponse(
#             "An error occurred while processing the file. Please check the logs.",
#             status_code=500
#         )


#------------------Code3------------Gimini--------------------------

# import google.generativeai as genai
# import azure.functions as func
# import logging
# from azure.storage.blob import BlobServiceClient
# import io

# # For processing PDFs
# from PyPDF2 import PdfReader

# # Configure Google Gemini API (Hardcoded API Key)
# GOOGLE_API_KEY = "AIzaSyDCvBpAvpLeVHf4boPFBfZBfINzfH_ySCo"
# genai.configure(api_key=GOOGLE_API_KEY)

# # Connection details
# CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stginvoicepdf;AccountKey=L+C2a+5LgrnQ3qkbuVCMDmV32GZIP3W26kDdmZar8MVsB/6d0mfH3HRL1dHIe7q2SQeMBP/ymvCE+ASt0HY4Fg==;EndpointSuffix=core.windows.net"
# CONTAINER_NAME = "remittancepdfs"
# FOLDER_NAME = "Remittance PDFs"

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="ExtractData")
# def extract_data(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     try:
#         # Create a BlobServiceClient
#         blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
#         # Get container client
#         container_client = blob_service_client.get_container_client(CONTAINER_NAME)

#         # List all blobs in the folder
#         blobs = container_client.list_blobs(name_starts_with=FOLDER_NAME + "/")
#         latest_blob = None
#         latest_time = None

#         # Find the latest blob
#         for blob in blobs:
#             if latest_time is None or blob.last_modified > latest_time:
#                 latest_blob = blob.name
#                 latest_time = blob.last_modified

#         if not latest_blob:
#             return func.HttpResponse(
#                 "No files found in the specified folder.",
#                 status_code=404
#             )

#         # Log the latest file name
#         logging.info(f"Latest file retrieved: {latest_blob}")

#         # Download the blob content
#         blob_client = container_client.get_blob_client(latest_blob)
#         download_stream = blob_client.download_blob()
#         file_content = download_stream.readall()

#         # Process the file (example: PDF)
#         if latest_blob.lower().endswith(".pdf"):
#             reader = PdfReader(io.BytesIO(file_content))
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()

#             # Send extracted text to Gemini for processing
#             response_text = send_to_gemini(text)
#             return func.HttpResponse(
#                 f"Extracted text from '{latest_blob}' and Gemini response: {response_text}",
#                 status_code=200
#             )

#         # Add more processing logic for other file types (e.g., Excel, CSV, etc.)
#         return func.HttpResponse(
#             f"Latest file '{latest_blob}' downloaded but processing for this file type is not implemented.",
#             status_code=200
#         )

#     except Exception as e:
#         logging.error(f"Error processing the latest file: {e}")
#         return func.HttpResponse(
#             "An error occurred while processing the file. Please check the logs.",
#             status_code=500
#         )

# def send_to_gemini(pdf_text):
#     # Prepare the input for Gemini API
#     input_prompt = """
#         You are an expert in extracting data from remittance advice documents.
#         For each remittance advice with multiple invoice numbers, create a separate row for each invoice.
#         The output should be formatted as JSON and include the following fields:
#         Invoice Number, Remittance Date, Remittance Number, Etn No, Payer Name, Payer Address, 
#         Payee Name, Payee Address, Contact No, Phone No, Country, Payment Method, Amount Paid, Payment Breakdown, 
#         Deductions, Adjustments, Bank Details, Reference Numbers, Payment Terms, Bill Ref, Net Amount, Instrument Date, Instrument No, Mode of payment,
#         Currency, Tax Amount, Discount Information, Payment Status, Payment Reason, 
#         Vendor ID, Remittance Contact Information, Purchase Order Number, Transaction Type, 
#         Adjustment Codes, Memo, Comments, Total, Amount Due, Due, Amount Paid, Due Date, Bank Account, Code, Company Name, Gross Amount, Amount, Sum Total
#     """
    
#     combined_input = f"I need the response in JSON and do not use any backticks {input_prompt}\n\nText: {pdf_text}"
    
#     # Call the Gemini API
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content([combined_input])
    
#     if hasattr(response, 'text'):
#         return response.text
#     else:
#         raise Exception("No response received from Gemini API.")



# #-------------------Save in the Json------------
import google.generativeai as genai
import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient
import io
import json
from datetime import datetime

# For processing PDFs
from PyPDF2 import PdfReader

# Configure Google Gemini API (Hardcoded API Key)
GOOGLE_API_KEY = "AIzaSyDCvBpAvpLeVHf4boPFBfZBfINzfH_ySCo"
genai.configure(api_key=GOOGLE_API_KEY)

# Connection details
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stginvoicepdf;AccountKey=L+C2a+5LgrnQ3qkbuVCMDmV32GZIP3W26kDdmZar8MVsB/6d0mfH3HRL1dHIe7q2SQeMBP/ymvCE+ASt0HY4Fg==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "remittancepdfs"
FOLDER_NAME = "Remittance PDFs"
OUTPUT_FOLDER = "OUTPUT"

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="ExtractData")
def extract_data(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        # Get container client
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # List all blobs in the folder
        blobs = container_client.list_blobs(name_starts_with=FOLDER_NAME + "/")
        latest_blob = None
        latest_time = None

        # Find the latest blob
        for blob in blobs:
            if latest_time is None or blob.last_modified > latest_time:
                latest_blob = blob.name
                latest_time = blob.last_modified

        if not latest_blob:
            return func.HttpResponse(
                "No files found in the specified folder.",
                status_code=404
            )

        # Log the latest file name
        logging.info(f"Latest file retrieved: {latest_blob}")

        # Download the blob content
        blob_client = container_client.get_blob_client(latest_blob)
        download_stream = blob_client.download_blob()
        file_content = download_stream.readall()

        # Process the file (example: PDF)
        if latest_blob.lower().endswith(".pdf"):
            reader = PdfReader(io.BytesIO(file_content))
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            # Send extracted text to Gemini for processing
            response_text = send_to_gemini(text)
            # Save response as JSON in OUTPUT folder
            save_response_as_json(response_text)
            return func.HttpResponse(
                f"Extracted text from '{latest_blob}' and Gemini response: {response_text}",
                status_code=200
            )

        # Add more processing logic for other file types (e.g., Excel, CSV, etc.)
        return func.HttpResponse(
            f"Latest file '{latest_blob}' downloaded but processing for this file type is not implemented.",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error processing the latest file: {e}")
        return func.HttpResponse(
            "An error occurred while processing the file. Please check the logs.",
            status_code=500
        )

def send_to_gemini(pdf_text):
    # Prepare the input for Gemini API
    input_prompt = """
        You are an expert in extracting data from remittance advice documents.
        For each remittance advice with multiple invoice numbers, create a separate row for each invoice.
        The output should be formatted as JSON and include the following fields:
        Invoice Number, Remittance Date, Remittance Number, Etn No, Payer Name, Payer Address, 
        Payee Name, Payee Address, Contact No, Phone No, Country, Payment Method, Amount Paid, Payment Breakdown, 
        Deductions, Adjustments, Bank Details, Reference Numbers, Payment Terms, Bill Ref, Net Amount, Instrument Date, Instrument No, Mode of payment,
        Currency, Tax Amount, Discount Information, Payment Status, Payment Reason, 
        Vendor ID, Remittance Contact Information, Purchase Order Number, Transaction Type, 
        Adjustment Codes, Memo, Comments, Total, Amount Due, Due, Amount Paid, Due Date, Bank Account, Code, Company Name, Gross Amount, Amount, Sum Total
    """
    
    combined_input = f"I need the response in JSON and do not use any backticks {input_prompt}\n\nText: {pdf_text}"
    
    # Call the Gemini API
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([combined_input])
    
    if hasattr(response, 'text'):
        return response.text
    else:
        raise Exception("No response received from Gemini API.")

def save_response_as_json(response_text):
    try:
        # Create Blob client for the OUTPUT folder
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        output_container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{OUTPUT_FOLDER}/response_{timestamp}.json"
        
        # Create Blob client for the file
        blob_client = output_container_client.get_blob_client(filename)

        # Save the JSON response
        blob_client.upload_blob(response_text, overwrite=True)
        logging.info(f"Saved Gemini API response as JSON in {filename}")

    except Exception as e:
        logging.error(f"Error saving JSON response: {e}")



