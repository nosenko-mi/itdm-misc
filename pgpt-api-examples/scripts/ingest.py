import sys
from pgpt_python.client import PrivateGPTApi
from os import listdir
from os.path import isfile, join

dir = sys.argv[1]
client = PrivateGPTApi(base_url="http://localhost:8001")
print(client.health.health())

files = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]
for file in files:
    print(f'Ingesting file: {file}')
    with open(file, "rb") as f:
        ingested_file_doc_id = client.ingestion.ingest_file(file=f).data[0].doc_id
        print(f'Ingested file id: {ingested_file_doc_id}')

    # try: 
    #     print(f'Ingesting file: {f}')
    #     ingested_file_docs = client.ingestion.ingest_file(file=f).data
    #     # for doc in ingested_file_doc_id:
    #     #     # print(doc.doc_id)
    #     print(f'File chunked into {len(ingested_file_docs)} separate documents.')
    # except Exception as e:
    #     print(f'Could not process file {f}.\n{e}')