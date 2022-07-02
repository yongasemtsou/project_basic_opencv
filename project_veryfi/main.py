import veryfi
import veryfi as veryfi
import pprint

#pip install veryfi

client_id="vrfYyp52noD2IDOyXtxHM9CV4KDJ93EAGsrRf41"
client_secret="dmemA2zl2XzoM6rPoseWJXSLzdOOE4VbKhYMItBgcrrZmITESph5oDUsYiV1kLgxFGAs28ujiJsdpJ4L5OLncjAlZYiB1izTM0rkNBafRBDSGdnsXHYRvU28w96S7Fb6"
username="yongasemtsou"
api_key="b7f341d745c45be765fb39206e20ba4f"

client = veryfi.Client(client_id, client_secret, username, api_key)

categories = ["Travel", "Airfare", "Lodging", "Job Supplies and Materials", "Grocery"]
json_result= client.process_document('files/sub_1.jpg', categories)

pprint.pprint(json_result)
